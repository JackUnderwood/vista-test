__author__ = 'John Underwood'

from ui import UI


class CorrSelections(UI):
    """
    Pre-requirement: needs to be on the Correspondence page -
    execute low.correspond first.

    Currently not in a fully working state, since adding new UI skin.
    """
    def __init__(self):
        super().__init__()
        # //*[@id="correspond_form"]/div[1]/div[1]/div[2]/div[2]
        runtime = {
            'selectCat': (  # //*[@id="category"]
                'Click',
                '//*[@id="button_notification"]/div[2]/div',
            ),
            # Broken from here down.
            'category': (
                'Click',
                '//*[@id="slide-out"]/li[3]/ul/li/div/ul/li[2]',
            ),
            'template': ('Select', '#template_id', 'ECFMG request'),
            'waitBoard': ('Wait', 'board_id', 5),
            'board': (
                'Select',
                '#board_id',
                'American Board Of Anesthesiology - NC - Raleigh'  # override
            ),
            'find': ('Find', '#desc_provider_id', 'campbell'),  # override
            'waitResult': ('Wait', 'display_box_container', 5),
        }

        process = UI()
        process.update(runtime)
        order = ('selectCat', )
        # 'category', 'template', 'waitBoard', 'board', 'find', 'waitResult', )
        process.execute(order)
