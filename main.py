from microdot import Microdot
from microdot import redirect
from microdot import send_file
from tictacdoh import TicTacDoh
from registration import Registration
from player import Player
import json

app = Microdot()
game = TicTacDoh()
registration = Registration(2, 2)

# Handler for all static content (CSS, JS, HTML, images, etc.)
@app.route('/static/<path:path>')
async def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path, max_age=1)

@app.get('/')
async def start(request):
    return send_file('static/html/register.html', max_age=1)

@app.get('/canRegister')
async def can_register(request):
    register_state = {
        "can_register": registration.at_capacity() == False
    }
    return json.dumps(register_state), 200, { 'Content-Type': 'application/json'}

@app.get('/gameReady')
async def game_ready(request):
    ready_state = {
        "ready": registration.enough_to_start()
    }
    return json.dumps(ready_state), 200, { 'Content-Type': 'application/json' }

@app.post('/register')
async def register(request):
    @request.after_request
    def set_cookie_token(request, response):
        response.set_cookie('token', request.form.get("token"))
        return response
    
    print(f"registered users: {len(registration.players)}")

    register_state = {
        "registered": False,
        "reason": None,
        "token": ""
    }

    if registration.at_capacity():
        # Server is at capacity, don't allow any more registrations
        register_state["registered"] = False
        register_state["reason"] = "full"

        return json.dumps(register_state), 403, { 'Content-Type': 'application/json' }

    else:
        # Register a player
        name = request.form.get("player_name")

        mark = "X" if len(registration.players) == 0 else "O"

        player = Player(name, request.form.get("token"), mark)

        print(f"Player {player.name} has token {player.token}")

        registration.register_user(player)
        register_state["registered"] = True
        register_state["token"] = request.form.get("token")

    return json.dumps(register_state), 200, { 'Content-Type': 'application/json' }


def get_player_data() -> dict:
    player_name = game.get_current_player_name()
    mark = game.mark[game.current_player_turn]
    
    return {
        "player_name": player_name, 
        "player_mark": mark, 
        "alert_message": game.alert_message, 
        "board": game.board
    }

@app.route('/play', methods=['GET', 'POST'])
async def play(request):

    if request.method == 'GET':
        game.player = registration.players
        game.start_game()

        game_data = get_player_data()
        return send_file('static/html/player.html', max_age = 1)
    
    elif request.method == 'POST':

        location = int(request.json["location"])

        game.player_turn(location)

        win_state = game.check_for_win()

        if win_state >= 0:
            win_data = {
                "redirect_url": "/win"
            }
            return json.dumps(win_data), 200, {'Content-Type': 'application/json'}
        
        game.next_turn()

    game_data = get_player_data()

    return json.dumps(game_data), 200, {'Content-Type': 'application/json'}

@app.get('/currentPlayer')
async def current_player(request):

    win_state = game.check_for_win()

    data = {
        "token": registration.players[game.current_player_turn].token,
        "win_state": win_state
    }
    return json.dumps(data), 200, { 'Content-Type': 'application/json'}

@app.get('/win')
async def win(request):
    
    html = ""
    with open('static/html/winner.html') as f: html = f.read()

    html = html.format(player_name = game.get_current_player_name())

    return html, 200, {'Content-Type': 'text/html'}

@app.get('/reset')
async def reset(request):
    game.reset()
    return redirect('/')

@app.get('/gameStatus')
async def board(request):

    win_state = game.check_for_win()
    
    game_data = get_player_data()
    game_data["win_state"] = win_state

    return json.dumps(game_data), 200, {'Content-Type': 'application/json'}

app.run(port=8080)