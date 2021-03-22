import datetime
from bs4 import BeautifulSoup
from .base_article_parser import BaseArticleParser


class GenericArticleParser(BaseArticleParser):
    urls_bases = [
        'http://',
        'https://'
    ]
    lookup_numeric_month = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'maj': 5,
        'jun': 6,
        'jul': 7,
        'avg': 8,
        'sep': 9,
        'okt': 10,
        'nov': 11,
        'dec': 12
    }

    def parse_html(self, html):
        parsed_article_time = None
        soup = BeautifulSoup(html, 'html.parser')
        article_times = soup.find_all('time')
        if article_times:
            for article_time in article_times:
                parsed_article_time = self.parse_date(article_time.text)
        paragraphs = soup.find_all(['p', 'h', 'div', 'span'])
        paragraphs = soup.find_all(['p'])
        # set default result
        result = {
            'valid': False,
            'news_datetime': parsed_article_time,
            'date': parsed_article_time - datetime.timedelta(days = 1),
            'total_number_of_vaccinations': 0,
            'fully_vaccinated': 0,
            'source': 'Uknown'
        }

        sentences = []
        for paragraph in paragraphs:
            paragraph_text = paragraph.text.strip()
            paragraph_sentences = paragraph_text.split('. ')
            for sentence in paragraph_sentences:
                sentences.append(sentence.replace('\xa0', ' '))
        self.parse_text(sentences, result)
        self.validate_result(result)
        print(result)
        return result
            # if len(p_text) > 1:
            #     print(p_text)
    def validate_result(self, result):
        result['valid'] = result['total_number_of_vaccinations'] != None and result['fully_vaccinated'] != None
        #TODO: implement further validations
