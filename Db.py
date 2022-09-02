import pymysql
import random


class Db:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='fdwjtz', database='screenshot')
        self.cursor = self.db.cursor()

    def get_disdata(self, num):
        tb_data = []
        for i in range(num):
            tb_id = random.randint(1, 15)
            state = f'select dis,spe,tim from dis where id={tb_id}'
            self.cursor.execute(state)
            tb_data.append(self.cursor.fetchone())
        return tb_data

    def __del__(self):
        self.db.close()
