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
        'search': ('Type', '#cv_provider_desc', provider['name']),
        'select': ('Click', '//*[@item_id={}]'.format(provider['id']), ),
        'template': ('Select', '#template_id', 'General'),
        'filter': ('Click', '#filterCv', ),
    }
    expected = 'CV Data Filter'

    process = UI()
    order = ('search', 'select', 'template', 'filter')
    process.update(runtime)
    process.execute(order)

    process.wait(1)
    process.results(expected)

    # Issue with randomized, unique IDs, i.e. id="displayContent_1491921184009"
    # Solution is to spy for some unique attribute, in this case, compound class.
    # Note: this example uses css; may also spy for attribute using xpath:
    # //*[@class='drawer z-depth-1 displayContentInline displayContentContainer']
    locator = process.spy(
        'css=.drawer.z-depth-1.displayContentInline.displayContentContainer',
        'id')  # get the id value "displayContent_1491919464910"
    runtime.update({
        'email': ('Click', '//*[@id="{}"]/div/table/tbody[3]/tr/td[1]/label'.
                  format(locator, ), ),
        # //*[@id="displayContent_1491921184009"]/div/table/tbody[3]/tr/td[1]/label
        'address': ('Click', '//*[@id="{}"]/div/table/tbody[4]/tr/td[1]/label'.
                    format(locator, ), ),
        'phone': ('Click', '//*[@id="{}"]/div/table/tbody[5]/tr/td[1]/label'.
                  format(locator, ), ),
        'edu1': ('Click', '//*[@id="{}"]/div/table/tbody[6]/tr[2]/td[1]/label'.
                 format(locator, ), ),
        'edu2': ('Click', '//*[@id="{}"]/div/table/tbody[6]/tr[3]/td[1]/label'.
                 format(locator, ), ),
        'edu3': ('Click', '//*[@id="{}"]/div/table/tbody[6]/tr[4]/td[1]/label'.
                 format(locator, ), ),
        'exp1': ('Click', '//*[@id="{}"]/div/table/tbody[7]/tr[3]/td[1]/label'.
                 format(locator, ), ),
        'exp2': ('Click', '//*[@id="{}"]/div/table/tbody[7]/tr[20]/td[1]/label'.
                 format(locator, ), ),
        'selectAllLicenses': ('Click',
                              '//*[@id="{}"]/div/table/tbody[8]/tr[1]/td[3]/a'.
                              format(locator, ), ),
        'generate': ('Click', '#cvGenerate', ),
    })
    process.update(runtime)
    order = ('email', 'address', 'phone', 'edu1', 'edu2', 'edu3',
             'exp1', 'exp2', 'selectAllLicenses', 'generate')
    process.execute(order)

    runtime.update({  # should not need to 'type and tab'; reported bug
        'filename': ('TypeAndTab', '#cvgen_name', file_name),
        'saveAs': ('Click', '#saveCvAs', )
    })
    process.update(runtime)
    order = ('filename', )
    process.execute(order)
    process.wait(1)

    order = ('saveAs', )
    process.execute(order)
    process.results('New CV Saved')

    process.wait(1)
    process.results(file_name)
    process.wait(1)
    process.teardown()
