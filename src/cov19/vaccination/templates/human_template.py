import jinja2
import locale

class HumanTemplate(object):
	name='human'
	template_str = '''Hi @edomt

Here is the latest report for {{ date.strftime("%d.%m.%Y") }}
total_vaccinations: {{ total_number_of_vaccinations | dots }}
people_fully_vaccinated: {{ fully_vaccinated | dots }}
people_vaccinated: {{ fully_vaccinated | dots }} + ({{ total_number_of_vaccinations | dots }} - (2 * {{ fully_vaccinated | dots }})) = {{ (fully_vaccinated + (total_number_of_vaccinations - (2 * fully_vaccinated))) | dots }}
total_vaccinations_per_hundred: 100 * {{ total_number_of_vaccinations | dots }}/6.804.596 = {{ (100 * total_number_of_vaccinations / 6804596 ) | dots}}

Source: {{ source }} / {{ news_datetime.strftime("%d.%m.%Y, %H:%M") }}

{{ url }}

"{{ sentence }}"
"In Serbia, according to latest Gov data, there was {{ total_number_of_vaccinations }} vaccinations against Corona virus and {{ fully_vaccinated }} citizens have received second vaccine dose"
'''
	def __init__(self):
		self.template = jinja2.Template(HumanTemplate.template_str)
	def generate(self, result):
		return self.template.render(result)
