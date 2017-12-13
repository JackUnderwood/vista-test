from ui import UI
from ui.low.file import File

__author__ = 'John Underwood'


class SplitTwo(UI):
    """
    Uploads a known two page file, and splits it into two different files.
    """
    File()
    file_path = 'C:\Projects_QA\_files_for_testing\CVDianaSunday.pdf'
    xpath = '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div[1]/div/a[1]'
    runtime = {
        'split': ('Click', '//*[@id="vsubnav"]/div/div[6]/a[3]'),
        'hover': ('Hover', xpath),
        'upload': ('Upload', xpath, file_path),
    }
    process = UI()
    process.update(runtime)
    process.execute(('split', 'hover', 'upload'))

    process.wait()
    process.teardown()
