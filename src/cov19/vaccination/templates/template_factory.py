from cov19.vaccination.templates.human_template import HumanTemplate

class TemplateFactory(object):
    templates = [
            HumanTemplate
        ]
    @staticmethod
    def create_template(template_name):        
        for template_class in TemplateFactory.templates:
            if template_class.name == template_name:
                return template_class()
        raise Exception(f'Unable to find the template {template_name}')