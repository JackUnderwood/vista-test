from ui import UI

__author__ = 'John Underwood'


class SalesBase(UI):
    """
    Click on the Sales | Manage Sales Base link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': self.SALES,
            'sales': ("Chain", [
                ('move_to_element', {
                    'to_element': '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element': '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {  # base
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[4]/a'}
                 ),
            ]),
        }

        process = UI(override)
        process.update(runtime)
        order = ('sales', )
        process.execute(order)
