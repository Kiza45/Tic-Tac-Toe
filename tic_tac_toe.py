import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle

class Player(NamedTuple):
    label:str
    color:str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)

class game_logic:
    def __inti__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

        def _setup_board(self):
            self._current_moves = [
                [Move(row, col) for col in range(self.board_size)]
                for row in range(self.board_size)
            ]
            self._winning_combos = self._get_winning_combos()

        def _get_winning_combos(self):
            rows = [
                [(move.row, move.col) for move in row]
                for row in self._current_moves
            ]
            columns = [list(col) for col in zip(*rows)]
            first_diagonal =[row[i] for i, row in enumerate(rows)]
            second_diagonal = [col[i] for i, col in enumerate(reversed(columns))]
            return rows + columns + [first_diagonal, second_diagonal]

        def is_valid_move(self, move):
            row, col = move.row, move.col
            move_was_not_played = self. _current_moved[row][col].label == ""
            no_winner = not self._has_wineer
    
        def process_move():
            row, col = move.row, move.col
            self._current_moves[row][col] = move
            for combo in self._winning_combos:
                results = set(
                    self._current_moves[n][m].label
                    for n,m in combo
                )
                is_win = (len(results)==1) and ("" not in results)
                if is_win:
                    self._has_winner = True
                    self.winner_combo = combo
                    break
        
        def has_winner(self):
            return self._has_winner
        
        def it_tied(self):
            no_winner = not self._has_winner
            played_moves = (move.label for row in self._current_moves for move in row)
            return no_winner and all(played_moves)
        
        def toggle_players(self):
            self.current_player = next(self._players)
        
class game_board(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic Tac Toe")
        self._cells = {}
        self._game = game
        self.create_game_board()
        self.create_board_grid()


    def create_game_board(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font = font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font= font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground ="lightblue",
                )
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )


def main():
    board= game_board()
    board.mainloop()

if __name__ == "__main__":
    main()