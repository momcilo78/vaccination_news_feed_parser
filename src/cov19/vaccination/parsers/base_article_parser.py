import re
from dns.rdataclass import NONE


class BaseArticleParser(object):
    def __init__(self):
        regex_number = r"([0-9]{1,3}([\.]?[0-9]{3})*)"

        regex_sentence_total_vaccination_list = []
        regex_sentence_total_vaccination_list.append(r"vakcinisano je {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"je vakcinisano {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"dato {regex_number} (vakcina|doza)".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"dato\s+{regex_number} doza vakcina".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"dato\s+{regex_number} (doza|vakcina)".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"dato je\s+{regex_number} (vakcina|doza)".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"dato je\s+ukupno\s+{regex_number} (vakcina|doza)".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"Ukupno vakcinacija:\s+{regex_number}".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"obavljeno ukupno\s+{regex_number} vakcinacija".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"obavljeno\s+{regex_number} vakcinacija".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"izvršene\s+{regex_number} vakcinacije".format(regex_number=regex_number))
        regex_sentence_total_vaccination_list.append(r"izvršeno\s+{regex_number} vakcinacija".format(regex_number=regex_number))

        self.regex_sentence_total_vaccination_list = self._compile_regex(regex_sentence_total_vaccination_list)

        regex_sentence_fully_vaccinated_list = []
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (građana|gradjana|ljudi|osoba) primilo je (i )?drugu dozu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"drugu dozu primilo je {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"drugu dozu je primilo {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"drugu dozu vakcine primilo je {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"drugu dozu vakcine je primilo {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"drugi dozu vakcine primilo je {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"drugu dozu vakcine primio je {regex_number} (građanin|gradjnin)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"drugu dozu vakcine je primio {regex_number} (građanin|gradjnin)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"drugu dozu primio je {regex_number}\s+(građanin|gradjnin)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"drugu dozu je primio {regex_number} (građanin|gradjnin)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (građana|gradjana|ljudi|osoba) dobilo je drugu vakcinu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (građana|gradjana|ljudi|osoba) dobilo je i drugu vakcinu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (građana|gradjana|ljudi|osoba) dobilo je drugu dozu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (građana|gradjana|ljudi|osoba) dobilo je i drugu dozu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze primilo je {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze je primilo {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze vakcine primilo je {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze vakcine je primilo {regex_number} (građana|gradjana|ljudi|osoba)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze primila su {regex_number} (građanina|gradjanina|ljudi|osobe)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze su primila {regex_number} (građanina|gradjanina|ljudi|osobe)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze vakcine primila su {regex_number} (građanina|gradjanina|ljudi|osobe)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze vakcine su primila {regex_number} (građanina|gradjanina|ljudi|osobe)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze primio je {regex_number} (građanin|gradjanin)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze je primio {regex_number} (građanin|gradjanin)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze vakcine primio je {regex_number} (građanin|gradjanin)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"obe doze vakcine je primio {regex_number} (građanin|gradjanin)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"dato je {regex_number} druge doze vakcine".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"od čega je {regex_number} (građana|gradjana|ljudi|osobe) primilo i drugu dozu vakcine".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"od čega je {regex_number} (građana|gradjana|ljudi|osobe) primilo i drugu dozu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"od čega je {regex_number} (građana|gradjana|ljudi|osobe) primilo drugu dozu vakcine".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"od čega je {regex_number} (građana|gradjana|ljudi|osobe) primilo drugu dozu".format(regex_number=regex_number))

        self.regex_sentence_fully_vaccinated_list = self._compile_regex(regex_sentence_fully_vaccinated_list)

    def parse_text(self, text, result):
        result['text'] = text
        result['total_number_of_vaccinations'] = None
        result['fully_vaccinated'] = None
        result['quoted_text'] = []
        for sentence in text:
            total_vaccination_number_results = self._parse_against_regex_list(sentence, self.regex_sentence_total_vaccination_list)            
            if total_vaccination_number_results:
                result['total_number_of_vaccinations'] = total_vaccination_number_results
                result['quoted_text'].append(sentence)
            fully_vaccinated_number_results = self._parse_against_regex_list(sentence, self.regex_sentence_fully_vaccinated_list)
            if fully_vaccinated_number_results:
                result['fully_vaccinated'] = fully_vaccinated_number_results
                result['quoted_text'].append(sentence)
    
#     def parse_sentence(self, text, result):
#         total_vaccination_number_results = self._parse_against_regex_list(text, self.regex_sentence_total_vaccination_list)
#         fully_vaccinated_number_results = self._parse_against_regex_list(text, self.regex_sentence_fully_vaccinated_list)
#         result['text'] = text
#         result['total_number_of_vaccinations'] = total_vaccination_number_results
#         result['fully_vaccinated'] = fully_vaccinated_number_results

    def _compile_regex(self, regex_list):
        compiled_regex_list = []
        for regex in regex_list:
            compiled_regex = re.compile(regex, re.IGNORECASE)
            compiled_regex_list.append(compiled_regex)
        return compiled_regex_list

    def _parse_against_regex_list(self, text, regex_list):
        for regex_sentence in regex_list:
            regex_sentece_result = regex_sentence.search(text)
            if regex_sentece_result:
                result = int(regex_sentece_result.groups()[0].replace('.', ''))
                return result
