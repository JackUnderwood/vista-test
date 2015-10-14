__author__ = 'John Underwood'

from ui import UI
from ui.low.file import File
from ui.high.file_select import FileSelect


class FileReassign(UI):
    File()
    FileSelect()

    runtime = {
        'reassign': ('Click', '#reassign'),
        'inputProvider': (
            'Type',
            '#reassigneSearchDescription',
            'lambert matt st:wv'
        ),
        'selectProvider': ('Click', '//*[@item_id="91273"]'),
        'subcategory': ('Select', '#reassignCategory', 'Certifications'),
        'copy': ('Click', '#reassignCopy')
    }

    expected = "File move successful"
    process = UI()
    process.update(runtime)
    order = ('reassign', 'inputProvider', 'selectProvider',
             'subcategory', 'copy')
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
