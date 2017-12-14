import ui
from ui import UI

__author__ = 'John Underwood'


class ChecklistSelectTemplate(UI):
    """
    Pre-requirement: needs to start from a provider's Checklist page
    """

    def __init__(self, override=None):
        super().__init__()
        # Access the 'Select a Template' drawer
        runtime = {
            'sendATemplatedCorrespondence': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[1]/i')
        }
        process = UI(override)
        process.update(runtime)
        process.execute(('sendATemplatedCorrespondence',))
