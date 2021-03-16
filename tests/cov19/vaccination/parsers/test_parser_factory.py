import pytest
from cov19.vaccination.parsers import ParserFactory
from cov19.vaccination.parsers.rts_rs import RTSFeedParser

@pytest.fixture
def parser_factory():
    return ParserFactory()

class TestParserFactory(object):
    
    def test_create_parser(self, capsys, parser_factory):
        with capsys.disabled():        
            parser = parser_factory.create_parser('https://www.rts.rs/some')
            assert type(parser) == RTSFeedParser
            with pytest.raises(LookupError) as e:
                parser = parser_factory.create_parser('')
            with pytest.raises(TypeError) as e:
                parser = parser_factory.create_parser(None)
