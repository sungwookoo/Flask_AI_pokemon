from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
import os
from werkzeug.utils import secure_filename


bp = Blueprint('feed_upload', __name__, url_prefix='/')

client = MongoClient('localhost', 27017)
db = client.dbpokemen


@bp.route('/main')
def home():
    return render_template('index.html')

# 작업중

# @bp.route('/api/feed_upload', methods=['POST'])
# def file_upload():
#     title_receive = request.form['title_give']
#     file = request.files['file_give']
#     extension = file.filename.split('.')[-1]
#     today = datetime.now()
#     mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
#     filename = f'{title_receive}-{mytime}'
#     save_to = f'static/uploads/{filename}.{extension}'
#     file.save(save_to)
#
#     doc = {'title':title_receive, 'img':f'{filename}.{extension}'}
#     db.camp.insert_one(doc)
#
#     return jsonify({'result':'success'})

    # if request.files['file']:
    #     if request.method == 'POST':
    #         file = request.files['file']
    #         content = request.form['content']
    #         user_id = request.form['user_id']
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join('static', 'uploads', filename))
    #         feed_img_src = os.path.join('static', 'uploads', filename)
    #         created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    #
    #         doc = {
    #             'user_id': user_id,
    #             'feed_img_src': feed_img_src,
    #             'content': content,
    #             'created_at': created_at
    #         }
    #
    #         db.feed.insert_one(doc)



## <<포스트맨 사용 예제>> ##
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
