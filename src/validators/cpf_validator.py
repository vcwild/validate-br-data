from typing import List
from .abstract_classes import AbstractDocumentValidator


class CPFValidator(AbstractDocumentValidator):
	"""Class validator for Cadastro de Pessoas Físicas (CPF)."""

	def __init__(self, repeated_digits: bool = False):
		self.digits = list(range(10))
		self.repeated_digits = repeated_digits

	def validate(self, doc: str = '') -> bool:
		"""Validates a CPF."""
		if not self._validate_input(doc, ['.', '-']):
			return False

		doc = list(self._only_digits(doc))

		if len(doc) != 11:
			return False

		if not self.repeated_digits and self._check_repeated_digits(doc):
			return False

		return self._generate_first_digit(doc) == doc[9] \
				and self._generate_second_digit(doc) == doc[10]

	def _generate_first_digit(self, doc: list) -> str:
		"""Generates CPF first digit."""
		sum = 0

		for i in range(10, 1, -1):
			sum += int(doc[10 - i]) * i

		sum = (sum * 10) % 11

		if sum == 10:
			sum = 0

		return str(sum)

	def _generate_second_digit(self, doc: list) -> str:
		"""Generates CPF second digit."""
		sum = 0

		for i in range(11, 1, -1):
			sum += int(doc[11 - i]) * i

		sum = (sum * 10) % 11

		if sum == 10:
			sum = 0

		return str(sum)

	def _check_repeated_digits(self, doc: List[str]) -> bool:
		"""Verifies if a CPF has repeated numbers."""
		return len(set(doc)) == 1
