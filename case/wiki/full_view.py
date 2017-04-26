from ui import UI
from ui.low.wiki import Wiki

__author__ = 'John Underwood'


class FullView(UI):
    """
    Clicks on the Full View button inside the wiki drawer.
    """
    process = UI()
    Wiki()

    process.update({
        'fullView': ('Click', '//*[@id="wiki_form"]/a'),
    })
    expected = 'Wiki'
    process.execute(('fullView', ))
    process.wait()

    process.results(expected)
    process.wait()
    process.teardown()
