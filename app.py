from flask import Flask
from routes.pokenea_routes import pokenea_bp

app = Flask(__name__)
app.register_blueprint(pokenea_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
