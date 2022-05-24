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


labeldn = {"person": "mr-mime", "bicycle": "dodrio", "car": "entei", "motorbike": "dialga", "aeroplane": "latios",
           "bus": "caterpie", "train": "onix", "truck": "pelipper",
           "boat": "blastoise", "traffic light": "pikachu", "fire hydrant": "squirtle", "stop sign": "hypno",
           "parking meter": "psyduck", "bench": "bulbasaur",
           "bird": "pidgeotto", "cat": "meowth", "dog": "growlithe", "horse": "ponyta", "sheep": "mareep",
           "cow": "tauros", "elephant": "phanpy", "bear": "ursaring", "zebra": "blitzle", "giraffe": "girafarig",
           "backpack": "chikorita", "umbrella": "foongus", "handbag": "azurill", "tie": "ekans",
           "suitcase": "trubbish", "frisbee": "jigglypuff", "skis": "lapras", "snowboard": "articuno",
           "sports ball": "voltorb", "kite": "mantyke", "baseball bat": "Farfetchd", "baseball glove": "binacle",
           "skateboard": "chimecho", "surfboard": "cofagrigus", "tennis racket": "cradily", "bottle": "gardevoir",
           "wine glass": "lileep",
           "cup": "lugia", "fork": "sigilyph", "knife": "pawniard", "spoon": "kadabra", "bowl": "wobbuffet",
           "banana": "tropius", "apple": "tsareena", "sandwich": "dugtrio",
           "broccoli": "budew", "carrot": "lopunny", "hot dog": "diglett", "pizza": "blaziken", "donut": "comfey",
           "cake": "gothitelle", "chair": "metagross", "sofa": "dewgong", "potted plant": "oddish",
           "bed": "clefable",
           "diningtable": "torterra", "toilet": "weepinbell", "tv monitor": "charjabug", "laptop": "torkoal",
           "mouse": "dedenne",
           "remote": "umbreon", "keyboard": "kyogre", "cell phone": "mewtwo", "microwave": "rotom",
           "oven": "paras", "toaster": "snorlax", "sink": "gyarados", "refrigerator": "meltan", "book": "slowpoke",
           "clock": "noctowl",
           "vase": "venusaur", "scissors": "scizor", "teddy bear": "teddiursa", "hair drier": "bellsprout",
           "toothbrush": "poliwag", "orange": "trapinch"}


labeldn_values = list(labeldn.values())

for label in labeldn_values:
    poke_li = ["banana", "bird"]
    acc_li = [98.9956200122833, 73.5150396823883]
    doc = {
        'user_id': 'test@test.com',
        'poke_li': poke_li,
        'acc_li': acc_li,
        'created_at': now,
        'feed_img_src': 'static/pokemon/'+label+'.png'
    }
    make_insert(doc, 'feed')
