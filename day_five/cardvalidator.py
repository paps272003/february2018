class CardValidator:
	
	def __init__(self,card_number):
		self.card_number = card_number
		self.validate()
		self.cardType()


	def validate(self):
		doubled = ""
		not_doubled = ""

		for index in range( len(self.card_number)-2, -1, -2 ):
			new_number = int( self.card_number[index] )*2
			doubled = doubled + str( new_number )

		for index in range( len(self.card_number)-1, -1, -2 ):
			not_doubled = not_doubled + self.card_number[index]

		total = 0

		for digit in doubled:
			total = total + int( digit )

		for digit in not_doubled:
			total = total + int( digit )

		if total % 10 == 0:
			self.valid = True
		else:
			self.valid = False

	def cardType(self):
		card_type_dict = {"VISA":["4"], "MASTERCARD":["51","52","53","54","55"],"AMEX":["34","37"],"DISCOVER":["6"]}

		for card_type in card_type_dict:
			for start_num in card_type_dict[card_type]:

				if start_num == self.card_number[0: len(start_num) ]:
					self.card_type = card_type

		if self.card_type in ["VISA", "MASTERCARD", "DISCOVER"]:
			if len(self.card_number) != 16:
				self.card_type = "INVALID"
		elif self.card_type in ["AMEX"]:
			if len(self.card_number) != 15:
				self.card_type = "INVALID"




my_card = CardValidator("4485040993287616")

print(my_card.valid)
print(my_card.card_type)