"""
    This file contains all of the necessary components for the application to connect to a data source via
    SQLAlchemy.
"""

import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, inspect

class DB_Connector():

    def __init__(self, conn_name):
        """
            This function initializes the DB_Connector class by exposing various parts of the SQLAlchemy
            architecture to the class.

            :param conn_name: The name of the connection that well be creating from the already read in connections
            array.
            :type conn_name: str.
        """
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
        """
            This method gets a table given a name through SQLAlchemy's reflection capability.

            :param table_name: Name of the table that we want to instantiate.
            :type table_name: str.
            :returns: SQLAlchemy Table object.
        """
        table = Table(table_name, self.meta)
        self.insp.reflecttable(table, None)

        return table

    def getCount(self, table_name):
        """
            This method gets a count of records given a table_name.

            :param table_name: Name of the table that we want to count records from.
            :type table_name: str.
            :returns: SQLAlchemy result of the count.
        """
        table = self.getTable(table_name)
        res = self.session.query(table).count()

        return res

    def insertInto(self, table_name, records):
        """
            This method inserts given records into a table.

            :param table_name: Name of the table that we want to insert into.
            :type table_name: str.
            :param records: A key, value pair of records to insert.
            :type table_name: arr.
        """
        table = self.getTable(table_name)
        ins = table.insert().values(records)
        self.conn.execute(ins)

    def deleteFrom(self, table_name):
        """
            This method deletes all records from a table.

            :param table_name: Name of the table that we want to delete from.
            :type table_name: str.
        """
        table = self.getTable(table_name)
        delete = table.delete()
        self.conn.execute(delete)

    def selectFrom(self, table_name):
        """
            This method selects all from a table.

            :param table_name: Name of the table that we want to select from.
            :type table_name: str.
            :returns: A jsonified result from SQLAlchemy.
        """
        table = self.getTable(table_name)
        res = self.session.query(table).all()
        # This commented block will likely be used instead of the query so we can get individual columns
        # from sqlalchemy.sql import select
        # sel = select(columns=['test', 'id'], from_obj=table)
        # res = list(self.conn.execute(sel))

        json_res = self.to_json(res, table)

        return json_res

    def to_json(self, qry_results, table):
        """
            This method jsonifies the SQLAlchemy query result.

            :param qry_results: Results from SQLAlchemy's query call.
            :type qry_results: SQLAlchemy ResultSet.
            :returns: Jsonified SQLAlchemy ResultSet.
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

from datetime import datetime

# Who can't jsonify datetimes :P
class CustomEncoder(json.JSONEncoder):
    """
        This class is a custom JSON encoder. Only required if we need to jsonify datetimes.
    """

    def default(self, obj):
        """
            Method to actually perform the jsonifying action.

            :param obj: The object that we are jsonifying.
            :returns: Jsonified object.
        """
        if isinstance(obj, datetime):
            # is iso format ok, or do we want something different?
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    connector = DB_Connector('test conn')
    if connector.getCount('test') == 0:
        connector.insertInto('test', [{'test': 0}])
    print connector.selectFrom('test')