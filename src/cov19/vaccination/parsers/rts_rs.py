import datetime
from bs4 import BeautifulSoup
from .base_article_parser import BaseArticleParser




class RTSFeedParser(BaseArticleParser):
    urls_bases = [
        'https://www.rts.rs'
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
        soup = BeautifulSoup(html, 'html.parser')

        # lookup article
        raw_story_date = soup.find('p', {"class", "storyDate"}).text.replace('&nbsp;', ' ').split(',')[1].strip().split('\xa0')
        day = int(raw_story_date[0].replace('.',''))
        month = RTSFeedParser.lookup_numeric_month[raw_story_date[1]]
        year = int(raw_story_date[2])
        main_lead = None
        
        # set default result
        result = {
            'valid': False,
            'news_datetime': None,
            'date': datetime.datetime(year, month, day) - datetime.timedelta(days = 1),
            'total_number_of_vaccinations': 0,
            'fully_vaccinated': 0,
            'source': 'Serbian National TV'
        }
        
        # locate main lead, it should be used in worse case, since this lead can change during the day!
        article_main_lead = soup.find('p', {"class": "storyMainLead"})
        if article_main_lead:
            main_lead = article_main_lead.text
        
        # lookup all feed entries
        feed_entries = soup.find_all("div", {"class": "short-story-holder"})        
        # process each entry
        for feed in feed_entries:
            sentences = []
            news_datetime = None
            # locate entry time
            feed_entry_date_time = feed.find_all('span', {"class": "short-story-date"})
            if feed_entry_date_time:
                if len(feed_entry_date_time) == 2:
                    # date time entry cntains both date and time
                    date_text = feed_entry_date_time[0].text.strip()
                    time_text = feed_entry_date_time[1].text.strip()
                    news_datetime = datetime.datetime.strptime(f'{date_text} {time_text}', '%d. %m. %Y. %H:%M')
                else:
                    # date time entry contains only time, date has to be inherited from page itself
                    feed_entry_time_elements = feed_entry_date_time[0].text.strip().split(':')
                    hour = int(feed_entry_time_elements[0])
                    minute = int(feed_entry_time_elements[1])
                    news_datetime = datetime.datetime(year, month, day, hour, minute)
            # locate title
            feed_entry_title = feed.find('h4', {"class": "short-story-title"})
            if feed_entry_title:
                sentences.append(feed_entry_title.text)
            # locate body
            feed_entry_body = feed.find('div', {"class": "short-story-body"})
            if feed_entry_body:
                body_paragraphs = feed_entry_body.find_all('p')
                for body_paragraph in body_paragraphs:
                    paragraph_sentences = body_paragraph.text.split('. ')
                    for sentence in paragraph_sentences:
                        sentences.append(sentence.replace('\xa0', ' '))
            # main lead is added to the end
            if main_lead:
                sentences.append(main_lead)
            self.parse_text(sentences, result)
            self.validate_result(result)
            result['news_datetime'] = news_datetime
            result['date'] = datetime.datetime(year, month, day) - datetime.timedelta(days = 1)
            result['source'] = 'Serbian National TV'
            if result['valid']:
                return result

        return result

    def validate_result(self, result):
        result['valid'] = result['total_number_of_vaccinations'] != None and result['fully_vaccinated'] != None
        #TODO: implement further validations
