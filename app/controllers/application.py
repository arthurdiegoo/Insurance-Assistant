from flask import request, jsonify
from app.scripts import evaluateRisk


def post_application(db):
    try:
        _json = request.json
        final_risk = evaluateRisk(_json)
        _age = _json['age']
        _dependents = _json['dependents']
        _house = _json['house']
        _income = _json['income']
        _marital_status = _json['marital_status']
        _risk_questions = _json['risk_questions']
        _vehicle = _json['vehicle']
        # Check for fields and method
        if request.method == 'POST':
            # Insert data to database
            application = db.users.insert({
                "application": {
                    "age": _age,
                    "dependents": _dependents,
                    "house": _house,
                    "income": _income,
                    "marital_status": _marital_status,
                    "risk_questions": _risk_questions,
                    "vehicle": _vehicle
                },
                "risk": final_risk
            })
            # Response ->
            return jsonify(final_risk)
        else:
            print('reached else')
            raise Exception('Bad Request')
    except Exception as e:
        response = jsonify(
            'Bad Request, All Fields are required')
        response.status_code = 400
        print(e)
        return response
