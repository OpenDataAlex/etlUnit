import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, inspect

class DB_Connector():

    __table_name = 'aw_jobexecution'

    def __init__(self, connection):
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

    def getTable(self, table_name):
        table = Table(table_name, self.meta)
        self.insp.reflecttable(table, None)

        return table

    # def getAll(self):
    #     table = self.getTable(self.__table_name)
    #     res = self.session.query(table).all()
    #     json_res = self.to_json(res, table)
    #
    #     return json_res

    # def getOne(self, name):
    #     table = self.getTable(self.__table_name)
        # get values where name is like the name param
        # res = self.session.query(table)\
        #     .filter(table.columns.name.like("%{}%".format(name))).all()
        # json_res = self.to_json(res, table)
        #
        # return json_res

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
            return json.dumps(results, cls=CustomEncoder)  # use the custom encoder to jsonify datetimes
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
