from tool.jobpost.helpers import enter_job_number, get_color, find_white_rows
import ui
from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_active_hot import JobActiveHot

__author__ = 'John Underwood'


class ReadyToPost(UI):
    """
    Fill in necessary elements using a 'white' status job and set the job to 
    'Ready to Post'--blue. Test that it changes to the correct status and row
    has the correct background color--blue #cee.
    """
    JobPosts()
    JobActiveHot()

    process = UI()
    res = find_white_rows(process)
    job_number = res['job_number']
    if job_number is None:
        ui.log.warning('FAILED: no job number available')
        process.teardown()

    edit_button_locator = "#edit_{}".format(job_number, )
    runtime = {
        'edit': ('Click', edit_button_locator, ),
        'subtitle': ('Type', '#jobs__job_board_subtitle', 'QA Subtitle Automate'),
        'template': ('Select',
                     '#JobDescriptionTemplates__job_description_template_id',
                     'Cardiology'),
        'readyToPost': (
            'Click',
            '//*[@id="jobEdit"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/label'),
        'save': ('Click', '#edit-save'),
    }
    process.update(runtime)
    expected = 'Job Saved'
    # If we do the template before the subtitle, then the Alert will not display.
    order = ('edit', 'template', 'subtitle', 'readyToPost', )
    process.execute(order)
    process.wait()
    process.execute(('save', ))
    process.wait()
    process.results(expected)
    process.get('jobs/search')
    process.wait()
    enter_job_number(process, job_number)

    expected_color = '#cceeee'
    locator = '//*[@id="result-target"]/tbody/tr[1]'
    rgb = process.get_css_property(locator, 'background-color')
    actual_color = get_color(rgb)
    process.compare(expected_color, actual_color,
                    message="compare background color")
    process.wait()
    process.teardown()
