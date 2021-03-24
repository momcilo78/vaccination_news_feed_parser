import pytest
import datetime
import requests
from cov19.vaccination.parsers import GenericArticleParser

@pytest.fixture
def parser():
    return GenericArticleParser()


@pytest.fixture
def html_pages():
    test_pages = [
        {
            'url': 'https://www.rts.rs/page/stories/sr/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81/story/3134/koronavirus-u-srbiji/4289883/korona-srbija-podaci-zarazeni.html',
            'total_number_of_vaccinations': 1827340,
            'fully_vaccinated': 666146,
            'news_datetime': datetime.datetime(2021,3,11,15,0)
        },
        {
            'url': 'https://www.b92.net/info/vesti/index.php?yyyy=2021&mm=03&dd=17&nav_category=12&nav_id=1828095',
            'total_number_of_vaccinations': 2052402,
            'fully_vaccinated': 793926,
            'news_datetime': datetime.datetime(2021,3,17,8,15)
        },
        {
            'url': 'https://www.b92.net/info/vesti/index.php?yyyy=2021&mm=03&dd=24&nav_category=12&nav_id=1831791',
            'total_number_of_vaccinations': 2206821,
            'fully_vaccinated': 876436,
            'news_datetime': datetime.datetime(2021,3,24,7,20)
        },
        {
            'url': 'https://www.b92.net/info/vesti/index.php?yyyy=2021&mm=02&dd=23&nav_category=12&nav_id=1816193',
            'total_number_of_vaccinations': 1263111,
            'fully_vaccinated': 451658,
            'news_datetime': datetime.datetime(2021,2,23,7,3)
        },
        # {
        #     'url': 'https://www.rts.rs/page/stories/sr/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81/story/3134/koronavirus-u-srbiji/4297614/koronavirus-srbija-podaci-17.-mart.html',
        #     'total_number_of_vaccinations': 2077197,
        #     'fully_vaccinated': 809375,
        #     'news_datetime': datetime.datetime(2021,3,17,19,17)
        # },
        # {
        #     'url': 'https://www.rts.rs/page/stories/sr/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81/story/3134/koronavirus-u-srbiji/4300365/koronavirus-srbija-broj-zarazenih-preminulih-vakcinacija-mere.html',
        #     'total_number_of_vaccinations': 2112074,
        #     'fully_vaccinated': 826851,
        #     'news_datetime': datetime.datetime(2021,3,19,8,22)
        # },
        # {
        #     'url': 'https://www.rts.rs/page/stories/sr/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81/story/3134/koronavirus-u-srbiji/4301815/koronavirus-srbija-zarazeni-podaci.html',
        #     'total_number_of_vaccinations': 2161595,
        #     'fully_vaccinated': 857934,
        #     'news_datetime': datetime.datetime(2021,3,20,15,7)
        # },
        # {
        #     'url': 'https://www.rts.rs/page/stories/sr/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81/story/3134/koronavirus-u-srbiji/4302356/koronavirus-kovid-19-vakcine-srbija-epidemija.html',
        #     'total_number_of_vaccinations': 2163593,
        #     'fully_vaccinated': 858461,
        #     'news_datetime': datetime.datetime(2021,3,21,6,35)
        # },
        # {
        #     'url': 'https://www.rts.rs/page/stories/sr/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81/story/3134/koronavirus-u-srbiji/4295816/koronavirus-kovid-19-vakcine-srbija-epidemija.html',
        #     'total_number_of_vaccinations': 2040313,
        #     'fully_vaccinated': 791269,
        #     'news_datetime': datetime.datetime(2021,3,16,8,50)
        # },
#         {
#             'url': '',
#             'total_number_of_vaccinations': 0,
#             'fully_vaccinated': 0,
#             'news_datetime': datetime.datetime(2021,3,0,0,0)
#         },
    ]
    for page in test_pages:
        r = requests.get(page['url'])
        if r.status_code != 200:
            raise Exception(f"Unable to retrieve URL: {page['url']}")
        page['html'] = r.text
    return test_pages

class TestGenericArticleParser(object):
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
