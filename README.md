# tictactoe
- A custom tic tac toe game in Python.
- The board can be 3x3, 3x4, 3x5, 4x3, 4x4, 4x5, 5x3, 5x4 and 5x5. 
- Difficulty ranges from 0-5 with additional hint options for the player.

#### How to run:
1. Download the `.py` files in a local repository.
2. `cd` to this local repository from the command line.
3. Run `python3 tictactoe.py <rows> <cols> <difficulty> <piece> <-h or -a>` where
- `<rows>` is the number of rows on the board; should be 3, 4, or 5.
- `<cols>` is the number of columns on the board; should be 3, 4, or 5.
- `<difficulty>` is the computer opponent’s difficulty. It can be either 0 for random moves, 1 for an immediate
win, 2 for the opponent looking ahead 1 move, 3 for look-ahead 2 moves and 4 for look-ahead to the end
of the game (option 4 is only available for 3x3 boards).
- `<piece>` is either X or O
- `<-h>` is an optional flag that enables your program’s hint feature, which tells the human player where to
play next.
- `<-a>` is an optional flag that enables an advanced hint feature (instead of -h), which indicates to the
human player the location of the best possible move.
