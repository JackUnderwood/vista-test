from ui import UI

__author__ = 'John Underwood'


class SalesCommissionRates(UI):
    """
    Click on the Sales | Manage Commission Rates link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': self.SALES,
            'sales': ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {  # rates
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[3]/a'}
                 ),
            ]),
        }

        process = UI(override)
        process.update(runtime)
        order = ('sales', )
        process.execute(order)
