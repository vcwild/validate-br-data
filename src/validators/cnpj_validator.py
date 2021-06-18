from .abstract_classes import AbstractDocumentValidator
from typing import Union


class CNPJValidator(AbstractDocumentValidator):
	"""Validator for Cadastro Nacional da Pessoa Jurídica (CNPJ)."""

	def __init__(self):
		self.digits = list(range(10))
		self.weights_first = list(range(5, 1, -1)) + list(range(9, 1, -1))
		self.weights_second = list(range(6, 1, -1)) + list(range(9, 1, -1))

	def validate(self, doc: str = '') -> bool:
		"""Validates CNPJ."""
		if not self._validate_input(doc, ['.', '/', '-']):
			return False

		doc = self._only_digits(doc)

		if len(doc) != 14:
			return False

		for i in range(10):
			if doc.count("{}".format(i)) == 14:
				return False

		return self._generate_first_digit(doc) == doc[12]\
				and self._generate_second_digit(doc) == doc[13]

	def mask(self, doc: str = '') -> str:
		"""Applies a CNPJ mask."""
		return "{}.{}.{}/{}-{}".format(doc[:2], doc[2:5], doc[5:8], doc[8:12], doc[-2:])

	def _generate_first_digit(self, doc: Union[str, list]) -> str:
		"""Generates first digit for CNPJ."""
		sum = 0

		for i in range(12):
			sum += int(doc[i]) * self.weights_first[i]

		sum = sum % 11

		if sum < 2:
			sum = 0
		else:
			sum = 11 - sum

		return str(sum)

	def _generate_second_digit(self, doc: Union[str, list]) -> str:
		"""Generates second digit for CNPJ."""
		sum = 0

		for i in range(13):
			sum += int(doc[i]) * self.weights_second[i]

		sum = sum % 11

		if sum < 2:
			sum = 0
		else:
			sum = 11 - sum

		return str(sum)
