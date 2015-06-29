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
        'next': '//*[@id="toolPanelContainer"]/div[2]/div[7]/a[2]',
        'next1': ('Click', '&next;', ),
        'splitPage': ('Click', '//*[@page="1"]'),
        'next2': ('Click', '&next;'),
        'inputProvider': (
            'Type',
            '#editSearchDescription',
            'lambert matt st:wv'
        ),
        'selectProvider': ('Click', '#user_name'),
        'category': ('Click', '#editObjectContainer'),
        'catLicenses': ('Click', '//*[@title="Licenses"]'),
        'subcategory': ('Click', '#editCategoryContainer'),
        'subcatStateLicense': ('Click', '//*[@title="State License"]'),
        'filename': ('Type', '#editNameContainer', 'qa_automation.pdf'),
        'next3': ('Click', '&next;'),
        'create': ('Click', '//*[@id="toolPanelContainer"]/div[2]/div[7]/a[3]')
    }

    expected = ""
    process = UI()
    process.update(runtime)
    order = ('', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()

