__author__ = 'John Underwood'

from ui import UI
from ui.low.file import File
from ui.high.file_select import FileSelect


class FileSplit(UI):
    # TODO: Need feedback message for Create split

    File()
    FileSelect()

    runtime = {
        'edit': ('Click', '#edit'),
        'next': ('Click', '//*[@id="toolPanelContainer"]/div[2]/div[7]/a[2]'),
        # 'next1': ('Click', '&next;', ),
        'selectPage1': (
            'Click',
            '//*[@id="toolPanelContainer"]/div[2]/div[4]/div[2]/div[2]'),

        'subcategory': ('Select', '#editCategory', 'Provider Licensing'),
        'filename': ('Type', '#editFilename', 'qa_automation.pdf'),
        # TODO: auto generate file names

        'create': ('Click', '//*[@id="toolPanelContainer"]/div[2]/div[7]/a[3]')
    }

    expected = "Files successfully edited"
    process = UI()
    process.update(runtime)
    order = ('edit', 'next', 'selectPage1', 'next', 'subcategory', 'filename',
             'next', 'create')
    process.execute(order)
    process.wait(1)
    process.results(expected)
    process.wait(3)
    process.teardown()

