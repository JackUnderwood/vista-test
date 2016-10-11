from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_search import JobSearch
from tool.utilities import get_configurations
from tool.generators.generator import gen_key

__author__ = 'John Underwood'


class JobReviewed(UI):
    """
    Edit a job as a non-admin user, then login as an admin user, and
    review the edited job.
    If job_board_post_status.last_approval_date < jobs.last_changed_date, then
    reviewed button is visible... if reviewed button is click,
    last_approval_date gets updated.
    """

    # Log in as non-admin user.
    username = get_configurations('USER_IMPOSTOR', 'name')
    user_id = get_configurations('USER_IMPOSTOR', 'user_id')
    runtime = {
        'impostor': ('Click', 'css=body>header>nav>div>ul.right>'
                              'li:nth-child(5)>a>i', ),
        'userId': user_id,
        'user': ('Type', '#change-user-user_key_id_desc', username),
        'select': ('Click', '//*[@item_id="&userId;"]'),
    }
    process = UI()
    process.update(runtime)
    order = ('impostor', 'user', 'select', )
    process.execute(order)

    # Non-admin user edits a job.
    job_number = '92127'
    JobPosts()
    JobSearch(override={'num': job_number})
    subtitle = gen_key()  # a 12 char random string of text

    runtime = {
        'subtitleText': subtitle,
        'edit': ('Click', '#edit_' + job_number,),
        'subtitle': ('Type', '#job_board_subtitle', '&subtitleText;'),
        'save': ('Click', '#drawer-save', ),
    }
    process.update(runtime)
    order = ('edit', 'subtitle', )
    process.execute(order)
    process.wait(2)
    process.execute(('save', ))

    # Change back to admin user.
    process.get('site/logout')
    process.wait(1)
    JobPosts()
    JobSearch(override={'num': job_number})
    runtime = {
        'view': ('Click', '#view_' + job_number,),
        'reviewed': ('Click', '#review_' + job_number,),
    }
    process.update(runtime)
    order = ('view', )
    process.execute(order)

    # Spy to see if Reviewed button is available
    addendum = "This is the first of two possible results"
    expected = "Reviewed"
    actual = process.spy('#review_' + job_number, 'innerHTML')
    if process.compare(expected, actual, message=addendum):
        # Now, click the "Reviewed" button
        addendum = "This is the second and final of two results"
        expected = 'Approval Updated for Job {}'.format(job_number, )
        order = ('reviewed', )
        process.execute(order)
        process.results(expected, locator='toast-container', message=addendum)

    process.wait(1)
    process.teardown()


