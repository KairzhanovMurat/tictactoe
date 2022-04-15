

class Board:

    EMPTY_CELL=0
    def __init__(self):
        self.game_board=[[0,0,0],
                         [0,0,0],
                         [0,0,0]]
    def print_board(self):
        print('\nThe board')
        self.board_with_positions()

        for x in self.game_board:
            print('|',end='')
            for y in x:
                if y==Board.EMPTY_CELL:
                    print(' |',end='')
                else:
                    print(f'{y}|',end='')
            print()
        print()



    def board_with_positions(self):
        print('|1|2|3|\n|4|5|6|\n|7|8|9|')

    def submit_move(self,player,move):
        row=move.get_row()
        col=move.get_column()
        val=self.game_board[row][col]
        if val==Board.EMPTY_CELL:
            self.game_board[row][col]=player.marker
        else:
            print('this position is already taken')

    def check_game_over(self,player,l_move):
        return ((self.check_row(player,l_move))or
               (self.check_column(player,l_move))or
               (self.check_diag(player))or
               (self.check_antidiag(player)))

    def check_row(self,player,l_move):
        row_index=l_move.get_row()
        board_index=self.game_board[row_index]
        return board_index.count(player.marker)==3

    def check_column(self,player,l_move):
        count=0
        col_idx=l_move.get_column()
        for i in range(3):
            if self.game_board[i][col_idx]==player.marker:
                count+=1
        return count==3

    def check_diag(self,player):
        count=0
        for i in range(3):
            if self.game_board[i][i]==player.marker:
                count+=1
        return count==3

    def check_antidiag(self,player):
        count=0
        for i in range(3):
            if self.game_board[i][2-i]==player.marker:
                count+=1
        return count==3

    def check_tie(self):
        count=0
        for i in self.game_board:
            count+=i.count(Board.EMPTY_CELL)
        return count==0

    def reset_board(self):
        self.game_board=[[0,0,0],
                         [0,0,0],
                         [0,0,0]]








