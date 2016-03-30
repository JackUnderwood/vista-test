from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class FileUpload(UI):
    """
    Regression test for story #96802980
    """
    License()
    Checklist()

    runtime = {
        'examinations': (
            'Click', 'css=#content>div.row>div.col.s3>ul>div>a:nth-child(3)'),
        'malpractice': (
            'Click', 'css=#ribbon_form>ul>li>div.collapsible-body>'
                     'div:nth-child(5)>div.col.s6.right-buttons.right-align>'
                     'a:nth-child(2)>span'),
        'fileCloud': ('Click', 'css=#experienceUpload>div>div.FWUploadDropZone>'
                               'i.fa-stack.fa.fa-cloud-upload')

    }
    expected = "foobar"
    process = UI()
    process.update(runtime)
    order = ('examinations', 'malpractice', 'fileCloud', )
    process.execute(order)
    process.wait(3)
    # process.results(expected)
    # process.teardown()

