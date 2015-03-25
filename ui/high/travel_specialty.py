__author__ = 'John Underwood'
from ui import UI


class TravelSpecialty(UI):
    """
    Pre-requirement: needs to be on the Travel page - execute low.travel first.
    Case test goes to EM. //*[@id="143545"]/div[1]
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'div': '5',
            'selectSpecialty': (
                "Click", '//*[@id="content"]/div[&div;]/div',),
            'provider': '143545',
            'selectAssign': ("Click", '//*[@id="&provider;"]/div[1]',),
        }
        process = UI(override)
        process.update(runtime)
        order = ('selectSpecialty', 'selectAssign')
        process.execute(order)
