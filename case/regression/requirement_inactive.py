from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class RequirementInactive(UI):
    """ Under construction
    Regression test for story #113028615
    """
    License()
    Checklist()

    runtime = {
        'checklist': ('Click', 'css=#content>div.row>div.col.s3>ul>'
                               'li:nth-child(7)>a'),
        'manage': (
            'Click',
            '//*[@id="checklist-form-container"]/div[3]/div[5]/a/i'),
        'active': (
            'Click',
            '//*[@id="stateLicenseRequirementEdit_form"]/div[1]/div[2]'
            '/label/span'),
        'save': (
            'Click', '//*[@id="stateLicenseRequirementEdit_form"]/div[5]/a[2]')
    }
    process = UI()
    process.update(runtime)
    order = ('checklist', )
    process.execute(order)

    # Get the first Requirement's label
    initial = process.spy(
        '//*[@id="checklist-form-container"]/div[3]/div[1]/label',
        'innerHTML', ).strip()
    # Set the first Requirement to Inactive
    order = ('manage', )
    process.execute(order)
    process.wait(2)  # need time to display the requirement listing
    order = ('active', 'save', )
    process.execute(order)
    # Comparison should NOT match
    # Add a new Requirement
    # Test case: check to see if the Inactive Requirement becomes active
    # Set Requirements back to the 'Active' state
    process.wait(5)
    process.teardown()
