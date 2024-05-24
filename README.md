# Ascii Game Engine
This project is a "for fun" project to create code that can generate ascii
games from text files and directories. I got inspired to try it from a friend
without coding experience asking how to make an ASCII based text game. 

    _            _  _    ___                     ___              _            
   /_\   ___ __ (_)(_)  / __| __ _  _ __   ___  | __| _ _   __ _ (_) _ _   ___ 
  / _ \ (_-</ _|| || | | (_ |/ _` || '  \ / -_) | _| | ' \ / _` || || ' \ / -_)
 /_/ \_\/__/\__||_||_|  \___|\__,_||_|_|_|\___| |___||_||_|\__, ||_||_||_|\___|
                                                           |___/               

## Usage
The goal is to create an EXE file that creates the framework for a text based
game. That way a developer can focus on working out a decent story rather than
worrying about coding a framework for that story. The _Planned_ way to do this
is by having the code read in text files with each section of the game on a new
line. check out this [example](/example.txt) for the proposed layout. Each
choice in the game will lead to a new text file contaning the consicenses of
that desicions.

## Development Timeline
Feature 1: The basic features of the engine
    - ability to read in text files
    - ability to display them in a window
    - choice mechanic working
Feature 2: Ascii Art
    - the ability to display art in the engine
    - a tool (probably utilizing something like [this](https://github.com/OsciiArt/DeepAA))
    to turn digital assets into ascii art
Feature 3: Text Generation
    - a big maybe
    - use some small scale AI model to generate text for the game

## Misc
For any questions or ideas feel free to create an issue or to fork the repo.
This is a "for-fun" project so I feel no real need to limit the sharing of it.
