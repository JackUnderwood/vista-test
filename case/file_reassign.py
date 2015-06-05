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
        'selectProvider': ('Click', '#user_name'),
        'category': ('Click', '//*[@id="reassignObjectContainer"]/ul'),
        'catLicenses': ('Click', '//*[@title="Licenses"]'),
        'subcategory': ('Click', '//*[@id="reassignCategoryContainer"]/ul'),
        'subcatStateLicense': ('Click', '//*[@title="State License"]'),
        'copy': ('Click', '#reassignCopy')
    }

    expected = "File move successful"
    process = UI()
    process.update(runtime)
    order = ('reassign', 'inputProvider', 'selectProvider', 'category',
             'catLicenses', 'subcategory', 'subcatStateLicense', 'copy')
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
