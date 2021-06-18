from validators import CPFValidator
from validators.CNPJValidator import CNPJValidator
from .base_object import BaseObject


class Cpf(BaseObject):
	def _is_valid_instance(self, value: str) -> bool:
		if len(value) == 11:
			value = self._format_type(value)
		return CPFValidator().validate(value)

	def _format_type(self, v) -> str:
		return f"{v[:3]}.{v[3:6]}.{v[6:9]}-{v[-2:]}"


class Cnpj(BaseObject):
	def _is_valid_instance(self, value: str) -> bool:
		if len(value) == 14:
			value = self._format_type(value)
		return CNPJValidator().validate(value)

	def _format_type(self, v) -> str:
		return f"{v[:2]}.{v[2:5]}.{v[5:8]}/{v[8:12]}-{v[-2:]}"
