class Player:
    def __init__(self, screen, player_x, player_y):
        self.screen = screen
        self.player_x = player_x
        self.player_y = player_y
        self.x_change = 0
        self.y_change = 0
        self.image = image

    def move(self, dice):
        pass

    def update(self):
        pass


class Table:
    def __init__(self):
        pass

    def show(self):
        pass


class Bit:
    def __init__(self, screen, index, image, bit_x, bit_y):
        self.screen = screen
        self.index = index
        self.image = image
        self.bit_x = bit_x
        self.bit_y = bit_y


class Dice:
    def __init__(self):
        pass

    def randDice(self):
        pass
