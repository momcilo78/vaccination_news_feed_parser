import datetime
from bs4 import BeautifulSoup
from .base_article_parser import BaseArticleParser


class GenericArticleParser(BaseArticleParser):
    urls_bases = [
        'http://',
        'https://'
    ]

    def parse_html(self, html):
        parsed_article_date = None
        soup = BeautifulSoup(html, 'html.parser')
        article_times = soup.find_all('time')
        parsed_article_datetime = None
        if article_times:
            for article_time in article_times:
                parsed_article_date = self.parse_date(article_time.text)
                parsed_article_time = self.parse_time(article_time.text)
                # if parsed stop processing
                if parsed_article_date and parsed_article_time:
                    parsed_article_datetime = parsed_article_date + parsed_article_time
                    break
        paragraphs = soup.find_all(['p', 'h', 'div', 'span'])
        # if the date was not found before with time, try with other elements
        if not parsed_article_date:
            for paragraph in paragraphs:
                parsed_article_date = self.parse_date(paragraph.text)
                parsed_article_time = self.parse_time(paragraph.text)
                if parsed_article_date and parsed_article_time:
                    parsed_article_datetime = parsed_article_date + parsed_article_time
                    break

        # paragraphs = soup.find_all(['p'])
        # set default result
        result = {
            'valid': False,
            'news_datetime': parsed_article_datetime,
            'date': parsed_article_datetime - datetime.timedelta(days = 1),
            'total_number_of_vaccinations': 0,
            'fully_vaccinated': 0,
            'source': 'Unknown'
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
