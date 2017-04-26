from ui import UI
from ui.low.wiki import Wiki

__author__ = 'John Underwood'


class DrawerViewSelect(UI):
    """
    Selects a wiki from the wiki's drawer.
    """
    process = UI()
    Wiki()

    process.update({
        'selectWiki': ('Select', '#wiki-entry', 'Licensing')
    })
    expected = 'Licensing Resources'
    process.execute(('selectWiki',))
    process.wait()
    actual = process.spy('#wiki-title', 'innerHTML')
    process.compare(expected, actual)
    process.wait()
    process.teardown()

