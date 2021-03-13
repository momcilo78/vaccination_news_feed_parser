import jinja2

class HumanTemplate(object):
	name='human'
	template_str = '''
Hi @edomt
Here is the latest report for {{ date.strftime("%d.%m.%Y") }}
total_vaccinations: {{ total_number_of_vaccinations }}
people_fully_vaccinated: {{ fully_vaccinated }}
people_vaccinated: {{ fully_vaccinated }} + ({{ total_number_of_vaccinations }} - (2*{{ fully_vaccinated }})) = {{ fully_vaccinated + (total_number_of_vaccinations - (2 * fully_vaccinated)) }}
total_vaccinations_per_hundred: 100 * {{ total_number_of_vaccinations }}/6.804.596 = {{ total_number_of_vaccinations /6804596}}

Source: {{ source }} / {{ news_datetime.strftime("%d.%m.%Y, %H:%M") }}

{{ url }}

"{{ sentence }}"
"In Serbia, according to latest Gov data, there was {{ total_number_of_vaccinations }} vaccinations against Corona virus and {{ fully_vaccinated }} citizens have received second vaccine dose"	
'''
	def __init__(self):
		self.template = jinja2.Template(HumanTemplate.template_str)
	
	def generate(self, result):	
		return self.template.render(result)