from flask import Blueprint, request
from pymongo import MongoClient, errors
from app.formExist import formExist


app_blueprint = Blueprint('app_blueprint', __name__)
client = MongoClient('localhost', 27017)
db = client.test
formsDB = db.forms


@app_blueprint.route('/forms/create', methods=["POST"])
def create_form():
    requestData = request.get_json()
    created_form_id = requestData['_id']
    if not (formExist(formsDB, created_form_id)):
        formsDB.insert_one(requestData)
        return '', 200
    return '', 409


@app_blueprint.route('/forms', methods=["GET"])
def get_all_forms():
    cursor = formsDB.find({})
    forms = list()
    for form in cursor:
            forms.append(form)
    if (forms == list()):
        return '', 204
    return forms, 200


@app_blueprint.route('/forms/<int:form_id>', methods=["GET"])
def get_one_forms(form_id):
    if formExist(formsDB, form_id):
        form = formsDB.find_one({"_id":form_id})
        return form, 200
    return '', 409


@app_blueprint.route('/forms/edit', methods=["POST"])
def edit_form():
    requestData = request.get_json()
    form_id = requestData['_id']
    if not formExist(formsDB, form_id):
        return '', 409
    form = formsDB.delete_one({"_id":form_id})
    formsDB.insert_one(requestData)
    return '', 200


@app_blueprint.route('/forms/delete/<int:form_id>', methods=["POST"])
def delete_one(form_id):
    if formExist(formsDB, form_id):
        form = formsDB.delete_one({"_id":form_id})
        return '', 200
    return '', 409


