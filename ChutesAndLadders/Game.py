import random

'''
    The chutes and the ladders on the game board are represented by "jumps".  
    The dictionary contains k:v = old_position:new_position
'''
jumps = {
    1: 38,
    4: 13,
    9: 31,
    16: 6,
    21: 42,
    28: 84,
    36: 44,
    48: 26,
    49: 11,
    51: 67,
    56: 53,
    62: 19,
    64: 60,
    71: 91,
    80: 100,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}


def roll_die():
    return random.randint(1, 6)


class Game:
    def __init__(self, player_count):
        self._player_count = player_count
        self._player_pos = [0] * self._player_count
        self._turns = 0
        self._log = ''

    def reset(self):
        self._player_pos = [0] * self._player_count
        self._turns = 0
        self._log = ''

    def log(self, position, player_no):
        pass
        if player_no == 0:
            self._log += '|'
        self._log += str(position) + ' '

    def play_game(self):
        crnt_player = 0

        while True:
            x = roll_die()
            new_pos = self._player_pos[crnt_player] + x

            if new_pos in jumps:
                new_pos = jumps[new_pos]

            if new_pos == 100:
                self.log(100, crnt_player)
                break
            elif new_pos > 100:
                new_pos -= x

            self._player_pos[crnt_player] = new_pos
            self.log(new_pos, crnt_player)
            crnt_player += 1
            if crnt_player >= self._player_count:
                crnt_player = 0
                self._turns += 1

        # print(f'p{crnt_player} won in {self._turns} turns |{self._log}')
        return crnt_player




