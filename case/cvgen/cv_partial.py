from ui import UI

from ui.low.file_cvpartial import FileCvPartial
from tool.generators.generator import gen_key

__author__ = 'John Underwood'


class CvPartial(UI):
    """
    Test the saving of a new education partial. Uses only one placeholder.
    """
    FileCvPartial()
    partial_name = 'auto_edu_' + gen_key(6)

    runtime = {
        'create': ('Click', '//*[@id="template-list"]/ul/li[1]/a', ),
        'partialName': ('Type', '#partials_name', partial_name),
        'category': ('Select', '#partials_category', 'Education'),
        'placeholder': ('Click', '//*[@id="control-list"]/ul/li[9]/a', ),
        'save': ('Click', '#savePartial', ),
    }

    expected = partial_name
    process = UI()
    order = ('create', 'partialName', 'category', 'placeholder')
    process.update(runtime)
    process.execute(order)
    process.wait(1)

    order = ('save', )
    process.execute(order)
    process.wait(1)

    process.results(expected, locator='//*[@id="template-list"]/ul')

    process.wait(1)
    process.teardown()
