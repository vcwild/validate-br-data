import re

class PhoneNumberValidator:
	def __init__(self) -> None:
		...

	def validate(self, phone):
		pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
		matched = re.search(pattern, phone)
		if matched and len(phone) < 15:
			return True
		return False
