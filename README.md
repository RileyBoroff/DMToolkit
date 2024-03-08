# DNDInitiativeTracker

This is a basic tool for tracking initiative, armor class, status effects, and health for Dungeons and Dragons 5th edition.

## Install

```
git clone https://github.com/RileyBoroff/DMToolkit.git
```

Open the folder and allow `Tracker.py` permission to run.

### Linux

```
cd 'path to folder'/DMToolkit
sudo chmod +x Tracker.py
```

### Running the program

```
python3 Tracker.py
```

## Options

Simply type one of these commands and press enter to perform the desired action:

- `h` or `help`: Displays the help menu.
- `exit`: Exits the program.
- `d`: Prompts for a name of what you want to damage then how much damage.
- `n`: Moves the indicator to the next item in the order.
- `+`: Adds a new item to the current turn order.
- `-`: Takes an item away from the current turn order.
- `s`: Add a status effect to an item in the turn order.
- `s-`: Remove a status effect from an item in the turn order.
