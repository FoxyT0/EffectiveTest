from flask import Blueprint, request
from pymongo import MongoClient

app_blueprint = Blueprint('app_blueprint', __name__)
client = MongoClient('localhost', 27017)
db = client.test
formsDB = db.forms

@app_blueprint.route('/', methods=["GET"])
def index():
    return "<h1>Application for forms is up.</h1>"

@app_blueprint.route('/forms/create', methods=["POST"])
def create_form():
    requestData = request.get_json()
    formsDB.insert_one(requestData)
    return '', 200

@app_blueprint.route('/forms', methods=["GET"])
def get_all_forms():
    cursor = formsDB.find({})
    forms = ""
    for form in cursor:
            forms += str(form) + "<p>"
    if (forms == ""):
        forms = "Нет ни одной формы."
    return f"{forms}"

@app_blueprint.route('/forms/<int:form_id>', methods=["GET"])
def get_one_forms(form_id):
    form = formsDB.find_one({"_id":form_id})
    return f"{form}"
