from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient
from util.common import object_id_to_string

bp = Blueprint('feed', __name__, url_prefix='/')

client = MongoClient('localhost', 27017)
db = client.dbpokemon


@bp.route('/history')
def get_history():
    return render_template('history.html')


@bp.route('/api/get_feed', methods=['GET'])
def get_feed():
    user_id = request.args.get('user_id')
    page = int(request.args.get('page'))

    user = list(db.user.find({'user_id': user_id}))
    user = object_id_to_string(user)
    user = user[0]

    total_feed = db.feed.count_documents({'user_id': user_id})
    feed_list = list(db.feed.find({'user_id': user_id}).skip((page - 1) * 8).limit(8))
    feed_list = object_id_to_string(feed_list)

    return jsonify({
        'feed_list': feed_list,
        'total_feed': total_feed,
        'page': str(page),
        'user': user
    })


@bp.route('/api/get_user', methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    user = list(db.user.find({'user_id': user_id}))
    user = object_id_to_string(user)
    user = user[0]

    return jsonify({
        'user': user
    })
