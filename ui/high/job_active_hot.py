from ui import UI

__author__ = 'John Underwood'


class JobActiveHot(UI):
    """
    Search for a Job Status of 'Active' and 'Hot'.
    """

    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'jobStatus': (
                'Click', 'css=.ui-multiselect.ui-widget.ui-state-default.'
                         'ui-corner-all.multi_s.multi_s_job_status'),
            'wait': ('Wait', '#ui-multiselect-s_job_status-option-1',
                     {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
            'jobStatusActive': (
                'Click', '#ui-multiselect-s_job_status-option-1'),
            'jobStatusHot': (
                'Click', '#ui-multiselect-s_job_status-option-4'),
        }
        process = UI(override)
        process.update(runtime)
        order = ('jobStatus', 'wait', 'jobStatusActive', 'jobStatusHot', )
        process.execute(order)
