import tkinter as tk
from tkinter import messagebox, Menu
import chess
import chess.engine
import threading
from tkinter.simpledialog import askstring

class ChessApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Game")
        self.geometry("600x600")
        self.board = chess.Board()
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.selected_piece = None
        self.possible_moves = []
        self.ai_difficulty = "Medium"
        self.single_player = False
        self.colors = ["gold" , "light gray"]  # Default color scheme
        self.create_board()
        self.create_menu()
        self.update_board()
        self.engine = chess.engine.SimpleEngine.popen_uci("C:/stockfish/stockfish/stockfish-windows-x86-64-avx2.exe")  # Update this path
    
    def create_board(self):
        for row in range(8):
            for col in range(8):
                color = self.colors[(row + col) % 2]
                square = tk.Label(self, bg=color, width=12, height=6, borderwidth=1, relief="solid")
                square.grid(row=row, column=col)
                square.bind("<Button-1>", lambda event, row=row, col=col: self.square_clicked(row, col))
                self.squares[row][col] = square
    
    def create_menu(self):
        menubar = Menu(self)
        self.config(menu=menubar)
        
        game_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        
        game_menu.add_command(label="Single Player", command=self.start_single_player)
        game_menu.add_command(label="Multiplayer", command=self.start_multiplayer)
        game_menu.add_command(label="Reset Game", command=self.reset_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.quit)
        
        ai_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="AI Difficulty", menu=ai_menu)
        
        ai_menu.add_command(label="Easy", command=lambda: self.set_ai_difficulty("Easy"))
        ai_menu.add_command(label="Medium", command=lambda: self.set_ai_difficulty("Medium"))
        ai_menu.add_command(label="Hard", command=lambda: self.set_ai_difficulty("Hard"))
        
        options_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=options_menu)
        
        options_menu.add_command(label="Change Board Color", command=self.change_board_color)

    def set_ai_difficulty(self, level):
        self.ai_difficulty = level
        messagebox.showinfo("AI Difficulty", f"AI Difficulty set to {level}")
    
    def start_single_player(self):
        self.single_player = True
        self.reset_game()
        messagebox.showinfo("Single Player", "Single Player mode started.")
    
    def start_multiplayer(self):
        self.single_player = False
        self.reset_game()
        messagebox.showinfo("Multiplayer", "Multiplayer mode started.")
    
    def reset_game(self):
        self.board.reset()
        self.update_board()
        self.selected_piece = None
        self.possible_moves = []
        messagebox.showinfo("Reset Game", "The game has been reset.")
    
    def update_board(self):
        for row in range(8):
           for col in range(8):
                piece = self.board.piece_at(chess.square(col, 7-row))
                text = self.get_piece_text(piece) if piece else ''
                self.squares[row][col].configure(text=text, font=("Arial", 6))

    
    def get_piece_text(self, piece):
        # Define the text to be displayed for each piece
        piece_symbol = piece.symbol()
        if piece_symbol == 'P':
            return 'Pawn'
        elif piece_symbol == 'p':
            return 'pawn'
        elif piece_symbol == 'R':
            return 'Rook'
        elif piece_symbol == 'r':
            return 'rook'
        elif piece_symbol == 'N':
            return 'Knight'
        elif piece_symbol == 'n':
            return 'knight'
        elif piece_symbol == 'B':
            return 'Bishop'
        elif piece_symbol == 'b':
            return 'bishop'
        elif piece_symbol == 'Q':
            return 'Queen'
        elif piece_symbol == 'q':
            return 'queen'
        elif piece_symbol == 'K':
            return 'King'
        elif piece_symbol == 'k':
            return 'king'
        return piece_symbol


    def square_clicked(self, row, col):
        square = chess.square(col, 7-row)
        piece = self.board.piece_at(square)
        
        if self.selected_piece is not None:
            self.clear_highlight()
            move = chess.Move(self.selected_piece, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.update_board()
                if self.single_player and self.board.turn == chess.BLACK:
                    self.perform_ai_move()
            self.selected_piece = None
            self.possible_moves = []
        else:
            if piece and (piece.color == self.board.turn):
                self.selected_piece = square
                self.highlight_moves(square)
    
    def perform_ai_move(self):
        def ai_move():
            with self.engine.analysis(self.board) as analysis:
                if self.ai_difficulty == "Easy":
                    limit = chess.engine.Limit(time=0.1)
                elif self.ai_difficulty == "Medium":
                    limit = chess.engine.Limit(time=0.5)
                else:  # Hard
                    limit = chess.engine.Limit(time=1.0)
                result = self.engine.play(self.board, limit)
                self.board.push(result.move)
                self.update_board()
        
        threading.Thread(target=ai_move).start()
    
    def clear_highlight(self):
        for row in range(8):
            for col in range(8):
                color = self.colors[(row + col) % 2]
                self.squares[row][col].configure(bg=color)
    
    def highlight_moves(self, square):
        self.possible_moves = [move.to_square for move in self.board.legal_moves if move.from_square == square]
        for move in self.possible_moves:
            row, col = 7-chess.square_rank(move), chess.square_file(move)
            self.squares[row][col].configure(bg="light yellow")
    
    def quit(self):
        self.engine.quit()
        self.destroy()

    def change_board_color(self):
            # Define color schemes for the chessboard
            classic_colors = ["gold", "light gray"]
            sea_colors = ["light blue", "light green"]

            # Prompt the user to select a color scheme
            self.change_board_color_title = tk.Toplevel(self.master)
            self.change_board_color_title.title("Enter Board Color")

            self.Color_change_text = tk.Label(self.change_board_color_title, text="Select a color scheme:\n1. Classic (c)\n2. Sea (s)")
            self.Color_change_text.pack()

            self.entry_color = tk.Entry(self.change_board_color_title)
            self.entry_color.pack(padx=10, pady=10)

            def change_color_of_board():
                color_choice = self.entry_color.get().strip().lower()
                if color_choice == "c":
                    self.colors = classic_colors
                elif color_choice == "s":
                    self.colors = sea_colors
                else:
                    messagebox.showwarning("Invalid Selection", "Please select a valid color scheme.")
                    return
                
                # Update the chessboard colors
                for row in range(8):
                    for col in range(8):
                        self.color = self.colors[(row + col) % 2]
                        self.squares[row][col].configure(bg=self.color)

            self.save_button = tk.Button(self.change_board_color_title, text="Save", command=change_color_of_board)
            self.save_button.pack(padx=10, pady=10)


if __name__ == "__main__":
    app = ChessApp()
    app.mainloop()
