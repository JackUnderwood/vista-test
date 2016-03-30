from ui.low.license import UI, License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class AddChecklistNote(UI):
    License()
    Checklist(override={'rowNum': '10'})
    runtime = {
        'checklist': (
            'Click',
            '//*[@id="content"]/div[2]/div[1]/ul/div/div/a'),
        'note': (
            'Type',
            '//*[@id="checklist-form-container"]/div[3]/div[2]/input',
            'Some important note from automation'),
        'save': ('Click', '//*[@id="checklist-form-container"]/div[3]/div[6]/a')
    }
    expected = 'Saved'
    process = UI()
    process.update(runtime)
    order = ('checklist', 'note', 'save')
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
