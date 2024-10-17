import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = 'X'
        self.board = [None] * 9
        self.buttons = [None] * 9
        self.create_board()
        
        self.turn_label = tk.Label(self.root, text=f"Player {self.player}'s turn", font=('normal', 20))
        self.turn_label.grid(row=3, column=0, columnspan=3)
        
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3)

    def create_board(self):
        for i in range(9):
            self.buttons[i] = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                        command=lambda i=i: self.on_button_click(i))
            self.buttons[i].grid(row=i//3, column=i%3)

    def on_button_click(self, index):
        if self.buttons[index]['text'] == "" and self.check_winner() is False:
            self.buttons[index]['text'] = self.player
            self.board[index] = self.player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
                self.highlight_winner()
            elif None not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                self.turn_label.config(text=f"Player {self.player}'s turn")

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] and self.board[condition[0]] is not None:
                return True
        return False

    def highlight_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] and self.board[condition[0]] is not None:
                for index in condition:
                    self.buttons[index].config(bg='lightgreen')

    def reset_game(self):
        self.player = 'X'
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text="", bg='SystemButtonFace')
        self.turn_label.config(text=f"Player {self.player}'s turn")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()