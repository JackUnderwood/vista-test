from ui.low.license import UI, License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class AddChecklistNote(UI):
    License()
    Checklist(override={'rowNum': '15'})
    runtime = {
        'checklist': (
            'Click',
            '//*[@id="content"]/div[2]/div[1]/ul/li[7]/a'),
        'check': (  # the requirement's checkbox
            'Click', '//*[@id="checklist-form-container"]/div[3]/div[1]/label'),
        'note': (
            'Type',
            '//*[@id="checklist-form-container"]/div[3]/div[2]/input',
            'Some important note from automation'),
        'noteClr': (
            'TypeAndTab',
            '//*[@id="checklist-form-container"]/div[3]/div[2]/input', ''),
        'save': ('Click', '//*[@id="checklist-form-container"]/div[3]/div[6]/a'),
        'wait': ('Wait', '#scratch-pad', {'condition': 'element_to_be_clickable'})
    }
    expected = 'Saved'
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
    order = ('wait', 'note', 'save')
    process.execute(order)
    process.results(expected)
    # Clean out the field
    process.wait()
    order = ('noteClr', 'save')
    process.execute(order)
    process.wait()
    process.teardown()
