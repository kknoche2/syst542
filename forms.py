from wtforms import Form, BooleanField, StringField, IntegerField, validators

class PropertyForm(Form):
	price = IntegerField('Purchase Price')
	address = StringField('Address')
	zip = IntegerField('Zip')
	deposit = IntegerField('Deposit')
	depreciation = StringField('Depreciation')
	resale_value = IntegerField('Resale Value')
