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
        'note': (
            'Type',
            '//*[@id="checklist-form-container"]/div[3]/div[2]/input',
            'Some important note from automation'),
        'save': ('Click', '//*[@id="checklist-form-container"]/div[3]/div[6]/a'),
        'wait': ('Wait', '#scratch-pad', {'condition': 'element_to_be_clickable'})
    }
    expected = 'Saved'
    process = UI()
    process.update(runtime)
    order = ('checklist', 'wait', 'note', 'save')
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
