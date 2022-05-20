from flask import Blueprint, render_template, jsonify, request, abort
bp = Blueprint('user', __name__, url_prefix='/')
from functools import wraps
import jwt
import hashlib
from config.config import Config
from pymongo import MongoClient
from datetime import date, datetime, timedelta

client = MongoClient('localhost', 27017)
db = client.dbpokemon

SECRET_KEY = Config.SECRET_KEY

@bp.route('/')
def login():
    return render_template('login.html')

def authrize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not 'mytoken' in request.cookies:
            abort(401)
        user = None
        token = request.cookies['mytoken']
        try:
            user = jwt.decode(token,SECRET_KEY, algorithms=['HS256'])
        except:
            abort(401)
        return f(user, *args, **kws)

    return decorated_function


@bp.route('/main')
@authrize
def home(user):
    if user is not None:
        return render_template('index.html')

@bp.route('/signup')
def signup_page():
    return render_template('signup.html')

@bp.route('/api/signup', methods=["POST"])
def check():
    new_id_receive = request.form['new_id_give']
    new_pw_receive = request.form['new_pw_give']
    new_nick_name_receive = request.form['new_nick_name_give']
    hashed_password = hashlib.sha256(new_pw_receive.encode('utf-8')).hexdigest()

    doc1 = {
        'user_id': new_id_receive
    }
    doc2 = {
        'nick_name': new_nick_name_receive
    }

    check_id = db.user.find_one(doc1)
    check_nick_name = db.user.find_one(doc2)

    if check_id is None and check_nick_name is None:
        doc = {
            "user_id": new_id_receive,
            "password": hashed_password,
            "nick_name": new_nick_name_receive
            }
        db.user.insert_one(doc)
        return jsonify({"result": "success", 'msg': '회원가입을 축하합니다.', 'url': "/"})

    elif check_id is not None:
        return jsonify({"result": "fail", 'msg': '중복되는 아이디가 있습니다.', 'url': '/signup'})

    elif check_nick_name is not None:
        return jsonify({"result": "fail", 'msg': '중복되는 닉네임이 있습니다.', 'url': '/signup'})


@bp.route('/login',methods=['POST'])
def sign_in():
    email_receive = request.form['email_give']
    pw_receive = request.form['pw_give']
    hashed_pw = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    result = db.user.find_one({'user_id':email_receive, 'password': hashed_pw})

    if result is not None:
        payload = {
            'user_id' : str(result.get('user_id')),
            'nick_name':result.get('nick_name')
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result':'fail', 'msg': 'id, pw 를 확인해주세요'})