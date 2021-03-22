from cov19.vaccination.parsers import RTSFeedParser, GenericArticleParser

class ParserFactory(object):
    parsers = [
            RTSFeedParser,
            GenericArticleParser
        ]
    @staticmethod
    def create_parser(url):
        if not isinstance(url, str):
            raise(TypeError('Input parameter url is not str'))
        supported = []
        for parser in ParserFactory.parsers:
            parser_urls = parser.urls_bases
            for parser_url in parser_urls:
                supported.append(parser_url)
                if url.startswith(parser_url):
                    return parser()
        supported = '\n'.join(supported)
        raise LookupError(f"Unable to find the parser for url: '{url}'\nSupported are:\n{supported}")
