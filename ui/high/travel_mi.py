__author__ = 'John Underwood'
from ui import UI


class TravelMiddleInitial(UI):
    """
    Pre-requirement: needs to be on the Travel's Provider Profile
    Case test goes to Provider Profile, changes Middle Initial.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'provider': ("Click", '//*[@id="vert-tabs"]/ul/li[1]/a', ""),
            'middleInitial': (
                "Click",
                '//*[@id="provider_profile_sub"]/div[2]/div[1]/label[3]/a', ""
            ),
            'enterMi': (
                "Type",
                '//*[@id="provider_profile_sub"]/div[2]/div[1]/label[3]/div/'
                'div[2]/div/form/div/div[1]/div[1]/input',
                'N'  # TODO: need to implement '__OVERRIDE__' for this value 'N'
            ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('provider', 'middleInitial', 'enterMi', )
        process.execute(order)

