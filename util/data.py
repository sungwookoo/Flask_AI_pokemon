import datetime
from pymongo import MongoClient
import random
import hashlib

client = MongoClient('localhost', 27017)
db = client.dbpokemon
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')


def random_img_src():
    return "https://picsum.photos/" + str(100 * random.randint(1, 7))


def random_password():
    return hashlib.sha256(str(random.randint(1, 1000)).encode('utf-8')).hexdigest()


def random_phone():
    return "010" + str(random.randint(1000, 9999)) + str(random.randint(1000, 9999))


# doc : 데이터 doc, table : '테이블이름'
def make_insert(doc, table):
    """ make_insert 사용 예시
    for i in range(10):
        doc = {
            'user_id': 'test',
            'content': '',
            'created_at': now,
            'feed_img_src': random_img_src()
        }
        make_insert(doc, 'feed')
    """
    db_table = getattr(db, table)
    db_table.insert_one(doc)


for i in range(10):
        doc = {
            'user_id': 'test@test.com',
            'content': str(i),
            'created_at': now,
            'feed_img_src': random_img_src()
        }
        make_insert(doc, 'feed')