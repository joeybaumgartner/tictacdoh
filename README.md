# Tic-Tac-Doh!

A simple Microdot version of Tic-Tac-Toe. This is just a simple proof-of-
concept of how to make a simple multiplayer game through thsi interface.

Core game logic lives in `tictacdoh.py`. All input/output goes through the
pages hosted by the server via `main.py`. Similarly, there's a command line
version via `tictacdoh-cli.py` that uses the same underlying game logic as the
web-based version.

## Running

Clone this repository, and create a folder called `microdot` within it. Copy [microdot.py](https://github.com/miguelgrinberg/microdot/blob/main/src/microdot/microdot.py), and [websocket.py](https://github.com/miguelgrinberg/microdot/blob/main/src/microdot/websocket.py)
into this folder of the repository, and [simple.css](https://github.com/kevquirk/simple.css/blob/main/simple.css) 
into the `/static/css/` folder. Run this from the command line:

```sh
python3 main.py
```

## Libraries

[Microdot](https://github.com/miguelgrinberg/microdot/)

[SimpleCSS](https://github.com/kevquirk/simple.css)
