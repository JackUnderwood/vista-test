__author__ = 'John Underwood'
from ui import UI


class TravelSpecialty(UI):
    """
    Pre-requirement: needs to be on the Travel page - execute file mod first.
    Case test goes to EM and then selects an assignment.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {  # specialty default EM
            'selectSpecialty': ("Click", '//*[@id="content"]/div[1]/div', ""),
            'selectAssign': ("Click", '//*[@id="138924"]/div[1]', "")
        }
        process = UI(override)
        process.update(runtime)
        order = ('selectSpecialty', 'selectAssign')
        process.execute(order)
