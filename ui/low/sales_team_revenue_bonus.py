from ui import UI

__author__ = 'John Underwood'


class SalesTeamRevenueBonus(UI):
    """
    Click on the Sales | Manage Team Revenue Bonus link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': self.SALES,
            'hover': ('Hover', '#slide-out'),
            'sales': ("Chain", [
                ('move_to_element', {
                    'to_element': '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element': '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {  # bonus
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[5]/a'}
                 ),
            ]),
        }

        process = UI(override)
        process.update(runtime)
        order = ('hover', 'sales', )
        process.execute(order)
