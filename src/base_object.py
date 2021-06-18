from abc import ABC, abstractclassmethod


class BaseObject(ABC):
	def __init__(self, value) -> None:
		self._value = None
		if not isinstance(value, str):
			try:
				value = str(value)
			except Exception:
				raise ValueError(f"Invalid `value` provided")
		if self._is_valid_instance(value):
			self._value = value
		else:
			raise ValueError(f"Invalid {self.__class__.__name__} provided")

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value: str):
		if self._is_valid_instance(value):
			self._value = value
		else:
			raise ValueError(f"Invalid {self.__class__.__name__}")

	def mask(self):
		return self._format_type(self._value)

	def __repr__(self) -> str:
		return f'{self.__class__.__name__}(value="{self._value}")'

	@abstractclassmethod
	def _is_valid_instance(self, value: str) -> bool:
		...

	@abstractclassmethod
	def _format_type(self, v) -> str:
		...
