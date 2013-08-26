import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, inspect

class DB_Connector():

    def __init__(self, conn_name):

        from etlunit.template_base.connections_reader import connections
        connection = connections[conn_name]

        if connection is None:
            exit()

        self.engine = create_engine('{}://{}:{}@{}:{}/{}'.format(
            connection['dbtype'],
            connection['user'],
            connection['pass'],
            connection['host'],
            connection['port'],
            connection['dbname']
        ))

        self.meta = MetaData()
        self.insp = inspect(self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.conn = self.engine.connect()

    def getTable(self, table_name):
        table = Table(table_name, self.meta)
        self.insp.reflecttable(table, None)

        return table

    def getCount(self, table_name):
        table = self.getTable(table_name)
        res = self.session.query(table).count()

        return res

    def insertInto(self, table_name, records):
        table = self.getTable(table_name)
        ins = table.insert().values(records)
        self.conn.execute(ins)

    def deleteFrom(self, table_name):
        table = self.getTable(table_name)
        delete = table.delete()
        self.conn.execute(delete)

    def selectFrom(self, table_name):
        table = self.getTable(table_name)
        res = self.session.query(table).all()
        json_res = self.to_json(res, table)

        return json_res

    def to_json(self, qry_results, table):
        """
            Jsonify the sql alchemy query result.
        """
        results = []
        if type(qry_results) is list:
            col_types = dict()
            for qry_result in qry_results:
                table_json = {}
                for col in table._columns:
                    value = getattr(qry_result, col.name)
                    if col.type in col_types.keys() and value is not None:
                        try:
                            table_json[col.name] = col_types[col.type](value)
                        except:
                            table_json[col.name] = "Error:  Failed to convert using ", str(col_types[col.type])
                    elif value is None:
                        table_json[col.name] = str()
                    else:
                        table_json[col.name] = value
                results.append(table_json)
            # return json.dumps(results, cls=CustomEncoder)  # use the custom encoder to jsonify datetimes
            return results
        else:
            return self.to_json([qry_results], table)

# Who can't jsonify datetimes :P
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            # is iso format ok, or do we want something different?
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    connector = DB_Connector('test conn')
    if connector.getCount('test') == 0:
        connector.insertInto('test', [{'test': 0}])
    print connector.selectFrom('test')