__author__ = 'John Underwood'

from ui import UI
from ui.low.file import File
from ui.high.file_select import FileSelect


class FileRename(UI):
    File()
    FileSelect()

    runtime = {
        'rename': ('Click', '#rename'),
        'execRename': ('Click', '//*[@button="rename"]')
    }

    expected = "Document Description Updated"
    process = UI()
    process.update(runtime)
    order = ('rename', 'execRename')
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
