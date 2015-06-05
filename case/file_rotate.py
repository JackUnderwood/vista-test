__author__ = 'John Underwood'

from ui import UI
from ui.low.file import File
from ui.high.file_select import FileSelect


class FileRotate(UI):
    File()
    FileSelect()

    runtime = {
        'rotate': ('Click', '#rotate'),
        'selectPage': (
            'Click',
            '//*[@id="toolPanelContainer"]/div[2]/div/div/div[2]/div[2]',
        ),
        'rotateLeft': ('Click', '#rotateLeft'),
    }

    expected = "Rotate was successful"
    process = UI()
    process.update(runtime)
    order = ('rotate', 'selectPage', 'rotateLeft', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
