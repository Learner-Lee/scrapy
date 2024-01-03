# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
import csv


class LixiangqianPipeline:
    def __init__(self):
        self.conn = pymysql.Connect(host='127.0.0.1', user='root', password='baidu123',
                                    port=3306, database='LXQDB',charset='utf8')
        self.cur = self.conn.cursor()

        # 创建表格（如果不存在）
        self.creat_table()




    def ave_to_csv(self, item):
        # 打开 CSV 文件，如果不存在会创建一个新的
        f = open("2.csv", "a", newline="", encoding="utf-8")

        # 定义 CSV 文件的表头
        headers = ["headline", "data"]

        # 创建一个 DictWriter 对象，用于写入 CSV 文件
        dw = csv.DictWriter(f, headers)

        # 写入 CSV 文件的表头
        # dw.writeheader()

        # 输入格式
        news = {'headline': item['headline'], 'data': item['data']}

        # 逐行写入书籍信息
        dw.writerow(news)

        # 关闭 CSV 文件
        f.close()

    def creat_table(self):
        # 创建表格的 SQL 语句
        create_table_sql = '''
                CREATE TABLE IF NOT EXISTS t_LXQ (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    headline VARCHAR(255),
                    newsdata VARCHAR(255)
                );
                '''

        # 执行创建表格的 SQL 语句
        self.cur.execute(create_table_sql)

        # 提交事务
        self.conn.commit()

    def process_item(self, item, spider):
        sql_str = "insert into t_LXQ(headline,newsdata) values (%s,%s)"
        args = [item['headline'], item['data']]
        # 提交事务
        self.cur.execute(sql_str, args)
        self.conn.commit()

        #保存进csv
        self.ave_to_csv(item)
        return item

    def traverse_table(self):
        # 查询表中所有数据的 SQL 语句
        select_all_sql = "SELECT * FROM t_LXQ"

        # 执行查询操作
        self.cur.execute(select_all_sql)

        # 获取所有查询结果
        all_data = self.cur.fetchall()

        # 遍历查询结果并处理
        for row in all_data:
            # row 是一个包含每一行数据的元组
            # 在这里，你可以根据需要处理每一行数据
            print(row)

    def __del__(self):
        # 遍历表
        self.traverse_table()
        self.cur.close()
        self.conn.close()

