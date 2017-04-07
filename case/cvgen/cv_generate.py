from ui import UI
from ui.low.file_cvgen import FileCvGen
from tool.generators.generator import gen_key

__author__ = 'John Underwood'


class CvGenerate(UI):
    """
    Prerequisite: requires the creation of templates
    Use the first available template, and generate the new CV file.
    """
    FileCvGen()
    file_name = "auto_" + gen_key(6)
    provider = {'name': 'Bertolozzi', 'id': '567754'}

    runtime = {
        'search': ('Type', '#cv_provider_desc', provider),
        'select': ('Click', '//*[@item_id="91273"]', ),
    }
