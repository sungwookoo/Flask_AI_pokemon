from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
from controller.yolocheck import yolo
import os

bp = Blueprint('feed_upload', __name__, url_prefix='/')

client = MongoClient('localhost', 27017)
db = client.dbpokemon

@bp.route('/main')
def home():
    return render_template('index.html')

# 이미지 전송(POST)
@bp.route('/api/feed_upload', methods=['POST'])
def file_upload():
    file = request.files['file_give']
    save_to = 'static/uploads/temp.jpg'
    # 파일 저장!
    file.save(save_to)
    result = yolo()
    file_path = 'static/uploads/temp.jpg'
    os.remove(file_path)
    if result == 'fail':
        return jsonify({'result': '업로드 실패'})

    return jsonify({'result': '업로드 완료!'})
