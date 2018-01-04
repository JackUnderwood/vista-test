from ui import UI
from ui.low.corr_template_creator import CorrTemplateCreator
from tool.generators.generator import gen_key

__author__ = 'John Underwood'


class SaveCorrTemplate(UI):
    """
    Save small changes to an existing correspond template on the 
    Create Template page.
    """
    CorrTemplateCreator()
    template_id = '16'  # License Renewal on test server has id of 16
    unique_key = gen_key(4)
    runtime = {
        'template': (
            'Click', '//*[@id="templatelist"]/li[{}]/div'.format(template_id, )),
        'subject': (
            'TypeAndTab',
            '#CorrespondenceTemplateEmailSubject',
            'License Renewal - VISTA {}'.format(unique_key, )),
        'save': ('Click', 'css=.waves-effect.waves-light.btn.template-save.'
                          'cyan.darken-3'),
    }
    expected = 'Saved Template'
    process = UI()
    process.update(runtime)
    process.execute(('template', 'subject', 'save',))
    process.results(expected, locator='toast-container')
    process.wait()
    process.teardown()
