import re
import datetime
from decimal import Decimal


def validate_card(card):
	if not re.search(r'^4[0-9]{12}(?:[0-9]{3})?$', card):
		return False
	return True


class BaseCardInfo:
	def __init__(self):
		self.CreditCardNumber = None
		self.CardHolder = None
		self.ExpirationDate = None
		self.SecurityCode = None
		self.Amount = None


class Card(BaseCardInfo):
	
	def __init__(self):
		super(Card, self).__init__()
	
	def verify_card_input(self, **kwargs):
		"""
		Requirement
		-CreditCardNumber(mandatory, string, it should be a valid credit card number)
		-CardHolder: (mandatory, string)
		-ExpirationDate (mandatory, DateTime, it cannot be in the past)
		-SecurityCode (optional, string, 3 digits)-Amount (mandatoy decimal, positive amount)
		"""
		cards_value = ["CreditCardNumber", "CardHolder", "ExpirationDate", "Amount"]
		if set(cards_value).intersection(kwargs.keys()) != set(cards_value):
			print("card details not exists")
			return False,"card details not exists"
		
		if validate_card(kwargs['CreditCardNumber']) == False and len(kwargs['CreditCardNumber']) != 16:
			print("invalid credit card number")
			return False, "invalid credit card number"
		
		if kwargs.get('SecurityCode',None) :
			if len(kwargs.get('SecurityCode', None)) == 3 and not kwargs.get('SecurityCode', None).isdigit():
				print("security code error")
				return False, "security code error"

		if not datetime.datetime.strptime(kwargs['ExpirationDate'], "%Y/%m/%d") > datetime.datetime.now():
			print("date time error")
			return False, "date time error format must be in %Y/%m/%d"
		
		try:
			if not Decimal(kwargs['Amount']) > 0:
				print("amount is invalid")
				return False, "amount is invalid"
		except:
			return False, "amount is invalid"
		

		self.CreditCardNumber = kwargs.get('CreditCardNumber', None)
		self.Amount = kwargs.get('Amount', None)
		self.CardHolder = kwargs.get('CardHolder', None)
		self.ExpirationDate = kwargs.get('ExpirationDate', None)
		
		if kwargs.get("SecurityCode", None):
			self.SecurityCode = kwargs.get('SecurityCode', None)

		return True, ""
	