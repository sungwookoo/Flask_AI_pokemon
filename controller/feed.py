from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient
from util.common import object_id_to_string
from controller.user import authrize

bp = Blueprint('feed', __name__, url_prefix='/')

client = MongoClient('localhost', 27017)
db = client.dbpokemon


@bp.route('/history')
@authrize
def get_history(user):
    return render_template('history.html', email=user['user_id'])


@bp.route('/api/get_feed', methods=['GET'])
@authrize
def get_feed(user):
    page = int(request.args.get('page'))

    find_user = list(db.user.find({'user_id': user['user_id']}))
    find_user = object_id_to_string(find_user)

    # total_feed = db.feed.count_documents({'user_id': user_id})
    # feed_list = list(db.feed.find({'user_id': user_id}).skip((page - 1) * 8).limit(8))
    pipeline = [
        {
            "$group": {
                "_id": "$feed_img_src",
                "user_id": {"$addToSet": "$user_id"}
            }
        },
        {
            "$match": {"user_id": {"$in": [user['user_id']]}}
        },
        {
            "$sort": {"_id": 1}
        },
        {
            "$skip": (page - 1) * 8
        },
        {
            "$limit": 8
        }
    ]

    total_pipeline = [
        {
            "$group": {
                "_id": "$feed_img_src",
                "user_id": {"$addToSet": "$user_id"}
            }
        },
        {
            "$match": {"user_id": {"$in": [user['user_id']]}}
        },
        {
            "$sort": {"_id": 1}
        }
    ]
    total_feed_list = list(db.feed.aggregate(total_pipeline))

    feed_list = list(db.feed.aggregate(pipeline))
    feed_list = object_id_to_string(feed_list)

    return jsonify({
        'feed_list': feed_list,
        'total_feed': len(total_feed_list),
        'page': str(page),
        'user': find_user
    })


@bp.route('/api/get_user', methods=['GET'])
@authrize
def get_user(user):
    user = list(db.user.find({'user_id': user['user_id']}))
    user = object_id_to_string(user)

    return jsonify({
        'user': user
    })

