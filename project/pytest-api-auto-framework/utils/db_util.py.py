import pymysql
from conf.config import DB_CONFIG

class DBUtil:
    def __init__(self):
        try:
            self.conn = pymysql.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        except Exception as e:
            print(f"数据库连接失败: {e}")

    def query_one(self, sql, params=None):
        """查询单条数据，用于断言"""
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()

db = DBUtil()