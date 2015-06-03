__author__ = 'John Underwood'

from ui import UI
from ui.low.file import File


class FileReset(UI):
    File()

    runtime = {
        'reset': ('Click', '//*[@id="vsubnav"]/div/i', )
    }
    expected = 'Options set to default'
    process = UI()
    process.update(runtime)
    process.execute(('reset', ))
    process.results(expected)
    process.teardown()
