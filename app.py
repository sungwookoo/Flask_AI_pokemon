from __init__ import create_app

if __name__ == '__main__':
    create_app().run('0.0.0.0', port=5001, debug=True)
