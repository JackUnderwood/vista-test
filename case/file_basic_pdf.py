__author__ = 'John Underwood'
"""
This file's name must have the 'pdf' char combination to use the viewer,
e.g. file_basic_pdf.py

This test  uses the Chrome PDF Viewer, so it needs the following driver's option
added add_experimental_option('excludeSwitches', ['test-type'])
The vtf.py file reads in the file's name and does a find for 'pdf' in the file's
name. If it sees that char combination, then it will set utils.is_pdf to True,
which then allows the option 'excludeSwitches' to be set.

An infobar warning banner will display, "You are using an unsupported
command-line flag: --ignore-certificate-errors. Stability and security will
suffer."
"""
from ui import UI
from ui.low.file import File


class FileBasic(UI):
    File()

    runtime = {
        'category': ('Click', '//*[@id="vsubnav"]/div/div[2]/ul', ),
        'selectCategory': ('Click', '//*[@id="vsubnav"]/div/div[2]/ul/ul/li[2]'),
        'subcategory': ('Click', '//*[@id="vsubnav"]/div/div[3]/ul', ),
        'selectSubcategory': (
            'Click',
            '//*[@id="vsubnav"]/div/div[3]/ul/ul/li[12]'
        ),
        'selectFile': ('Click', '//*[@id="fileList"]/div[2]/div/div[2]/div[2]')
    }
    process = UI()
    process.update(runtime)
    order = ('category', 'selectCategory', 'subcategory',
             'selectSubcategory', 'selectFile', )
    process.execute(order)
    process.wait(3)
    process.teardown()
