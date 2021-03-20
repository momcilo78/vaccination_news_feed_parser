import pytest
import os
import datetime
import requests

from cov19.vaccination.parsers import RTSFeedParser
from _pytest.hookspec import pytest_fixture_post_finalizer


@pytest.fixture
def parser():
    return RTSFeedParser()


# @pytest.fixture
# def html_pages():
#     base_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'html', 'rts')
#     html_files = [current for current in os.listdir(base_path) if (current.endswith('.html') or current.endswith('.htm'))]
#     collection = []
#     for current in html_files:
#         with open(os.path.join(base_path, current)) as res_file:
#             elements = os.path.splitext(current)[0].split('_')
#             entry_date = elements[1]
#             year = int(entry_date[0:4])
#             month = int(entry_date[5:6])
#             day = int(entry_date[6:8])
#             entry_time = elements[2]
#             hour = int(entry_time[0:2])
#             minute = int(entry_time[2:4])
#             feed_entry_total_vaccinations = int(elements[3])
#             feed_entry_total_full_vaccinated = int(elements[4])
#             html_page = res_file.read()
#             collection.append(
#                 {
#                     'file': current,
#                     'html': html_page,
#                     'news_datetime': datetime.datetime(year, month, day, hour, minute),
#                     'total_number_of_vaccinations': feed_entry_total_vaccinations,
#                     'fully_vaccinated': feed_entry_total_full_vaccinated
#                 }
#             )
#     return collection

@pytest.fixture
def html_pages():
    test_pages = [
        {
            'url': 'https://www.rts.rs/page/stories/sr/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81/story/3134/koronavirus-u-srbiji/4300365/koronavirus-srbija-broj-zarazenih-preminulih-vakcinacija-mere.html',
            'total_number_of_vaccinations': 2112074,
            'fully_vaccinated': 826851,
            'news_datetime': datetime.datetime(2021,3,19,8,22)
        },
    ]
    for page in test_pages:
        r = requests.get(page['url'])
        if r.status_code != 200:
            raise Exception(f"Unable to retrieve URL: {url}")
        page['html'] = r.text
    return test_pages


class TestRTSFeerParser(object):
    def test_parse_html(self, capsys, parser, html_pages):
        with capsys.disabled():
            print("")
            for html_page in html_pages:
                print(f"Parsing: {html_page['url']}")
                result = parser.parse_html(html_page['html'])
                # print(result)
                assert result != None
                assert result['news_datetime'] == html_page['news_datetime']
                assert result['total_number_of_vaccinations'] == html_page['total_number_of_vaccinations']
                assert result['fully_vaccinated'] == html_page['fully_vaccinated']
