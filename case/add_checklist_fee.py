from ui.low.license import UI, License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class AddChecklistFee(UI):
    runtime = {
        'checklist': (
            'Click',
            '//*[@id="content"]/div[2]/div[1]/ul/div/div/a'),
        'feeAmount': '75',
        'fee': (
            'Type',
            '//*[@id="checklist-form-container"]/div[3]/div[3]/input',
            '&feeAmount;'),
        'save': ('Click', '//*[@id="checklist-form-container"]/div[3]/div[6]/a')
    }
    expected = 'Saved'
    License()
    Checklist(override={'rowNum': '10'})
    process = UI()
    process.update(runtime)
    order = ('checklist', 'fee', 'save')
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.update({'feeAmount': '', })  # clear
    process.execute(('fee', 'save', ))
    process.teardown()
