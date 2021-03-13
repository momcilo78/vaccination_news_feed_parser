from cov19.vaccination.parsers import RTSFeedParser

class ParserFactory(object):
    parsers = [
            RTSFeedParser
        ]
    @staticmethod
    def create_parser(url):        
        for parser in ParserFactory.parsers:
            parser_url = parser.url
            if url.startswith(parser_url):
                return parser()
        raise Exception(f'Unable to find the parser for url: {url}')