import datetime
from bs4 import BeautifulSoup
from .base_article_parser import BaseArticleParser




class RTSFeedParser(BaseArticleParser):
    url = 'https://www.rts.rs'
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
        soup = BeautifulSoup(html, 'html.parser')

        # lookup article
        raw_story_date = soup.find('p', {"class", "storyDate"}).text.replace('&nbsp;', ' ').split(',')[1].strip().split('\xa0')
        day = int(raw_story_date[0].replace('.',''))
        month = RTSFeedParser.lookup_numeric_month[raw_story_date[1]]
        year = int(raw_story_date[2])

        # lookup all feed entries
        feed_entries = soup.find_all("div", {"class": "short-story-holder"})

        # process each entry
        for feed in feed_entries:
            sentences = []
            title = None
            hour = None
            minute = None
            # locate entry time
            feed_entry_time = feed.find('span', {"class": "short-story-date"})
            if feed_entry_time:
                feed_entry_time_elements = feed_entry_time.text.strip().split(':')
                hour = int(feed_entry_time_elements[0])
                minute = int(feed_entry_time_elements[1])
            # locate title
            feed_entry_title = feed.find('h4', {"class": "short-story-title"})
            if feed_entry_title:
                sentences.append(feed_entry_title.text)
            # locate body
            feed_entry_body = feed.find('div', {"class": "short-story-body"})
            if feed_entry_body:
                body_sentences = feed_entry_body.find_all('p')
                for body_sentence in body_sentences:
                    sentences.append(body_sentence.text)
            # process sentences
            for sentence in sentences:
                result = self.parse_sentence(sentence)
                self.validate_result(result)
                # include the news_date result
                result['news_datetime'] = datetime.datetime(year, month, day, hour, minute)
                result['date'] = datetime.datetime(year, month, day) - datetime.timedelta(days = 1)
                result['source'] = 'Serbian National TV'
                if result['valid']:
                    return result
        return {
            'valid': False,
            'news_datetime': datetime.datetime(year, month, day),
            'date': datetime.datetime(year, month, day) - datetime.timedelta(days = 1),
            'total_number_of_vaccinations': 0,
            'fully_vaccinated': 0,
            'source': 'Serbian National TV'
            }

    def validate_result(self, result):
        result['valid'] = result['total_number_of_vaccinations'] != None and result['fully_vaccinated'] != None
        #TODO: implement further validations
