from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient
from util.common import object_id_to_string

bp = Blueprint('feed', __name__, url_prefix='/')

client = MongoClient('localhost', 27017)
db = client.dbpokemon


@bp.route('/main')
def get_history():
    return render_template('history.html')


@bp.route('/api/get_feed', methods=['GET'])
def get_feed():
    user_id = request.args.get('user_id')
    page = int(request.args.get('page'))

    user = db.user.find_one({'user_id': user_id, '_id': False})
    feed_list = list(db.feed.find({'user_id': user_id}).skip((page - 1) * 9).limit(9))
    feed_list = object_id_to_string(feed_list)

    return jsonify({
        'feed_list': feed_list,
        'page': str(page + 1),
        'user': user
    })
