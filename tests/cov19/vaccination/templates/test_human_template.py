import pytest
import datetime
from cov19.vaccination.templates.human_template import HumanTemplate

@pytest.fixture
def human_template():
    return HumanTemplate()

class TestTemplateFactory(object):

    def test_create_parser(self, capsys, human_template):
        with capsys.disabled():
            # TODO: add translation here!
            result = {
                'text': ['Prema poslednjim podacima, u Srbiji je obavljeno ukupno 2.112.074 vakcinacija','Drugu dozu primio je 826.851 građanin naše zemlje.'],
                'total_number_of_vaccinations': 2112074,
                'fully_vaccinated': 826851,
                'valid': True,
                'news_datetime': datetime.datetime(2021, 3, 19, 8, 22),
                'date': datetime.datetime(2021, 3, 18, 0, 0),
                'source': 'Serbian National TV',
                'quoted_text': ['Prema poslednjim podacima, u Srbiji je obavljeno ukupno 2.112.074 vakcinacija','Drugu dozu primio je 826.851 građanin naše zemlje.'],
                'translation': 'According to the latest data, a total of 2,112,074 vaccinations were performed in Serbia. 826,851 citizens of our country received the second dose.'
            }
            output = human_template.generate(result)
            assert output == '''Hi @edomt

Here is the latest report for 18.03.2021
total_vaccinations: 2.112.074
people_fully_vaccinated: 826.851
people_vaccinated: 826.851 + (2.112.074 - (2 * 826.851)) = 1.285.223
total_vaccinations_per_hundred: 100 * 2.112.074/6.804.596 = 31.038933097571114

Source: Serbian National TV / 19.03.2021, 08:22



"Prema poslednjim podacima, u Srbiji je obavljeno ukupno 2.112.074 vakcinacija Drugu dozu primio je 826.851 građanin naše zemlje."
"According to the latest data, a total of 2,112,074 vaccinations were performed in Serbia. 826,851 citizens of our country received the second dose."'''