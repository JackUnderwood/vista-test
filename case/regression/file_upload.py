from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class FileUpload(UI):
    # TODO: needs expected results.
    """
    Regression test for story #96802980 --
    """
    License()
    Checklist()
    file_path = 'C:\Projects_QA\_files_for_testing\CVDianaSunday.pdf'

    runtime = {
        'examinations': (
            'Click', '//*[@id="content"]/div[2]/div[1]/ul/li[4]/a'),
        'malpractice': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[2]/span'),
        'fileCloud': ('Upload',
                      '//*[@id="experienceUpload"]/div/div[2]/input[1]',
                      'C:\Projects_QA\_files_for_testing\CallReport.pdf')

    }
    expected = "Upload Successful"
    process = UI()
    process.update(runtime)
    order = ('examinations', 'malpractice', 'fileCloud', )
    process.execute(order)
    process.wait(3)
    process.results(expected)
    process.wait()
    process.teardown()

