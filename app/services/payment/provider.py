from app.services.payment import Card


class BasePaymentProvider:
	def __init__(self, repeat=0):
		self.repeat = repeat
		self.gateway = None
		
	def __repr__(self):
		return "<{}>".format("BasePaymentProvider")
	
	def connect(self, gateway=None, details=None):
		if gateway != None:
			if self.authenticate(details):
				return True
		return False
	
	def authenticate(self, details=None):
		if details != None:
			return True
		return False
	
	def pay(self, amount, user_details=None, gateway=None):
		if gateway is None:
			gateway = self.gateway
		print('gateway', gateway)
		while self.repeat + 1 > 0:
			if self.connect(gateway, user_details):
				print("payment of {} in gateway {} sucessful".format(amount, self.gateway))
				return True
			self.repeat -= 1
		return False


class PremiumBasePaymentProvider(BasePaymentProvider):
	def __init__(self, repeat=3):
		super(PremiumBasePaymentProvider, self).__init__(repeat)
		self.gateway = "PremiumBasePaymentProvider"
	
	def __repr__(self):
		return "<PremiumBasePaymentGateway>"


class ExpensiveBasePaymentProvider(BasePaymentProvider):
	def __init__(self, repeat=1):
		super(ExpensiveBasePaymentProvider, self).__init__(repeat)
		self.gateway = "ExpensiveBasePaymentProvider"
	
	def __repr__(self):
		return "<ExpensiveBasePaymentProvider>"


class CheapBasePaymentProvider(BasePaymentProvider):
	def __init__(self, repeat=0):
		super(CheapBasePaymentProvider, self).__init__(repeat)
		self.gateway = "CheapBasePaymentProvider"
	
	def __repr__(self):
		return "<CheapBasePaymentProvider>"


class ExternalPayment:
	def __init__(self, amount, card_details=None):
		self.amount = amount
		self.card_details = card_details
	
	def make_payment(self):
		try:
			payment_mode = None
			if self.amount <= 20:
				payment_mode = CheapBasePaymentProvider()
			elif 20 < self.amount < 500:
				payment_mode = ExpensiveBasePaymentProvider()
			elif self.amount >= 500:
				payment_mode = PremiumBasePaymentProvider()
			else:
				return False
			print('payment_mode', payment_mode)
			status = payment_mode.pay(self.amount, self.card_details)
			return status
		except:
			return False

