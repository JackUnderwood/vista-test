from ui.low.license import UI, License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class AddChecklistRequirement(UI):
    """
    Note: waiting for bug fix https://www.pivotaltracker.com/story/show/104940726
    """
    License()
    Checklist()
    runtime = {
        'addRequirement': (
            'Click',
            '//*[@id="checklist-form-container"]/div[2]/div/a/i'),
        'active': ('Click', '//*[@id="stateLicenseRequirementEdit_form"]/'
                            'div[1]/div[2]/label/span'),
        'state': ('Click', ''),  # TODO: WAIT state/cred/type may auto-fill
    }
    expected = 'Requirement saved'

