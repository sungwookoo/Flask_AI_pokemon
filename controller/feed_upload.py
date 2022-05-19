from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
import os
from werkzeug.utils import secure_filename


bp = Blueprint('feed_upload', __name__, url_prefix='/')

client = MongoClient('localhost', 27017)
db = client.dbpokmon


@bp.route('/main')
def home():
    return render_template('index.html')

# 이미지 전송(POST)
@bp.route('/api/feed_upload', methods=['POST'])
def file_upload():
    title_receive = request.form['title_give']
    file = request.files['file_give']
    user_id = request.form['user_id']
    content = request.form['content']
    created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    # 해당 파일에서 확장자명만 추출
    extension = file.filename.split('.')[-1]
    # 파일 이름이 중복되면 안되므로, 지금 시간을 해당 파일 이름으로 만들어서 중복이 되지 않게 함!
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'{title_receive}-{mytime}'
    # 파일 저장 경로 설정 (파일은 db가 아니라, 서버 컴퓨터 자체에 저장됨)
    save_to = f'static/{filename}.{extension}'
    # 파일 저장!
    file.save(save_to)

    # 아래와 같이 입력하면 db에 추가 가능!
    doc = {'title': title_receive, 'img': f'{filename}.{extension}'}
    db.camp.insert_one(doc)

    doc = {
        'feed_img_src': feed_img_src,
        'user_id': user_id,
        'content': content,
        'created_at': created_at
    }

    db.feed.insert_one(doc)
    return jsonify({'result': 'success'})

# 주소에다가 /fileshow/이미지타이틀 입력하면 그 이미지타이틀을 title이라는 변수로 받아옴
@bp.route('/fileshow/<title>')
def file_show(title):
    # title은 현재 이미지타이틀이므로, 그것을 이용해서 db에서 이미지 '파일'의 이름을 가지고 옴
    img_info = db.camp.find_one({'title': title})
    # 해당 이미지 정보를 jinja 형식으로 사용하기 위해 넘김
    return render_template('showimg.html', img_info=img_info)




# <<포스트맨 사용 예제>> ##
# @bp.route('/api/get_hello', methods=['GET'])
# def hello():
#     user_id = request.args.get('user_id')
#     return jsonify({
#         'msg': 'hello',
#         'name': 'hwisu',
#         'user_id': user_id
#     })
#
#
# @bp.route('/api/post_hello', methods=['POST'])
# def save_comment():
#     msg_receive = request.form['msg']
#     if msg_receive == 'hello':
#         return jsonify({'msg': '댓글이 작성되었습니다.'})
#     else:
#         return jsonify({'msg': msg_receive})
