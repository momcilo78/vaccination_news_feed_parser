from cov19.vaccination.templates.human_template import HumanTemplate
import jinja2


# define jinja2 filter that prints integer with thousands dot separators
if 'dots' not in jinja2.filters.FILTERS:
    jinja2.filters.FILTERS['dots'] = lambda v: '{:,}'.format(v).replace(',','.')


class TemplateFactory(object):
    templates = [
            HumanTemplate
        ]
    @staticmethod
    def create_template(template_name):
        if not isinstance(template_name, str):
            raise(TypeError('Input parameter template_name is not str'))
        for template_class in TemplateFactory.templates:
            if template_class.name == template_name:
                return template_class()
        raise LookupError(f'Unable to find the template {template_name}')
