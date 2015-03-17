__author__ = 'John Underwood'
from ui import UI


class TravelSpecialty(UI):
    """
    NOT IN A USABLE STATE - see TODOs.
    Pre-requirement: needs to be on the Travel page - execute low.travel first.
    Case test goes to EM. //*[@id="143545"]/div[1]
    """
    def __init__(self, override=None):
        super().__init__(override)

        runtime = {
            'selectSpecialty': ("Click", '//*[@id="content"]/div[5]/div', ""),
            'provider': '143545',
            'selectAssign': ("Click", '//*[@id="&provider;"]/div[1]', ""),
        }
        process = UI()
        process.update(runtime)
        order = ('selectSpecialty', 'selectAssign')
        process.execute(order)
