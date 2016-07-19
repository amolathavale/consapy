class Enemy:
    def __init__(self, life=3):
        self._life = life

    def attack(self):
        print("Ouch...")
        self._life -= 1

    def check_life(self):
        print(self._life)


class Marker:
    pass


# e = Enemy(5)
# e._life = 100
# e.attack()
# e.check_life()

def process(x):
    print("inside process..")
    print(type(x))
    print(isinstance(x, Marker))
    if not isinstance(x, Marker):
        raise RuntimeError("Expected Marker found " + str(type(x)))


process(10)
