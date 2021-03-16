import pytest
from cov19.vaccination.templates import TemplateFactory
from cov19.vaccination.templates.human_template import HumanTemplate

@pytest.fixture
def template_factory():
    return TemplateFactory()

class TestParserFactory(object):

    def test_create_parser(self, capsys, template_factory):
        with capsys.disabled():
            parser = template_factory.create_template('human')
            assert type(parser) == HumanTemplate
            with pytest.raises(LookupError) as e:
                parser = template_factory.create_template('')
            with pytest.raises(TypeError) as e:
                parser = template_factory.create_template(None)
