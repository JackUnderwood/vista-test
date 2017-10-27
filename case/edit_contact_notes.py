from ui import UI

__author__ = 'John Underwood'


class EditContactNotes(UI):
    """ See TestRail test case C251 - Get to the Contact Notes panel
    Precondition
    1 - Click on Find... field in header, find a provider, and select
    2 - Close the Workspace
    Test case
    3 - Open the Workspace
    4 - Click on the Manage phone numbers icon.
    5 - Click on a row's phone number button.
    Expected: The Contact Notes drawer displays for provider from
    precondition's step 1.
    """
    res = []
    expected = {
        'provider': 'Matt Lambert st:wv',
        'providerId': '91273',
        'notes': 'Called and left a voicemail.',
        'feedback': 'Call Logged'
    }
    # //*[@id="lastFive"]/div/div[1]/div/div/div[4]
    # //*[@id="lastFive"]/div/div[3]/div/div/text()
    runtime = {
        'find': ('Type', '#main_desc', expected['provider']),
        'select': ('Click', '//*[@item_id="{}"]'.
                   format(expected['providerId'],)),
        'phone': ('Click',
                  '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[4]'),
        'contact': ('Click',
                    '//*[@id="phoneGrid_grid"]/tbody/tr[1]/td[4]/a/span'),
        'quick': ('Select', '//*[@class="cQuickNotes"]', 'Voicemail'),
        'save': ('Click', '//*[@button="save"]'),
        'comments': ('Click', '#viewLastFive'),
    }
    process = UI()
    process.update(runtime)
    order = ('find', 'select', 'phone', 'contact', )
    process.execute(order)

    process.wait()
    process.execute(('quick', 'save'))
    process.wait()
    res.append(process.results(expected['feedback']))
    process.execute(('contact', 'comments',))
    process.wait()
    inner = process.spy('//*[@id="lastFive"]/div/div[1]/div/div', 'innerHTML')
    res.append(expected['notes'] in inner)
    process.compare(True, all(res), message='list of results: {}'.format(res,))
    process.wait()
    process.teardown()
