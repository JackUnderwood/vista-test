from ui.low.license import UI, License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class AddChecklistFee(UI):
    License()
    Checklist()
    runtime = {
        'checklist': (
            'Click',
            '//*[@id="content"]/div[2]/div[1]/ul/li[7]/a'),
        'check': (  # check-off the requirement
            'Click', '//*[@id="checklist-form-container"]/div[3]/div[1]/label'),
        'feeAmount': '75',
        'fee': (
            'Type',
            '//*[@id="checklist-form-container"]/div[3]/div[3]/input',
            '&feeAmount;'),
        'save': ('Click', '//*[@id="checklist-form-container"]/div[3]/div[6]/a'),
        'wait': ('Wait', '#scratch-pad', {'wait_time': 8, })
    }
    expected = 'Saved'
    process = UI()
    process.update(runtime)
    order = ('checklist',)
    process.execute(order)
    process.wait()
    temp = process.spy('#cklr_0', 'checked')  # determine if item is checked
    if temp is not None:
        # This req has been check; we need to un-check it.
        order = ('check', )
        process.execute(order)
        process.wait()
    order = ('wait', 'fee', 'save', )
    process.execute(order)
    process.results(expected, message="input value into fee field")
    process.wait(2)
    process.update({'feeAmount': '', })  # clear
    process.execute(('fee', 'save', ))
    process.wait()
    process.results(expected, message="cleared field")
    process.teardown()
