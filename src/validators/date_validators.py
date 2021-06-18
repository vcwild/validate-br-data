from src.validators.abstract_classes import AbstractDocumentValidator
from datetime import datetime

class DateMonthYearHourMinutesValidator(AbstractDocumentValidator):
	def validate(self, value):
		try:
			datetime.strptime(value, "%d/%m/%Y %H:%M")
			return True
		except ValueError:
			...
		return False
