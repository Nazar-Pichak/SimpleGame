import tkinter
from random import choice
from time import sleep

# The game is based on inheritance from builtin module GUI Tkinter.
# Some additional methods were created by me and with help of one participant from beginner's platform. 

class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        self.window = window
        super().__init__(window, width=300, height=300, bg='yellow')
        self.state = [None, None, None, None, None, None, None, None, None]
        self.bind('<Button-1>', self.click )
        self.game_is_running = True
        self.wins_x = 0
        self.wins_o = 0
        self.draw = 0

# This method is bound with method 'end_game' and together they define winner. 

    def get_winner(self):
        self.variants = []
        
        for i, j in enumerate(range(0, 9, 3)):
            self.variants.append(self.state[j:j + 3])
            self.variants.append(self.state[i::3])

        self.variants.append(self.state[::4])
        self.variants.append(self.state[2:7:2])
        
        if ['x', ] * 3 in self.variants:
            self.delete('all')
            message = self.create_text(140, 140, text='X-player won', fill='black', font=('Arial', 25))
            self.create_rectangle(10, 10, 290, 290, width=5, outline='darkgreen')
            self.update()
            self.delete('all')
            sleep(2)
            self.delete(message)
            self.end_game()
            self.game_is_running = False    
            
        elif ['o', ] * 3 in self.variants:
            self.delete('all')
            message = self.create_text(140, 140, text='Bot-player won', fill='black', font=('Arial', 25))
            self.create_rectangle(10, 10, 290, 290, width=5, outline='darkgreen')
            self.update()
            self.delete('all')
            sleep(2)
            self.delete(message)
            self.end_game()
            self.game_is_running = False
              
        elif None not in self.state:
            self.delete('all')
            message = self.create_text(140, 140, text='Nobody won', fill='black', font=('Arial', 30))
            self.create_rectangle(10, 10, 290, 290, width=5, outline='darkgreen')
            self.update()
            self.delete('all')
            sleep(2)
            self.delete(message)
            self.end_game()
            self.game_is_running = False

# This method is for creating mark 'O' of bot steps.   
            
    def add_o(self, column, row):
        column = (column * 100) + 50
        row = (row * 100) + 50
        r = 30
        self.create_oval(column-r, row-r, column+r, row+r, width=5, outline='red')

# This method is for creating mark 'X' of player steps.

    def add_x(self, column, row):
        column = (column * 100) + 50
        row = (row * 100) + 50
        r = 30
        self.create_line(column-r, row-r, column+r, row+r, fill='blue', width=5)
        self.create_line(column-r, row+r, column+r, row-r, fill='blue', width=5)

# This method is for creating grid on the canvas and drawing lines.

    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill='grey')
        self.create_line(200, 0, 200, 300, fill='grey')
        self.create_line(300, 100, 0, 100, fill='grey')
        self.create_line(300, 200, 0, 200, fill='grey')
        self.create_rectangle(0, 0, 300, 300, width=15, outline='darkgreen')

# This method is bound with method 'add_o' to get steps from the bot and find the best variants for the next steps. 

    def bot_move(self):
        o_is_None = [o for o, el in enumerate(self.state) if el is None]
        wins =  (['o','o'], ['x','x'])
        try:
            for i in wins:

                if self.state[:2] == i and self.state[2] is None :
                    index = 2
                    break
                elif self.state[3:5] == i and self.state[5] is None:
                    index = 5
                    break
                elif self.state[6:8] == i and self.state[8] is None:
                    index = 8
                    break
                elif self.state[0:4:3] == i and self.state[6] is None:
                    index = 6
                    break
                elif self.state[1:5:3] == i and self.state[7] is None:
                    index = 7
                    break
                elif self.state[2:6:3] == i and self.state[8] is None:
                    index = 8
                    break
                elif self.state[0:5:4] == i and self.state[8] is None:
                    index = 8
                    break
                elif self.state[2:5:2] == i and self.state[6] is None:
                    index = 6
                    break
                elif self.state[4:9:4] == i and self.state[0] is None:
                    index = 0
                    break
                elif self.state[4:7:2] == i and self.state[2] is None:
                    index = 2
                    break
                elif self.state[0:9:8] == i and self.state[4] is None or self.state[2:7:4] == i and self.state[4] is None or self.state[1:8:6] == i and self.state[4] is None or self.state[3:6:2] == i and self.state[4] is None:
                    index = 4
                    break
                elif self.state[1:3] == i and self.state[0] is None:
                    index = 0
                    break
                elif self.state[4:6] == i and self.state[3] is None:
                    index = 3
                    break
                elif self.state[7:9] == i and self.state[6] is None:
                    index = 6
                    break
                elif self.state[0:7:6] == i and self.state[3] is None:
                    index = 3
                    break
                elif self.state[2:9:6] == i and self.state[5] is None:
                    index = 5
                    break
                elif self.state[4:8:3] == i and self.state[1] is None:
                    index = 1
                    break
                elif self.state[0:3:2] == i and self.state[1] is None:
                    index = 1
                    break
                elif self.state[6:9:2] == i and self.state[7] is None:
                    index = 7
                    break
                elif self.state[3:7:3] == i and self.state[0] is None:
                    index = 0
                    break
                elif self.state[5:9:3] == i and self.state[2] is None:
                    index = 2
                    break
                elif self.state[4] is None:
                    index = 4
    
                elif self.state[0] is None:
                    index = 0
    
                elif self.state[2] is None:
                    index = 2
    
                elif self.state[6] is None:
                    index = 6
    
                elif self.state[8] is None:
                    index = 8
    
                else:
                    index = choice(o_is_None)
            
        
            self.state[index] = 'o'
            self.add_o(index % 3, int(index / 3))

# Small exception handling if all cells are drawn.

        except IndexError:
            self.delete('all')
            message = self.create_text(140, 140, text='Drawn all cells', fill='black', font=('Arial', 25))
            self.create_rectangle(10, 10, 290, 290, width=5, outline='darkgreen')
            self.update()
            sleep(2)
            self.delete(message)

# This method is bound with methods: 'restart_game', 'add_x', 'bot_move', 'get_winner'. The main functionality is getting steps from player.

    def click(self, event):
        if self.game_is_running is False:
            self.restart_game()
        elif self.game_is_running is True:
            column = int(event.x / 100)
            row = int(event.y / 100)
            index = row * 3 + column
            if self.state[index] is None:
                self.state[index] = 'x'
                self.add_x(column, row)
                self.update()
                sleep(1)
                self.bot_move()
                self.get_winner()

# This method is for creating the text and the next instructions for player.

    def end_game(self):
        self.create_text(150, 260, text='Click to start a new game', fill='darkblue', font=('Arial', 15))
        self.create_rectangle(10, 10, 290, 290, width=5, outline='darkgreen')
        if ['x',] * 3 in self.variants:
            self.wins_x += 1
        elif ['o',] * 3 in self.variants:
            self.wins_o += 1
        elif None not in self.state:
            self.draw += 1
        self.create_text(150, 60, text=f'X-score - {self.wins_x}', fill='black', font=('Arial', 25))
        self.create_text(150, 100, text=f'O-score - {self.wins_o}', fill='black', font=('Arial', 25))
        self.create_text(150, 140, text=f'Draw-score - {self.draw}', fill='black', font=('Arial', 25))
        if self.wins_x > self.wins_o:
            self.create_text(150, 200, text='Try to win now cheater', fill='red', font=('Arial', 15))
            self.create_text(150, 60, text=f'X-score - {self.wins_x}', fill='black', font=('Arial', 25))
            self.create_text(150, 100, text=f'O-score - {self.wins_o}', fill='black', font=('Arial', 25))
            self.create_text(150, 140, text=f'Draw-score - {self.draw}', fill='black', font=('Arial', 25))        

# This method is for restarting game if somebody won.

    def restart_game(self):
        self.delete('all')
        self.draw_lines()
        self.state = [None,] * 9
        self.update()
        self.game_is_running = True
        if self.wins_x > self.wins_o:
            self.bot_move()
            
window = tkinter.Tk()
window.title('Game TicTacToe')
window.resizable(False, False)


game = TicTacToe(window)
game.draw_lines()
game.pack()

if __name__ == '__main__':
    game.mainloop()