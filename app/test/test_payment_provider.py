import pytest
import requests
import json

from app.settings import FLASK_RUN_HOST, FLASK_RUN_PORT

url = "http://{}:{}".format(FLASK_RUN_HOST, FLASK_RUN_PORT)


def test_no_argument():
    response = requests.post("{}/payment".format(url), data={}, headers={"Content-Type": "application/json"})
    assert response.status_code == 400


def invalid_credit_card_number():

    card_data_1 = {"CreditCardNumber": "qwer123456ijiojw","CardHolder":"Sonu","SecurityCode": "111",
"ExpirationDate": "2020/1/1","Amount": 333.3}
    response_1 = requests.post("{}/payment".format(url), data=json.dumps(card_data_1), headers={"Content-Type":"application/json"})
    
    assert response_1.status_code == 400
    
    
def valid_data_test():
    card_data_1 = {"CreditCardNumber": "1234567890123456", "CardHolder": "Sonu", "SecurityCode": "111",
                   "ExpirationDate": "2022/11/12", "Amount": 19}
    card_data_2 = {"CreditCardNumber": "1234567890123456", "CardHolder": "Sonu", "SecurityCode": "111",
                   "ExpirationDate": "2022/11/12", "Amount": 333}
    card_data_3 = {"CreditCardNumber": "1234567890123456", "CardHolder": "Sonu", "SecurityCode": "111",
                   "ExpirationDate": "2022/11/12", "Amount": 666}
    
    response_1 = requests.post("{}/payment".format(url), data=json.dumps(card_data_1), headers={"Content-Type":"application/json"})
    response_2 = requests.post("{}/payment".format(url), data=json.dumps(card_data_2), headers={"Content-Type":"application/json"})
    response_3 = requests.post("{}/payment".format(url), data=json.dumps(card_data_3), headers={"Content-Type":"application/json"})
    
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 200


def test_expiry_card():
    card_data_1 = {"CreditCardNumber": "1234567890123456", "CardHolder": "Sonu", "SecurityCode": "111",
                   "ExpirationDate": "2022/1/1", "Amount": 333.3}
    card_data_2 = {"CreditCardNumber": "1234567890123456", "CardHolder": "Sonu", "SecurityCode": "111",
                   "ExpirationDate": "2019/1/1", "Amount": 333.3}
    

    response_1 = requests.post("{}/payment".format(url), data=json.dumps(card_data_1), headers={"Content-Type": "application/json"})
    response_2 = requests.post("{}/payment".format(url), data=json.dumps(card_data_2),
                               headers={"Content-Type": "application/json"})
    
    assert response_1.status_code == 200
    assert response_2.status_code == 400


def test_security_code():
    card_data_1 = {"CreditCardNumber": "1234567890123456", "CardHolder": "Sonu", "SecurityCode": "111",
                   "ExpirationDate": "2022/1/1", "Amount": 333.3}
    card_data_2 =  {"CreditCardNumber": "1234567890123456", "CardHolder": "prashant rana", "ExpirationDate": "2022/1/1", "Amount": 333.3}
    card_data_3 = {"CreditCardNumber": "1234567890123456", "CardHolder": "prashant rana", "SecurityCode": 444,
                   "ExpirationDate": "2022/1/1", "Amount": 333.3}

    response_1 = requests.post("{}/payment".format(url), data=json.dumps(card_data_1),
                               headers={"Content-Type": "application/json"})
    
    response_2 = requests.post("{}/payment".format(url), data=json.dumps(card_data_2),
                               headers={"Content-Type": "application/json"})
    response_3 = requests.post("{}/payment".format(url), data=json.dumps(card_data_3),
                               headers={"Content-Type": "application/json"})
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 400
