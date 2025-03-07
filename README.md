# Tic-Tac-Doh!

A simple Microdot version of Tic-Tac-Toe. This is just a simple proof-of-
concept of how to make a simple multiplayer game through thsi interface.

Core game logic lives in `tictacdoh.py`. All input/output goes through the
pages hosted by the server via `main.py`. Similarly, there's a command line
version via `tictacdoh-cli.py` that uses the same underlying game logic as the
web-based version.

## Requirements

- This project uses SimpleNamespace which will require at least Python 3.3, but most
  testing has been done on Python 3.13.

## Running

Clone this repository, and create a folder called `microdot` within it, and copy the 
following files into the folder:

- [microdot.py](https://raw.githubusercontent.com/miguelgrinberg/microdot/refs/heads/main/src/microdot/microdot.py)
- [websocket.py](https://raw.githubusercontent.com/miguelgrinberg/microdot/refs/heads/main/src/microdot/websocket.py)
- [__init.py__](https://raw.githubusercontent.com/miguelgrinberg/microdot/refs/heads/main/src/microdot/__init__.py)
- [helpers.py](https://raw.githubusercontent.com/miguelgrinberg/microdot/refs/heads/main/src/microdot/helpers.py)

Copy [simple.css](https://github.com/kevquirk/simple.css/blob/main/simple.css) 
into the `/static/css/` folder. Run this from the command line:

```sh
python3 main.py
```

## External Libraries

[Microdot](https://github.com/miguelgrinberg/microdot/)

[SimpleCSS](https://github.com/kevquirk/simple.css)
