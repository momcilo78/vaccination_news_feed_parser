import pytest
import datetime
from cov19.vaccination.parsers import BaseArticleParser

@pytest.fixture
def parser():
    return BaseArticleParser()

@pytest.fixture
def news():
    return [
        {
            'text': ['U Srbiji je, prema najnovijim podacima Vlade, izvršeno 1.263.111 vakcinacija protiv koronavirusa, a 451.658 građana dobilo je drugu vakcinu.'],
            'total_number_of_vaccinations': 1263111,
            'fully_vaccinated': 451658
        },
        {
            'text': ['U Srbiji je, prema najnovijim podacima Vlade, izvršeno 1.300.330 vakcinacija protiv kovida, a obe doze vakcine primilo je 472.769 građana.'],
            'total_number_of_vaccinations': 1300330,
            'fully_vaccinated': 472769
        },
        {
            'text': ['U Srbiji je, prema najnovijim podacima Vlade, izvršeno 1.343.718 vakcinacija protiv koronavirusa, a obe doze vakcine primilo je 487.359 građana.'],
            'total_number_of_vaccinations': 1343718,
            'fully_vaccinated': 487359
        },
        {
            'text': ['U Srbiji su, prema najnovijim podacima Vlade, izvršene 1.375.872 vakcinacije protiv koronavirusa, a obe doze vakcine primilo je 497.729 građana.'],
            'total_number_of_vaccinations': 1375872,
            'fully_vaccinated': 497729
        },
        {
            'text': ['U Srbiji su, prema najnovijim podacima Vlade, izvršene 1.405.142 vakcinacije protiv kovida, a obe doze vakcine primilo je 507.425 građana.'],
            'total_number_of_vaccinations': 1405142,
            'fully_vaccinated': 507425
        },
        {
            'text': ['U Srbiji su, prema najnovijim podacima Vlade, izvršene 1.433.055 vakcinacije protiv koronavirusa, a obe doze vakcine primilo je 511.807 građana.'],
            'total_number_of_vaccinations': 1433055,
            'fully_vaccinated': 511807
        },
        {
            'text': ['U Srbiji su, prema najnovijim podacima Vlade, izvršene 1.436.682 vakcinacije protiv koronavirusa, a obe doze vakcine primilo je 511.999 građana.'],
            'total_number_of_vaccinations': 1436682,
            'fully_vaccinated': 511999
        },
        {
            'text': ['U Srbiji je do sada, prema najnovijim podacima, obavljeno 1.470.406 vakcinacija, od čega je 524.231 građana primilo i drugu dozu vakcine.'],
            'total_number_of_vaccinations': 1470406,
            'fully_vaccinated': 524231
        },
        {
            'text': ['U Srbiji je, prema najnovijim podacima Vlade, obavljeno ukupno 1.501.917 vakcinacija. Od tog broja, dato je 530.863 druge doze vakcine.'],
            'total_number_of_vaccinations': 1501917,
            'fully_vaccinated': 530863
        },
        {
            'text': ['U Srbiji su, prema najnovijim podacima Vlade, izvršene 1.535.274 vakcinacije protiv koronavirusa, a obe doze vakcine primio je 534.751 građanin.'],
            'total_number_of_vaccinations': 1535274,
            'fully_vaccinated': 534751
        },
        {
            'text': ['U Srbiji su, prema najnovijim podacima Vlade, izvršene 1.576.983 vakcinacije protiv koronavirusa, a obe doze vakcine primila su 563.922 građanina.'],
            'total_number_of_vaccinations': 1576983,
            'fully_vaccinated': 563922
        },
        {
            'text': ['U Srbiji su, prema najnovijim podacima Vlade, izvršene 1.618.754 vakcinacije protiv koronavirusa, a obe doze vakcine primilo je 593.617 građana.'],
            'total_number_of_vaccinations': 1618754,
            'fully_vaccinated': 593617
        },
        {
            'text': ['U Srbiji su, prema najnovijim podacima Vlade, izvršene 1.650.030 vakcinacije protiv koronavirusa, a obe doze vakcine primilo je 620.067 građana.'],
            'total_number_of_vaccinations': 1650030,
            'fully_vaccinated': 620067
        },
        {
            'text': ['U Srbiji su, prema najnovijim podacima Vlade, izvršene 1.651.293 vakcinacije protiv koronavirusa, a obe doze vakcine primilo je 620.853 građana.'],
            'total_number_of_vaccinations': 1651293,
            'fully_vaccinated': 620853
        },
        {
            'text': ['Prema najnovijim podacima, u Srbiji je obavljeno ukupno 1.704.790 vakcinacija, a drugi dozu vakcine primilo je 623.424 građana.'],
            'total_number_of_vaccinations': 1704790,
            'fully_vaccinated': 623424
        },
        {
            'text': ['Prema najnovijim podacima, u Srbiji je obavljeno 1.750.533 vakcinacija, a drugu dozu je primilo 625.707 građana.'],
            'total_number_of_vaccinations': 1750533,
            'fully_vaccinated': 625707
        },
        {
            'text': ['U Srbiji je do sada obavljeno 1.792.912 vakcinacija, a 647.019 osoba dobilo je i drugu dozu vačine, pokazuju najnoviji podaci Vlade Srbije.'],
            'total_number_of_vaccinations': 1792912,
            'fully_vaccinated': 647019
        },
        {
            'text': ["Ukupno vakcinacija: 1.827.340, drugu dozu primilo je 666.146 ljudi."],
            'total_number_of_vaccinations': 1827340,
            'fully_vaccinated': 666146
        },
        {
            'text': ["U Srbiji je do sada dato 1.897.335 doza vakcina protiv korona virusa, a 701.100 osoba primilo je i drugu dozu, pokazuju najnoviji podaci Vlade Srbije."],
            'total_number_of_vaccinations': 1897335,
            'fully_vaccinated': 701100
        },
        {
            'text': ["U Srbiji je do sada dato 1.957.065 doza vakcina protiv koronavirusa, a 738.756 osoba primilo je i drugu dozu, pokazuju najnoviji podaci Vlade Srbije."],
            'total_number_of_vaccinations': 1957065,
            'fully_vaccinated': 738756
        },
        {
            'text': ["Prema poslednjim podacima, u Srbiji je obavljeno ukupno 2.112.074 vakcinacija.", "Drugu dozu primio je 826.851 građanin naše zemlje."],
            'total_number_of_vaccinations': 2112074,
            'fully_vaccinated': 826851
        },
    ]

class TestBaseArticleParser(object):
    def test_parse_text(self, capsys, parser, news):
        for current_news in news:
            result = {}
            parser.parse_text(current_news['text'], result)
            assert result['total_number_of_vaccinations'] == current_news['total_number_of_vaccinations']
            assert result['fully_vaccinated'] == current_news['fully_vaccinated']

    def test_parse_date(self, capsys, parser):
        with capsys.disabled():
            text = '22.03.2021'
            parsed_date = parser.parse_date(text)
            assert parsed_date == datetime.datetime(2021,3,22)
            text = '22.03.2021.'
            parsed_date = parser.parse_date(text)
            assert parsed_date == datetime.datetime(2021,3,22)
            text = '22.03.21'
            parsed_date = parser.parse_date(text)
            assert parsed_date == datetime.datetime(2021,3,22)
            text = '22/03/2021'
            parsed_date = parser.parse_date(text)
            assert parsed_date == datetime.datetime(2021,3,22)
            text = '22/03/21'
            parsed_date = parser.parse_date(text)
            assert parsed_date == datetime.datetime(2021,3,22)
            text = '22. Mart 2021.'
            parsed_date = parser.parse_date(text)
            assert parsed_date == datetime.datetime(2021,3,22)
            text = '22. Mar 2021'
            parsed_date = parser.parse_date(text)
            assert parsed_date == datetime.datetime(2021,3,22)
            text = '22. Mar 21'
            parsed_date = parser.parse_date(text)
            assert parsed_date == datetime.datetime(2021,3,22)
            text = '2021-03-22'
            parsed_date = parser.parse_date(text)
            assert parsed_date == datetime.datetime(2021,3,22)

