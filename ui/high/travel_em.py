__author__ = 'John Underwood'
from ui import UI


class TravelEm(UI):
    """
    Pre-requirement: needs to be on the Travel page - execute file mod first.
    Case test goes to EM and then selects an assignment.
    """
    def __init__(self, override=None):
        super().__init__()
        print("TravelEm __init__", override)

        runtime = {
            'selectEm': ("Click", '//*[@id="content"]/div[1]/div', ""),
            'selectAssign': ("Click", '//*[@id="138924"]/div[1]', "")
        }
        process = UI(override)
        process.update(runtime)
        order = ('selectEm', 'selectAssign')
        process.execute(order)
