from tool.jobpost.helpers import find_rows, get_color
from ui import UI
from ui.low.job_posts import JobPosts

__author__ = 'John Underwood'


class ReadyToPost(UI):
    """
    Fill in necessary elements using a 'white' status job and set the job to 
    'Ready to Post'--blue. Test that it changes to the correct status and row
    has the correct background color--blue #cee.
    """
    JobPosts()

    runtime = {
        'JobStatus': ('Click', 'css=.ui-multiselect.ui-widget.ui-state-default.'
                               'ui-corner-all.multi_s.multi_s_job_status'),
        'wait': ('Wait', '#ui-multiselect-s_job_status-option-1',
                 {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
        'JobStatusActive': (
            'Click', '#ui-multiselect-s_job_status-option-1'),
        'JobStatusHot': (
            'Click', '#ui-multiselect-s_job_status-option-4'),
        'expandAll': ('Click', '//*[@id="result-target"]/thead/tr[1]/td[3]/i[1]')
    }
    process = UI()
    process.update(runtime)
    order = ['JobStatus', 'wait', 'JobStatusActive', 'JobStatusHot', 'expandAll']
    process.execute(order)
    process.wait()
    ready_to_post_locator = './td/div/div[3]/div[2]/div[5]/div/div/div[2]/strong'
    rows = find_rows(process, 'expandable-row',
                     ready_to_post_locator, 'innerHTML')

    valid_rows = [r[0] for r in rows if 'No' in r]

    if len(valid_rows) < 1:
        process.compare(True, False, message="no valid rows available")
        process.teardown()
    # A row's edit button location //*[@id="edit_97866"]
    # ['expandable_97866', 'expandable_97861', ..., 'expandable_97852']
    # Get the id value; everything to the right of the underscore.
    # row_index = all_rows.index(row_job_number) + 1
    row_id = valid_rows[0][valid_rows[0].find('_') + 1:]
    edit_button_locator = "#edit_{}".format(row_id, )
    process.update({
        'edit': ('Click', edit_button_locator, ),
        'subtitle': ('Type', '#jobs__job_board_subtitle', 'QA Subtitle Automate'),
        'template': ('Select',
                     '#JobDescriptionTemplates__job_description_template_id',
                     'Cardiology'),
        'readyToPost': (
            'Click',
            '//*[@id="jobEdit"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/label'),
        'save': ('Click', '#edit-save'),
    })
    expected = 'Job Saved'
    # If we do the template before the subtitle, then the Alert will not display.
    order = ('edit', 'template', 'subtitle', 'readyToPost', 'save')
    process.execute(order)
    process.wait()
    process.results(expected)

    expected_color = '#cceeee'
    id_rows = [row[0] for row in rows]
    row_index = id_rows.index('expandable_{}'.format(row_id,))+1
    locator = '//*[@id="result-target"]/tbody/tr[{}]'.format(row_index, )
    rgb = process.get_css_property(locator, 'background-color')
    actual_color = get_color(rgb)
    process.compare(expected_color, actual_color,
                    message="compare background color")
    process.wait()
    process.teardown()
