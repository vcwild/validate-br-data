from datetime import datetime
import re
from .base_object import BaseObject
from src.validators import (
	CPFValidator,
	CNPJValidator,
	PhoneNumberValidator,
	DateMonthYearHourMinutesValidator
)

class CPF(BaseObject):
	def _is_valid_instance(self, value: str) -> bool:
		if len(value) == 11:
			value = self._format_type(value)
		return CPFValidator().validate(value)

	def _format_type(self, v) -> str:
		return f"{v[:3]}.{v[3:6]}.{v[6:9]}-{v[-2:]}"


class CNPJ(BaseObject):
	def _is_valid_instance(self, value: str) -> bool:
		if len(value) == 14:
			value = self._format_type(value)
		return CNPJValidator().validate(value)

	def _format_type(self, v) -> str:
		return f"{v[:2]}.{v[2:5]}.{v[5:8]}/{v[8:12]}-{v[-2:]}"


class PhoneNumber(BaseObject):
	def _is_valid_instance(self, value: str) -> bool:
		return PhoneNumberValidator().validate(value)

	def _format_type(self, v) -> str:
		pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
		m = re.search(pattern, v)

		if m.group(1):
			return "+{}({}){}-{}".format(
				m.group(1), m.group(2), m.group(3), m.group(4)
			)
		return "({}){}-{}".format(m.group(2), m.group(3), m.group(4))

class Date(BaseObject):
	def __init__(self, value) -> None:
		super().__init__(value)
		self._value = datetime.strptime(value, "%d/%m/%Y %H:%M")
		self.day = self._value.day
		self.month = self._value.month
		self.year = self._value.year
		self.weekday = self._value.weekday()
		self.hour = self._value.hour
		self.minute = self._value.minute

	@property
	def mes(self):
		month_list = ['janeiro', 'fevereiro', 'março','abril', 'maio', 'junho',
					  'julho','agosto', 'setembro', 'outubro','novembro', 'dezembro']
		return month_list[self.month - 1]

	@property
	def dia_da_semana(self):
		weekday_list = ['segunda', 'terça', 'quarta', 'quinta',
						'sexta', 'sábado', 'domingo']
		return weekday_list[self.weekday]

	def mask(self, long=False):
		if long:
			message = '{}, {} de {} de {} às {}:{}'
			return message.format(self.dia_da_semana.capitalize(), self.day, self.mes,
								  self.year, self.hour, self.minute)
		return self._format_type(self._value)

	def _is_valid_instance(self, value: str) -> bool:
		return DateMonthYearHourMinutesValidator.validate(value)

	def _format_type(self, v) -> str:
		return v.strftime("%d/%m/%Y %H:%M")
