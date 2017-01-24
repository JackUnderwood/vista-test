import ui
from ui import UI
from ui.low.job_icon import JobIcon
from tool.generators.generator import gen_key
__author__ = 'John Underwood'


class JobSaveICtrl(UI):
    """
    Regression test for story #137446781 - save a new control
    """
    JobIcon()
    control_name = "Procedures_" + gen_key(range_size=8)
    ui.log.info("JobSaveICtrl __init__() called")
    ui.log.info("Expected Control Name: {}".format(control_name, ))

    runtime = {
        'create': ('Click', 'css=#control-list>ul>li.active>a'),
        'name': ('Type', '#control_name', control_name),
        'description': ('Type', '#control_description', 'A new control'),
        'active': ('Click', '//*[@id="control-editor"]/label[3]'),
        'controlType': (
            'Select', '#job_description_control_type_id', 'TextArea Input'),
        'external': ('Click', '//*[@id="control-editor"]/div[1]/label[2]'),
        'internal': ('Click', '//*[@id="control-editor"]/div[1]/label[3]'),
        'save': ('Click', '#control-save'),
        'delete': ('Click', '#control-delete')

    }
    expected = "Save Successful"
    process = UI()
    # Test control creation
    process.update(runtime)
    order = ('create', 'name', 'description', 'active', 'controlType',
             'external', 'internal', 'save')
    process.execute(order)
    process.wait(1)
    process.results(expected)

    order = ('delete', )
    process.execute(order)

    # Test deletion alert
    alert_text = process.dismiss_alert()
    expected = 'Are you sure you want to delete this control?'
    actual = expected in alert_text
    process.compare(True, actual)

    process.teardown()
