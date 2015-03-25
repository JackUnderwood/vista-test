__author__ = 'John Underwood'

from ui import UI
from ui.low.correspond import Correspond


class Corr10002(UI):
    Correspond()

    runtime = {
        'category': ('Select', '#category', 'Provider Licensing'),
        'template': ('Select', '#template_id', 'ECFMG request'),
        'waitBoard': ('Wait', 'board_id', 5),
        'board': (
            'Select',
            '#board_id',
            'American Board Of Anesthesiology - NC - Raleigh'
        ),
        'find': ('Find', '#desc_provider_id', 'marvin'),
        'waitResult': ('Wait', 'display_box_container', 5),
        'provider': ('Click', '//span[@item_id="402355"]', ''),
        # 'provider': ('Click', '//*[contains(., "Aaron Lessen")]', ''),
        # /doc/story/content//*[contains(., 'Yahoo')]
        # //*[@id="display_box_container"]/*[contains(., 'Aaron Campbell')]
        # '//*[@id="vsubnav"]/div/div[3]/ul/ul/li[@alt="System Documents"]',
        # //*[@id="243920"]    //*[@id="display_box_container"]

        # //*[@id="user_name"]
    }

    process = UI()
    process.update(runtime)
    order = ('category', 'template', 'waitBoard', 'board', 'find',
             'waitResult', )
    process.execute(order)
    # process.wait(5)
    # order = ('provider', )
    # process.execute(order)
    # process.wait(8)  # JNU!!! remove later
    process.teardown()
