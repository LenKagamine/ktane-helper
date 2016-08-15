# Keep Talking and Nobody Explodes Bot

A voice controlled helper for the game Keep Talking and Nobody Explodes.

## Requirements

- [Python 3.x](https://www.python.org) with pip
- PyAudio 0.2.9+
- [Swig](http://www.swig.org)
- [Microsoft Visual Studio 2015](https://www.visualstudio.com)
- PocketSphinx (including language files)
- [espeak](http://espeak.sourceforge.net)

Python, Swig, Visual Studio, and espeak are available on their respective websites.

After installing Python and pip, run `pip install pyaudio` and `pip install pocketsphinx` to install PyAudio and PocketSphinx.

Run `python Main.py` to start the bot.

## Commands
Upon starting, the bot will calibrate the sensitivity for the speech recognition. It will best detect commands if there are only ambient noises during calibration.

After calibration comes the main menu. The user can select an option by saying a command:

- Defuse a module: `defuse <module name>`
- Setup the bomb: `bomb setup`
- Reset a module: `reset <module name>`

Running bomb setup will allow the user to input six variables about the bomb that may be needed when defusing a module. If bomb setup is not run, and a variable is required while defusing, the bot will simply ask for that variable before defusing.

The variables are: `parallel port` (`yes` = exists / `no` = doesn't exist), `FRK indicator` (Y/N, pronounced "freak"), `CAR indicator` (Y/N), the `last digit` of the serial number, a vowel in the serial number (`serial vowel`, Y/N), and the number of `batteries`.

Several modules are disarmed over multiple stages, such as Memory. To disarm subsequent stages, run the defuse command again. Often, if a mistake is made, the player will have to start from the first stage. In this case, a module can be reset using the reset command.

For a detailed description of each module and the steps to disarm them in the game, check out the [Bomb Defusal Manual](http://www.bombmanual.com).

### Wires
Say the colours of the wires from top to bottom (i.e. `red blue blue yellow`).

### The Button
Say the colour of the button followed by the text on the button (i.e. `yellow detonate`).

### Simon Says
Say `buttons`, then the colours of the buttons in the order they flash (i.e. `buttons blue blue red`).

### Memory
Say `display`, then the number in the big display, followed by the four button numbers from left to right (i.e. `display one one three four two`).

Other modules coming soon...
