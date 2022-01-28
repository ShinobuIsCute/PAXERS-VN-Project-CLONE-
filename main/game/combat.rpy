$actionNumber = 0
python:
    class Unit:

        def __init__(self, hp, ad)
            self.hp = none
            self.attacks = none

        def attack(self,target)
            target.hp = target.hp - self.ad



mch = Unit(25, 3)
golem = Unit(20,2)
label ComCho:
    while actionNumber == 0:
        menu:
            "Attack":
                call attCho

            "Spells":
                call speCho

            "Backpack":
                call bacCHo

            #Not entirely sure what we should have as the fourth combat option yet.
            "Defend":
                call defCho
    return

label attCho:
    menu:

    return
label speCho:
    "WIP, sorry!"
    return
label bacCho:
    "WIP, sorry!"

    return
label defCho
    "WIP, sorry!"

    return
