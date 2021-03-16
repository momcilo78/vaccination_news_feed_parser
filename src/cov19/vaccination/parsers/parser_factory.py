from cov19.vaccination.parsers import RTSFeedParser

class ParserFactory(object):
    parsers = [
            RTSFeedParser
        ]
    @staticmethod
    def create_parser(url):
        if not isinstance(url, str):
            raise(TypeError('Input parameter url is not str')) 
        for parser in ParserFactory.parsers:
            parser_url = parser.url
            if url.startswith(parser_url):
                return parser()
        raise LookupError(f"Unable to find the parser for url: '{url}'")
