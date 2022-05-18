from flask import Blueprint, render_template, jsonify, request

bp = Blueprint('feed_upload', __name__, url_prefix='/')


@bp.route('/api/feed_upload')
def feed_upload():
    return


@bp.route('/api/get_hello', methods=['GET'])
def hello():
    user_id = request.args.get('user_id')
    return jsonify({
        'msg': 'hello',
        'name': 'hwisu',
        'user_id': user_id
    })


@bp.route('/api/post_hello', methods=['POST'])
def save_comment():
    msg_receive = request.form['msg']
    if msg_receive == 'hello':
        return jsonify({'msg': '댓글이 작성되었습니다.'})
    else:
        return jsonify({'msg': msg_receive})
