import pytest
import datetime
from cov19.vaccination.templates.human_template import HumanTemplate

@pytest.fixture
def human_template():
    return HumanTemplate()

class TestParserFactory(object):

    def test_create_parser(self, capsys, human_template):
        with capsys.disabled():
            # TODO: add translation here!
            result = {
                'sentence': 'U Srbiji je do sada dato   2.007.650 doza vakcina protiv koronavirusa, a 782.668 osoba primilo je i drugu dozu, pokazuju najnoviji podaci Vlade Srbije.',
                'total_number_of_vaccinations': 2007650,
                'fully_vaccinated': 782668,
                'valid': True,
                'news_datetime': datetime.datetime(2021, 3, 15, 7, 0),
                'date': datetime.datetime(2021, 3, 14, 0, 0),
                'source': 'Serbian National TV'
            }
            output = human_template.generate(result)
            assert output == '''Hi @edomt

Here is the latest report for 14.03.2021
total_vaccinations: 2.007.650
people_fully_vaccinated: 782.668
people_vaccinated: 782.668 + (2.007.650 - (2 * 782.668)) = 1.224.982
total_vaccinations_per_hundred: 100 * 2.007.650/6.804.596 = 29.50432325445919

Source: Serbian National TV / 15.03.2021, 07:00



"U Srbiji je do sada dato   2.007.650 doza vakcina protiv koronavirusa, a 782.668 osoba primilo je i drugu dozu, pokazuju najnoviji podaci Vlade Srbije."
"In Serbia, according to latest Gov data, there was 2007650 vaccinations against Corona virus and 782668 citizens have received second vaccine dose"'''
