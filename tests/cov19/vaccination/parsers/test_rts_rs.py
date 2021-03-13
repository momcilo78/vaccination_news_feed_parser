import pytest
import os
import datetime

from cov19.vaccination.parsers import RTSFeedParser


@pytest.fixture
def parser():
    return RTSFeedParser()


@pytest.fixture
def html_pages():
    base_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'html', 'rts')
    html_files = [current for current in os.listdir(base_path) if (current.endswith('.html') or current.endswith('.htm'))]
    collection = []
    for current in html_files:
        with open(os.path.join(base_path, current)) as res_file:
            elements = os.path.splitext(current)[0].split('_')
            entry_date = elements[1]
            year = int(entry_date[0:4])
            month = int(entry_date[5:6])
            day = int(entry_date[6:8])
            entry_time = elements[2]
            hour = int(entry_time[0:2])
            minute = int(entry_time[2:4])
            feed_entry_total_vaccinations = int(elements[3])
            feed_entry_total_full_vaccinated = int(elements[4])
            html_page = res_file.read()
            collection.append(
                {
                    'file': current,
                    'html': html_page,
                    'news_datetime': datetime.datetime(year, month, day, hour, minute),
                    'total_number_of_vaccinations': feed_entry_total_vaccinations,
                    'fully_vaccinated': feed_entry_total_full_vaccinated
                }
            )
    return collection


class TestRTSFeerParser(object):
    def test_parse_html(self, capsys, parser, html_pages):
        with capsys.disabled():
            print("")
            for html_page in html_pages:
                print(f"Parsing: {html_page['file']}")
                # print(f"{html_page['html']}")
                result = parser.parse_html(html_page['html'])
                print(result)
                assert result != None
                assert result['news_datetime'] == html_page['news_datetime']
                assert result['total_number_of_vaccinations'] == html_page['total_number_of_vaccinations']
                assert result['fully_vaccinated'] == html_page['fully_vaccinated']
