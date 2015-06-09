__author__ = 'John Underwood'

from ui import UI


class CorrSelections(UI):
    """
    Pre-requirement: needs to be on the Correspondence page -
    execute low.correspond first.

    Currently not in a fully working state, since adding new UI skin.
    """
    def __init__(self, override=None):
        super().__init__(override)

        runtime = {
            'category': ('Select', '#category', 'Provider Licensing'),
            'template': ('Select', '#template_id', 'License Renewal'),

            # override key 'providerLicense' value
            'providerLicense': ('Select', '#license_id', 'MD - P - D36976 - E'),
        }

        process = UI(override)
        process.update(runtime)
        order = ('category', 'template', 'providerLicense', )
        process.execute(order)
