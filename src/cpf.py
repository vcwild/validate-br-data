from validators import CPFValidator

class Cpf:
	def __init__(self, document) -> None:
		self.value = None
		if isinstance(document, int):
			document = str(document)
		if self._is_valid_cpf(document):
			self.value = document
		else:
			raise ValueError("Invalid CPF")

	def __str__(self) -> str:
		return f'Cpf(value="{self.value}")'

	def _is_valid_cpf(self, document: str) -> bool:
		if len(document) == 11:
			document = self._format_cpf(document)
			self.mask = document
		return CPFValidator().validate(document)

	def _format_cpf(self, document) -> str:
		return f"{document[:3]}.{document[3:6]}.{document[6:9]}-{document[-2:]}"
