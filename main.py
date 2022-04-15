
from player import Player
from  board import Board

class Game:
    def start(self):
        print('Hello, welome to Tic Tac Toe')


        player=Player()
        computer=Player()
        board=Board()

        board.print_board()

        while True:


            while True:
                plr_move=player.get_move()
                board.submit_move(player,plr_move)
                board.print_board()
                if board.check_tie():
                    print('its a tie!')
                    break
                elif board.check_game_over(player,plr_move):
                    print('You won! Congratulations!')
                    break
                else:
                    comp_move=computer.get_move()
                    board.submit_move(computer,comp_move)
                    board.print_board()
                    if board.check_game_over(computer,comp_move):
                        print('You lost, comp won...')
                        break
            user_input=input('Hello, do you want to play? X-yes,O-no. ').upper()
            if user_input=='O':
                print('OK,good bye!')
                break
            elif user_input=='X':
                print('Ok,lets go')
                self.start_new_round(board)
            else:
                print('lets start anyway))')
                self.start_new_round(board)

    def start_new_round(self,board):
        print('New round')
        board.reset_board()
        board.print_board()

game=Game()
game.start()




