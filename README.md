# Tic-Tac-Doh!

A simple Microdot version of Tic-Tac-Toe. This is just a simple proof-of-
concept of how to make a simple multiplayer game through thsi interface.

Core game logic lives in `tictacotoe.py`. All input/output goes through the
pages hosted by the server via `__init.py__`. Similarly, there's a command line
version via `tictacto-cli.py` that uses the same underlying game logic as the
web-based version.

## Running

Copy [microdot.py](https://github.com/miguelgrinberg/microdot/blob/main/src/microdot/microdot.py)
into the same folder as this repository, and [simple.css](https://github.com/kevquirk/simple.css/blob/main/simple.css) 
into the `/static/css/` folder. Run this from the command line:

```sh
python3 __init__.py
```

## Libraries

[Microdot](https://github.com/miguelgrinberg/microdot/)

[SimpleCSS](https://github.com/kevquirk/simple.css)
