import os
import sqlite3
from datetime import datetime


class LogMe(object):

    def __init__(self, path=None):
        """
        Initialize logging object and setup schema

        :param path:
        """
        self._db_path = None
        self._db_schema_path = 'schema.sql'
        self._conn = None

        if path is not None:
            self._db_path = path
        else:
            self._db_path = 'measurement.db'

        self._db_schema_path = 'schema.sql'
        db_is_new = not os.path.exists(self._db_path)

        self.open_database()

        if db_is_new:
            self._create_schema()
        self.close_database()

    def _create_schema(self):
        """
        Create the measurement schema in the database
        :return:
        """
        with open(self._db_schema_path, 'rt') as f:
            schema = f.read()
            self._conn.executescript(schema)

    def open_database(self):
        """
        Open a connection to the database
        :return:
        """
        if self._conn is None:
            self._conn = sqlite3.connect(self._db_path)

    def close_database(self):
        """
        Close the connection to the database
        :return:
        """
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def log(self, metric, value, source, timestamp):
        """
        Log a row to the database
        :param metric:
        :param value:
        :param source:
        :param timestamp:
        :return:
        """
        self.open_database()
        sql = "insert into measurement(metric, value, source, timestamp) values('{0}', {1}, '{2}', '{3}');".format(
            metric, value, source, timestamp)
        self._conn.executescript(sql)


if __name__ == '__main__':
    ts = datetime.now()
    log = LogMe(path='test.db')
    log.log('CPU', 0.8, 'foo', ts)
