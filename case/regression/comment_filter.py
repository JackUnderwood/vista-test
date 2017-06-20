import ui
from ui import UI

__author__ = 'John Underwood'


class CommentFilter(UI):
    """
    Search comments by using the Username filter.
    Regression test for #130662867 - "Comment - sys error and ajax error
    during filter"
    """
    ui.log.info("CommentFilter __init__() called")
    process = UI()

    runtime = {
        'find': ('Type', '#main_desc', 'lambert st:wv'),
        'select': ('Click', '//*[@item_id="91273"]'),
        'manage': ('Click',
                   '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[6]/i'),
    }
    process.update(runtime)
    order = ('find', 'select',)
    process.execute(order)
    process.wait()
    process.execute(('manage',))
    entry = process.spy('//*[@id="commentsGrid_grid"]/tbody/tr[1]/td[6]',
                        'innerHTML')
    expected = process.spy('//*[@id="commentsGrid_grid"]/tbody/tr/td', 'innerHTML')
    process.update({
        'username': ('Type', '//*[@id="commentsGrid_grid"]/tfoot/tr/th[6]/input',
                     entry)
    })
    process.execute(('username', ))
    actual = process.spy('//*[@id="commentsGrid_grid"]/tbody/tr/td', 'innerHTML')
    process.wait()
    result = process.compare(expected, actual, message='row\'s ID')
    process.wait()
    process.teardown()
