from src.objects import CPF, CNPJ
from src.document_factory import DocumentFactory
import pytest

# test

@pytest.fixture(scope='session')
def factory():
	return DocumentFactory()


def test_document_factory_should_spawn_instance_of_document_factory(factory):
	assert isinstance(factory, DocumentFactory)


def test_factory_create_cpf_document_should_create_cpf_document(factory):
	document = "01234567890"
	may_be_cpf = factory.create_document(document)

	assert	isinstance(may_be_cpf, CPF)


def test_factory_create_cnpj_document_should_create_cnpj_document(factory):
	document = "35379838000112"
	may_be_cnpj = factory.create_document(document)

	assert isinstance(may_be_cnpj, CNPJ)


def test_factory_create_batch_documents_should_create_batch_documents(factory):
	documents = ["01234567890", "35379838000112"]

	batch_documents = list(map(factory.create_document, documents))
	expected_response = [CPF(value="01234567890"), CNPJ(value="35379838000112")]

	assert repr(batch_documents) == repr(expected_response)
