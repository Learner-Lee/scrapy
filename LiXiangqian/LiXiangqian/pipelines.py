# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class ScrapyMySQLPipeline:
    def __init__(self):
        self.conn = pymysql.Connect(host='127.0.0.1', user='root', password='123456', port=3306, database='LXQDB',
                                    charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        '''
        CREATE TABLE YourTableName (id INT AUTO_INCREMENT PRIMARY KEY,tital VARCHAR(255),detail VARCHAR(255),price VARCHAR(255));
        '''
        sql_str = "insert into t_LXQ(tital,detail,price) values (%s,%s,%s)"
        args = [item['tital'], item['detail'], item['price']]
        # 提交事务
        self.cur.execute(sql_str, args)
        self.conn.commit()
        return item

    def __del__(self):
        self.cur.close()
        self.conn.close()
