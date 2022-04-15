from move import Move
from random import choice
class Player:
    PLAYER='O'
    COMPUTER='X'
    def __init__(self,is_player=True):
        self._is_player=is_player
        if self._is_player:
            self._marker=Player.PLAYER

        else:
           self._marker=Player.COMPUTER


    @property
    def is_player(self):
        return self._is_player


    @property
    def marker(self):
        return self._marker


    def get_move(self):
        if self._is_player:
            return self.get_player_move()
        else:
            return self.get_computer_move()

    def get_player_move(self):
        while True:
            user_input=int(input('enter your move '))
            move=Move(user_input)
            if move.is_valid():
                break
            else:
                print('please enter a valid input')
        return move

    def get_computer_move(self):
        random_choise=choice(list(range(1,10)))
        move=Move(random_choise)
        print(f'comp chosed {move.value}')
        return move







