import re
import datetime

class BaseArticleParser(object):
    def __init__(self):
        # regex for large integers
        regex_number = r"([0-9]{1,3}([\.]?[0-9]{3})*)"

        # regex for total vaccination
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
        regex_sentence_total_vaccination_list.append(r"date\s+{regex_number} doze (vakcine|vakcina)".format(regex_number=regex_number))
        self.regex_sentence_total_vaccination_list = self._compile_regex(regex_sentence_total_vaccination_list)

        # regex for full vaccinated
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
        regex_sentence_fully_vaccinated_list.append(r"drugu dozu primilo {regex_number} (građana|gradjna|osoba|ljudi)".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (građana|gradjana|ljudi|osoba) dobilo je drugu vakcinu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (građana|gradjana|ljudi|osoba) dobilo je i drugu vakcinu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (građana|gradjana|ljudi|osoba) dobilo je drugu dozu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (građana|gradjana|ljudi|osoba) dobilo je i drugu dozu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (građana|gradjana|ljudi|osoba) primilo je i drugu dozu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (osobe) primile su i drugu dozu".format(regex_number=regex_number))
        regex_sentence_fully_vaccinated_list.append(r"{regex_number} (osobe) primile su drugu dozu".format(regex_number=regex_number))
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

        # regex for purely numeric date
        regex_numeric_date_list = [
            # 22.03.2021 22.03.2021.
            r"(\d{1,2})\.(\d{1,2})\.(\d{4})\.?",
            # 22.03.21
            r"(\d{1,2})\.(\d{1,2})\.(\d{2})",
            # 22/03/2021
            r"(\d{1,2})\/(\d{1,2})\/(\d{4})",
            # 22/03/221
            r"(\d{1,2})\/(\d{1,2})\/(\d{2})",
        ]
        self.regex_numeric_date_list = self._compile_regex(regex_numeric_date_list)

        # lookup for months giving the numeric month
        self.lookup_numeric_month = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'maj': 5, 'jun': 6, 'jul': 7, 'avg': 8, 'sep': 9, 'okt': 10, 'nov': 11, 'dec': 12,
            'јан': 1, 'феб': 2, 'мар': 3, 'апр': 4, 'мај': 5, 'јун': 6, 'јул': 7, 'авг': 8, 'сеп': 9, 'окт': 10, 'нов': 11, 'дец': 12,
            'januar': 1, 'februar': 2, 'mart': 3, 'april': 4, 'maj': 5, 'jun': 6, 'jul': 7, 'avgust': 8, 'septembar': 9, 'oktobar': 10, 'novembar': 11, 'decembar': 12,
            'јануар': 1, 'фебруар': 2, 'март': 3, 'април': 4, 'мај': 5, 'јун': 6, 'јул': 7, 'август': 8, 'септембар': 9, 'октобар': 10, 'новембар': 11, 'децембар': 12,
            # ha ha, lets be forgiving
            'juni': 6, "juli": 7,
            'јуни': 6, "јули": 7
        }

        # regex for alpha numeric date
        regex_alpha_numeric_date_list = [
            # 23. Mart 2021., 23. Mart 2021,23. Mar 2021
            r"(\d{1,2})\.?\s+({months})\s+(\d{4})\.?".replace('{months}','|'.join(self.lookup_numeric_month.keys())),
            # 23. Mart 21., 23. Mart 21,23. Mar 21
            r"(\d{1,2})\.?\s+({months})\s+(\d{2})\.?".replace('{months}','|'.join(self.lookup_numeric_month.keys())),
        ]
        print(regex_alpha_numeric_date_list)
        self.regex_alpha_numeric_date_list = self._compile_regex(regex_alpha_numeric_date_list)

        # 2021-03-22, 2021-3-22, 2021-03-2
        self.regex_inverted_date = re.compile(r"(\d{4})-(\d{1,2})-(\d{1,2})")

        self.regex_time = re.compile(r"([0-1]?[0-9]|2[0-3]):([0-5][0-9])")

    def parse_date(self, text, century=(datetime.date.today().year // 100) - 1):
        # first numeric
        parsed_date = self._parse_date_against_numeric_regex_list(text, century)
        if parsed_date:
            return parsed_date
        # now with alpha-numeric date
        parsed_date = self._parse_date_against_alpha_numeric_regex_list(text, century)
        if parsed_date:
            return parsed_date
        # last resort: reverse
        parsed_date = self._parse_reverse_date(text)
        if parsed_date:
            return parsed_date
    
    def parse_time(self, text):
        regex_result = self.regex_time.search(text)
        if regex_result:
            groups = regex_result.groups()
            if len(groups) == 2:
                return datetime.timedelta(hours = int(groups[0]), minutes = int(groups[1]))
        

    def parse_text(self, text, result):
        result['text'] = text
        result['total_number_of_vaccinations'] = None
        result['fully_vaccinated'] = None
        result['quoted_text'] = []
        for sentence in text:
            total_vaccination_number_results = self._parse_against_regex_list(sentence, self.regex_sentence_total_vaccination_list)
            if total_vaccination_number_results:
                result['total_number_of_vaccinations'] = total_vaccination_number_results
                if sentence not in result['quoted_text']:
                    result['quoted_text'].append(sentence)
            fully_vaccinated_number_results = self._parse_against_regex_list(sentence, self.regex_sentence_fully_vaccinated_list)
            if fully_vaccinated_number_results:
                result['fully_vaccinated'] = fully_vaccinated_number_results
                if sentence not in result['quoted_text']:
                    result['quoted_text'].append(sentence)

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

    def _parse_date_against_numeric_regex_list(self, text, century):
        for regex in self.regex_numeric_date_list:
            regex_result = regex.search(text)
            if regex_result:
                day = int(regex_result.groups()[0])
                month = int(regex_result.groups()[1])
                year_string = regex_result.groups()[2]
                # if short year form is used make sure it uses century information
                if len(year_string) != 4:
                    year_string = f'{century + 1}{year_string}'
                year = int(year_string)
                result = datetime.datetime(year, month, day)
                return result

    def _parse_date_against_alpha_numeric_regex_list(self, text, century):
        for regex in self.regex_alpha_numeric_date_list:
            regex_result = regex.search(text)
            if regex_result:
                day = int(regex_result.groups()[0])
                month = self.lookup_numeric_month[regex_result.groups()[1].lower()]
                year_string = regex_result.groups()[2]
                # if short year form is used make sure it uses century information
                if len(year_string) != 4:
                    year_string = f'{century + 1}{year_string}'
                year = int(year_string)
                result = datetime.datetime(year, month, day)
                return result

    def _parse_reverse_date(self, text):
        regex = self.regex_inverted_date
        regex_result = regex.search(text)
        if regex_result:
            day = int(regex_result.groups()[2])
            month = int(regex_result.groups()[1])
            year = int(regex_result.groups()[0])
            result = datetime.datetime(year, month, day)
            return result
