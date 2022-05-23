from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from controller.user import authrize


bp = Blueprint('feed_result', __name__, url_prefix='/')

client = MongoClient('localhost', 27017)
db = client.dbpokemon

@bp.route('/result')
def result():
    return render_template('result.html')

@bp.route('/api/get_imgresult', methods=['GET'])
def get_imgresult():
    result = list(db.feed.find())
    result_img = result[-1]['feed_img_src']
    print(result_img)
    return jsonify({
        'result_img': result_img
    })

@bp.route('/api/get_pokeresult', methods=['GET'])
def get_pokeresult():
    result = list(db.feed.find())
    result_poke = result[-1]['poke_li'][0]
    print(result_poke)
    return jsonify({
        'result_poke':result_poke
    })
@bp.route('/api/get_accresult', methods=['GET'])
def get_accresult():
    result = list(db.feed.find())
    result_acc = result[-1]['acc_li'][0]
    print(result_acc)
    return jsonify({
        'result_acc':result_acc
    })
