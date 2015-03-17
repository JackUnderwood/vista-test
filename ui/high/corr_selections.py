__author__ = 'John Underwood'

from ui import UI


class CorrSelections(UI):
    """
    Pre-requirement: needs to be on the Send Correspondence page -
    execute low.correspond first.
    """
    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'category': ('Select', '#category', 'Provider Licensing'),
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

        process = UI(override)
        process.update(runtime)
        order = ('category', 'template', 'waitBoard', 'board', 'find',
                 'waitResult', )
        process.execute(order)
