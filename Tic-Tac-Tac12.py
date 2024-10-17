import tkinter as tk
from tkinter import messagebox
import pygame

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Set the window size
        self.root.geometry("800x800")
        
        # Load the background image
        self.bg_image = tk.PhotoImage(file="C:/Users/User/Documents/tk_project/ticb.png")
        
        # Create a label to display the background image
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.player = 'X'
        self.board = [None] * 9
        self.buttons = [None] * 9
        
        # Configure grid to center the game board
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        
        self.create_board()
        
        self.turn_label = tk.Label(self.root, text=f"Player {self.player}'s turn", font=('normal', 20))
        self.turn_label.grid(row=4, column=1, columnspan=3, pady=20)
        
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=5, column=1, columnspan=3, pady=20)
        
        # Initialize pygame mixer
        pygame.mixer.init()
        self.cheer_sound = pygame.mixer.Sound("C:/Users/User/Documents/tk_project/winsound.wav")
        self.draw_sound = pygame.mixer.Sound("C:/Users/User/Documents/tk_project/drawsound.wav")
        self.background_music = "C:/Users/User/Documents/tk_project/gamemusic.wav"
        
        # Play background music in a loop
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely

    def create_board(self):
        for i in range(9):
            self.buttons[i] = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                        command=lambda i=i: self.on_button_click(i))
            self.buttons[i].grid(row=i//3+1, column=i%3+1, padx=10, pady=10)

    def on_button_click(self, index):
        if self.buttons[index]['text'] == "" and self.check_winner() is False:
            self.buttons[index]['text'] = self.player
            self.buttons[index]['fg'] = 'red' if self.player == 'X' else 'blue'
            self.board[index] = self.player
            if self.check_winner():
                self.flash_winner()
                pygame.mixer.music.stop()  # Stop background music
                self.cheer_sound.play()
                self.root.after(1000, lambda: self.show_winner_popup())
            elif None not in self.board:
                pygame.mixer.music.stop()  # Stop background music
                self.draw_sound.play()
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                self.turn_label.config(text=f"Player {self.player}'s turn")

    def check_winner(self):
        self.win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                               (0, 3, 6), (1, 4, 7), (2, 5, 8),
                               (0, 4, 8), (2, 4, 6)]
        for condition in self.win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] and self.board[condition[0]] is not None:
                self.winning_condition = condition
                return True
        return False

    def flash_winner(self):
        self.flashing = True
        self.flash_state = True
        self.flash()

    def flash(self):
        if not self.flashing:
            return
        color = 'lightgreen' if self.flash_state else 'SystemButtonFace'
        for index in self.winning_condition:
            self.buttons[index].config(bg=color)
        self.flash_state = not self.flash_state
        self.root.after(500, self.flash)

    def show_winner_popup(self):
        messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
        self.flashing = False

    def reset_game(self):
        self.player = 'X'
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text="", bg='SystemButtonFace', fg='black')
        self.turn_label.config(text=f"Player {self.player}'s turn")
        self.flashing = False
        pygame.mixer.music.play(-1)  # Restart background music

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()