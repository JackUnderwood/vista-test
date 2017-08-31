from ui.low.license import UI, License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class AddChecklistCheck(UI):
    License()
    Checklist(override={'rowNum': '1'})
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
            'Click', '//*[@id="checklist-form-container"]/div[3]/div[1]/label'),
        'noteClr': (
            'Type',
            '//*[@id="checklist-form-container"]/div[3]/div[2]/input', ''),
        'feeClr': (
            'Type',
            '//*[@id="checklist-form-container"]/div[3]/div[3]/input', ''),
        'save': ('Click', '//*[@id="checklist-form-container"]/div[3]/div[6]/a'),
    }
    expected = "Saved"
    process = UI()
    process.update(runtime)
    order = ('checklist', )
    process.execute(order)
    process.wait()
    temp = process.spy('#cklr_0', 'checked')  # determine if item is checked
    if temp is not None:
        # This req has been check; we need to un-check it.
        order = ('check', )
        process.execute(order)
        process.wait()
    order = ('note', 'fee', )
    process.execute(order)
    order = ('check', )
    process.execute(order)
    process.results(expected)
    process.wait()

    # Clear all & return it back to unchecked.
    order = ('check', )
    process.execute(order)
    process.wait()
    order = ('noteClr', 'feeClr', 'save')
    process.execute(order)
    process.results(expected)
    process.wait()
    process.teardown()
