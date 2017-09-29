import ui
from ui import UI
from ui.low.job_icon import JobIcon
from tool.db import get_record
__author__ = 'John Underwood'


class JobICtrlOutputStyle(UI):
    """
    Regression test for story #137027335 - select a new default
    changes all input controls
    """
    JobIcon()
    ui.log.info("JobCtrlOutputStyle called")
    index = '5'  # ranges between [3-121]

    runtime = {
        'index': index,
        'inputControl': ('Click', '//*[@id="control-list"]/ul/li[&index;]/a')
    }
    expected = "Save Successful"
    process = UI()
    process.update(runtime)
    order = ('inputControl', )
    process.execute(order)

    locator = '//*[@id="control-list"]/ul/li[{}]/a'.format(index)
    job_description_control_id = process.spy(locator, 'data-control')
    ui.log.info("Option Value: {}".format(job_description_control_id,))

    sql = """
        SELECT multiselect_output_divider
        FROM job_description_controls
        WHERE job_description_control_id = '%s'
    """ % job_description_control_id

    record = get_record(sql)
    multiselect_output_divider = record[0][0]
    ui.log.info("Output Style: {}".format(multiselect_output_divider, ))

    process.compare('/', multiselect_output_divider,
                    message="check output style divider")

    process.wait(1)
    process.teardown()
