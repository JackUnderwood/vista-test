__author__ = 'John Underwood'

from ui import UI
from ui.low.file import FileBegin
from ui.high.file_my_queue import FileMyQueue


class File10001(UI):
    """
    Purpose: dummy testcase; goes to the File page.
    This test case is a trial test to see how the vtf will be use. It tests
    naming convention of regression files, tests interaction between modules,
    tests how to handle setup and teardown (should it use vtf base file), etc.
    """
    FileBegin()
    FileMyQueue()

    runtime = {
        'file1': (
            "Click",
            '//*[@id="fileList"]/div[2]/div/div[2]/div[4]',
            ""
        ),
        'file2': (
            "Click",
            '//*[@id="fileList"]/div[2]/div/div[2]/div[5]',
            ""
        ),
    }
    process = UI()
    process.update(runtime)
    order = ('file1', )
    process.execute(order)
    process.wait(1)
    order = ('file2', )
    process.execute(order)
    process.wait(8)
    process.teardown()

