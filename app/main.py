from flask import Flask
from app.endpoints import app_blueprint 

class App:
    
    def __init__(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(app_blueprint)
       
    def run(self):
        self.app.run(debug=True)
