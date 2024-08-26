# Chess.py
![Chess Game](https://github.com/Mcoder1538/Python-Projects-/blob/main/ChessusingTKinter/ChessUsingTkinter.png) <!-- Replace this URL with the actual URL of your project image -->

**Chess.py** is a Python-based chess game that provides a graphical interface for playing chess. It uses the `chess` library for game logic and Stockfish for AI moves, while the GUI is built using Tkinter.

## Features

- **Graphical User Interface (GUI)**: The game features a simple and intuitive GUI built with Tkinter, displaying an 8x8 chessboard with labels representing chess pieces.
- **Single Player Mode**: Play against the AI with adjustable difficulty levels (Easy, Medium, Hard).
- **Multiplayer Mode**: Allows two players to play against each other on the same computer.
- **AI Difficulty Levels**: Choose between Easy, Medium, and Hard difficulty for the AI opponent.
- **Board Color Customization**: Change the color scheme of the chessboard to match your preference.
- **Game Reset**: Easily reset the game to start a new match.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/chess.py.git
    cd chess.py
    ```

2. **Install the required Python packages**:
    Make sure you have Python installed. Then, install the required packages:
    ```bash
    pip install tkinter chess
    ```

3. **Download and Set Up Stockfish**:
    - Download Stockfish from [here](https://stockfishchess.org/download/).
    - Update the path to the Stockfish executable in your code:
      ```python
      self.engine = chess.engine.SimpleEngine.popen_uci("path/to/stockfish")
      ```
    Replace `"path/to/stockfish"` with the actual path to the Stockfish executable.

## Usage

1. **Run the Game**:
    ```bash
    python chess.py
    ```
   This will launch the Chess game window.

2. **Play the Game**:
   - Click on a piece to see its possible moves highlighted.
   - Click on a highlighted square to move the selected piece.
   - Use the menu options to switch between Single Player and Multiplayer modes, adjust AI difficulty, reset the game, or change board colors.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the existing coding style and document your changes.

## License

This project is licensed under the MIT License. See the [https://github.com/Mcoder1538/Python-Projects-/blob/main/LICENSE.md] file for details.
