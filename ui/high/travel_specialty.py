__author__ = 'John Underwood'
from ui import UI


class TravelSpecialty(UI):
    """
    NOT IN A USABLE STATE.
    Pre-requirement: needs to be on the Travel page - execute low.travel first.
    Case test goes to EM.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {  # specialty default EM
            'selectSpecialty': ("Click", '//*[@id="content"]/div[1]/div', ""),
            'provider': '123456',  # TODO: __OVERRIDE__ provider id
            'selectAssign': ("Click", '//*[@id="#provider"]/div[1]', ""),
        }  # TODO: create a placeholder routine in vtf - see #89432718
        process = UI(override)
        process.update(runtime)
        order = ('selectSpecialty', )
        process.execute(order)
