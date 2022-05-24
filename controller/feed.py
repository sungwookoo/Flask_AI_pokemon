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
    db.user.update_one({'user_id': user['user_id']}, {'$set': {'number_of_poke': len(total_feed_list)}})
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


@bp.route('/api/rank', methods=['GET'])
def getrank():
    find_user = list(db.user.find({}))
    find_user = object_id_to_string(find_user)
    rankli = []
    c = 0
    for i in range(len(find_user)):
        if i == 0:
            rankli.append(find_user[0])
        else:
            while c < len(rankli):
                if rankli[len(rankli) - c - 1]['number_of_poke'] >= find_user[i]['number_of_poke']:
                    rankli.insert(len(rankli) - c, find_user[i])
                    break
                elif c == len(rankli) - 1:
                    rankli.insert(0, find_user[i])
                c += 1
    print(rankli)

    return jsonify({
        'rankli': rankli
    })
