from flask import Flask

def create_app():
    app = Flask(__name__)

    from controller import user
    app.register_blueprint(user.bp)

    from controller import feed
    app.register_blueprint(feed.bp)

    from controller import feed_upload
    app.register_blueprint(feed_upload.bp)

    return app

