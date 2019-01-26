# Keep Talking and Nobody Explodes Bot

A voice controlled helper for the game Keep Talking and Nobody Explodes.

## Requirements

- [Python 3.4+](https://www.python.org) with pip
  - [pyttsx3](https://pypi.org/project/pyttsx3/): text to speech
  - [PyAudio 0.2.9+](https://pypi.org/project/PyAudio/): audio (speech) recording
  - [PocketSphinx](https://pypi.org/project/pocketsphinx/): speech recognition

Running `pip install pyaudio pocketsphinx pyttsx3` should be enough, but consult their documentation for details.

Run `python Main.py` to start the bot.

### Troubleshooting

- Python 3.7 on Windows has issues with installing `pyaudio`. If you have trouble with this, try downgrading to Python 3.6 or check out [this issue](https://github.com/LenKagamine/ktane-helper/issues/2#issuecomment-457312606).
- If you encounter an error message like `No module named win32com.client`, install `pip install pypiwin32` as well. Read the [pyttsx3 docs](https://github.com/nateshmbhat/pyttsx3) for more details.

## How The Bot Listens

The bot uses PocketSphinx for speech recognition which can accept a grammar file when parsing speech. A grammar file describes the exact phrases that PocketSphinx will listen for. This greatly improves the accuracy of the speech recognition as it will only check for a few specified keywords rather than the entire English language. You can read more about grammars [here](https://cmusphinx.github.io/wiki/tutoriallm/#grammars).

Every time the bot listens for a command or information, it listens for a specific grammar provided by a grammar file in the `grammars/` directory.

The file `Speech.py` contains the `Speech` class which handles all of the speech related functionality of the bot, such as listening and speaking. The file itself should be abstract enough to use in your own projects. There are three main methods to consider:

- `calibrate(duration = 1)`: Take an audio sample to calibrate the threshold of the speech recognition.
  - `duration`: Length of the calibration in seconds.
- `listen(grammar = None)`: Listen for speech, parse it into text, and return it.
  - `grammar`: Filepath of the grammar file. If no file is specified, the speech recognition will try all English words.
- `say(text)`: Use text-to-speech to say the given text.

You can also customize the bot's speech by changing its voice, speech rate, and volume. Read more on [pyttsx3's docs](https://pyttsx3.readthedocs.io/en/latest/engine.html#changing-voices).

## Voice Commands

Upon starting, the bot will calibrate the sensitivity for the speech recognition for several seconds. It will best detect commands if there are only ambient noises during calibration.

After calibration comes the main menu. The user can select an option by saying a command:

- Defuse a module: `defuse <module name>`
- Setup the bomb: `bomb setup`
- Update number of strikes: `strikes <number of strikes>`
- Undo a module: `undo <module name>`
- Reset a module: `reset <module name>`
- Quit the bot: `exit` or `terminate`

## Bomb Setup

Running bomb setup will allow the user to input six variables about the bomb that may be needed when defusing a module. If bomb setup is not run, and a variable is required while defusing a module, the bot will simply ask for that variable before defusing.

The variables are:

- `parallel port` (`yes` = exists / `no` = doesn't exist)
- `FRK indicator` (Y/N, pronounced "freak")
- `CAR indicator` (Y/N, pronounced "car")
- the `last digit` of the serial number (e.g. `last digit even`, `last digit odd`, `last digit five`)
- a vowel in the serial number (`serial vowel`, Y/N)
- the number of `batteries` (e.g. `batteries none`, `batteries three`)

## Modules

Several modules are disarmed over multiple stages, such as Memory. To disarm subsequent stages, run the defuse command again. Often, if a mistake is made, the player will have to start from the first stage. In this case, a module can be reset using the reset command, e.g. `reset memory`. To reset only the most recent stage, use the undo command, e.g. `undo memory`.

Also, some modules are disarmed differently depending on the number of strikes on the bomb. If a strike happens, make sure to update the bot by saying `strikes` followed by the number of strikes, e.g. `strikes one`.

For a detailed description of each module and the steps to disarm them in the game, check out the [Bomb Defusal Manual](http://www.bombmanual.com).

### Wires

Say the colours of the wires from top to bottom (i.e. `red blue blue yellow`).

### The Button

Say the colour of the button followed by the text on the button (i.e. `yellow detonate`).

### Simon Says

Say `buttons`, then the colours of the buttons in the order they flash (i.e. `buttons blue blue red`).

### Memory

Say `display`, then the number in the big display, followed by the four button numbers from left to right (i.e. `display one one three four two`).

This module can be reset back to stage 1.

### Other Modules?

This project is no longer actively maintained. While I might address any issues with the bot, I won't be adding any more modules. If you want to contribute, submit a PR and I'll be happy to review it.
