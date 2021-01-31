from flask import Blueprint, request, abort, jsonify
import json
from app.services.payment import Card, ExternalPayment

blueprint = Blueprint('views', __name__)


@blueprint.route('/payment', methods=['POST'])
def payment():
    if request.method == 'POST':
        data = request.get_data(as_text=True)
        
        if not data:
            return {"status_code": 400, "msg": "failed"}, 400
        
        request_data = json.loads(data)
        
        card_data = Card()
        print("request data {}".format(request_data))
        try:
            status, error = card_data.verify_card_input(**request_data)
            if error != '':
                print("card data invalid")
                return {"status_code": 400, "msg": error}, 400
        except:
            return {"status_code": 400, "msg": "failed"}, 400
        try:
            # started payment
            print("started payment")
            payment_status = ExternalPayment(card_data.Amount, card_data)
            print("payment process started... we can do validation and db update depends on use case.")
            
            payment_sccessfull = payment_status.make_payment()
            # checking the transaction status, if it is successful or not.
            print("payment_sccessfull", payment_sccessfull)
            if payment_sccessfull:
                return {"status_code": 200, "msg": "successful"}, 200
            else:
               return {"status_code": 400, "msg": "failed"}, 400
        except:
            return {"status_code": 500, "msg": "woops! something went wrong"}, 500
    else:
        return {"status_code": 400, "msg": "failed"}, 400
