from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_search import JobSearch

__author__ = 'John Underwood'
job_details = """VISTA represents a traditional Family Medicine opportunity in a
rural Central Texas junior college community.

Opportunity Benefits:
* Outpatient/Inpatient Primary Care position
* Attractive 18 month income guarantee ($224,496 for the first year!)
* Sign-on bonus (up to $25,000)
* Malpractice coverage

Community Benefits:
* Charming, junior college community of 4,000
* Located just 90 minutes west of Dallas/Fort Worth"""


class JobCancelEdit(UI):
    """
    Check that the JS alert box appears when trying to cancel an edited job.
    Uses the text in the alert box to compare; result is True
    """
    job_number = '92094'
    JobPosts()
    JobSearch(override={'num': job_number})

    runtime = {
        'subtitleText': "Rural Healthcare Central Texas",
        'descText': job_details,
        'edit': ('Click', '#edit_' + job_number,),
        'subtitle': ('Type', '#job_board_subtitle', '&subtitleText;'),
        'template': ('Select', '#template', 'Marketing Tab'),
        'description': ('TypeInCkeditor', '.cke_wysiwyg_frame', '&descText;'),
        'cancel': ('Click', '#drawer-close', )
    }
    expected = "Are you sure you want to lose your work?"
    process = UI()
    process.update(runtime)
    order = ('edit', 'subtitle', 'description', 'cancel', )
    process.execute(order)
    alert_text = process.accept_alert()
    actual = expected in alert_text
    process.compare(True, actual)
    process.wait(5)
    process.teardown()


