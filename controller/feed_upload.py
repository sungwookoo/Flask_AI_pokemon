from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
# from user import authrize

bp = Blueprint('feed_upload', __name__, url_prefix='/')

client = MongoClient('localhost', 27017)
db = client.dbpokemon

@bp.route('/main')
def home():
    return render_template('index.html')

# 이미지 전송(POST)
@bp.route('/api/feed_upload', methods=['POST'])
def file_upload():
    title_receive = request.form['title_give']
    file = request.files['file_give']
    # user_id = request.form['user_id']
    # content = request.form['content']
    # feed_img_src = request.form['feed_img_src']

    # 확장자명 설정
    extension = 'jpg'
    # 파일 이름이 중복되면 안되므로, 지금 시간을 해당 파일 이름으로 만들어서 중복이 되지 않게 함!
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'{title_receive}-{mytime}'
    # 파일 저장 경로 설정 (파일은 db가 아니라, 서버 컴퓨터 자체에 저장됨)
    save_to = f'static/uploads/{filename}.{extension}'
    # 파일 저장!
    file.save(save_to)

    doc = {
        # 'user_id': user_id,
        'created_at': mytime,
        # 'feed_img_src': ,
        # 'content': content
    }
    db.feed.insert_one(doc)
    return jsonify({'result': '업로드 완료!'})
