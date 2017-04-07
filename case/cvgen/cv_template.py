from ui import UI

from ui.low.file_cvtemplate import FileCvTemplate
from tool.generators.generator import gen_key

__author__ = 'John Underwood'


class CvTemplate(UI):
    """
    Prerequisite: requires the creation of partials
    Use the first available partial, and save the new template.
    """
    FileCvTemplate()
    template_name = 'auto_' + gen_key(6)

    runtime = {
        'create': ('Click', '//*[@id="template-list"]/ul/li[1]/a', ),
        'templateName': ('Type', '#template_name', template_name),
        'partial': ('Click', '//*[@id="partials-list"]/ul/li[2]/a', ),
        'save': ('Click', '#saveTemplate', ),
    }

    expected = template_name
    process = UI()
    order = ('create', 'templateName', 'partial', 'save')
    process.update(runtime)
    process.execute(order)
    process.wait(1)

    process.results(expected, locator='//*[@id="template-list"]/ul/li[2]/a')

    process.wait(1)
    process.teardown()
