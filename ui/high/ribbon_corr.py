__author__ = 'John Underwood'

from ui import UI


class RibbonToCorrespondence(UI):

    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'correspondIcon': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[1]/i'
            ),
            'selectTemplate': (  # override
                'Click',
                '//*[@id="correspondenceChooser_form"]/p[2]/p[7]/a'
            ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('correspondIcon', 'selectTemplate', )
        process.execute(order)
