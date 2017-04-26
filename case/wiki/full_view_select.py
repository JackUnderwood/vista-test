from ui import UI
from ui.low.wiki import Wiki

__author__ = 'John Underwood'


class FullViewSelect(UI):
    """
    Selects a wiki from the wiki's full view page.
    """
    process = UI()
    Wiki()

    process.update({
        'fullView': ('Click', '//*[@id="wiki_form"]/a'),
        'select': ('Select', '#wiki-entry', 'Licensing')
    })
    expected = 'Licensing Resources'
    process.execute(('fullView', 'select',))
    process.wait()
    actual = process.spy('#wiki-title', 'innerHTML')
    process.compare(expected, actual)
    process.wait()
    process.teardown()
