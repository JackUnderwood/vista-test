__author__ = 'John Underwood'

from ui import UI
from ui.low.file import File
from ui.high.file_select import FileSelect


class FileDeactivate(UI):
    File()
    FileSelect()

    runtime = {
        'delete': ('Click', '#delete'),
        'deactivate': ('Click', '//*[@button="delete"]'),
    }

    expected = "Status updated successfully"
    process = UI()
    process.update(runtime)
    order = ('delete', 'deactivate', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()

