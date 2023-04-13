def formExist(formsDB, form_id):
    if (formsDB.find_one({"_id":form_id})) == None:
        return False
    return True

