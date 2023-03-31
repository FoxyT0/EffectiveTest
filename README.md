# EffectiveTest

## Get starting

First, install all dependencies from the requirements.txt with the command install -r requirements.txt'.
Next step, write python manage.py into CLI being in project folder.

## Main endpoints

1. GET '/' – home endpoint to make sure the app is running.
2. GET '/forms' – endpoint for view all forms available in the database.
3. GET '/forms/<int:form_id>' – endpoint for view form with specific form_id.
4. POST '/form/create' – endpoint for adding new forms.

## View of forms data

Forms are JSON-like.
Example:

```json
{
"_id": "222",
"1":{
"type":"text",
"question":"Whats up?",
"answer":"All is good!"
}
"2":{
"type":"radio",
"question":"How are you?",
"answer":{
"1":"OK",
"2":"So-so",
"3":"Bad :("
}
}
}
```

Here \_id is id of form. 1 and 2 is number of questions. Type is the answer type(text/radio/check_box). Field answer can be string or JSON-like
when type of answer is not text.
