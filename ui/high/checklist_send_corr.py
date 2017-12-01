import ui
from ui import UI

__author__ = 'John Underwood'


class ChecklistSendCorr(UI):

    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'send': ('Click',
                     '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[1]/i'),
            'template': ('Click',
                         '//*[@id="correspondenceChooser_form"]/p[2]/p[10]/a'),
        }
        ui.log.info("Select the License Renewal template")
        process = UI(override)
        process.update(runtime)
        process.execute(('send', 'template',))
        process.wait(3)
        process.check_for_new_window()
