from ui import UI
from tool.vlog import VLog

__author__ = 'John Underwood'


class Find(UI):
    """
    Types a inside Find... and selects a provider.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="FIND")
        log.info(" ======= Find... ======= ")

        runtime = {
            'entity': 'Matt Lambert st:wv',  # OVERRIDE
            'entityId': '91273',  # OVERRIDE
            'searchType': 'Provider',  # OVERRIDE
            'expand': (
                'Click',
                'css=body>header>nav>div>ul.left>li:nth-child(4)>div>div>'
                'div.find-form>i.vistatt.search-type.fa.fa-user-md.active'),
            'selectType': ('Click', '//*[@title="&searchType;"]'),
            'find': ('Type', '#main_desc', '&entity;'),
            'select': ('Click', '//*[@item_id="&entityId;"]'),
        }
        process = UI(override)
        process.update(runtime)
        order = ('expand', 'selectType', 'find', 'select', )
        process.execute(order)
