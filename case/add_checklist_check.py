from ui.low.license import UI, License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class AddChecklistCheck(UI):
    License()
    Checklist(override={'rowNum': '3'})
    runtime = {
        'checklist': (
            'Click',
            '//*[@id="content"]/div[2]/div[1]/ul/li[7]/a'),
        'note': (
            'Type',
            '//*[@id="checklist-form-container"]/div[3]/div[2]/input',
            'Important note for check'),
        'fee': (
            'Type',
            '//*[@id="checklist-form-container"]/div[3]/div[3]/input',
            '375'),
        'check': (  # check-off the requirement
            'Click', '//*[@id="checklist-form-container"]/div[3]/div[1]/label')
    }
    expected = "Saved"
    process = UI()
    process.update(runtime)
    order = ('checklist', 'note', 'fee', 'check', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
