from microdot import Microdot
from microdot import redirect
from microdot import send_file
from tictacdoh import TicTacDoh

app = Microdot()
game = TicTacDoh()

# Handler for all static content (CSS, JS, HTML, images, etc.)
@app.route('/static/<path:path>')
async def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path, max_age=1)

@app.get('/')
async def start(request):
    return send_file('static/start.html', max_age=1)

@app.post('/play')
async def post_play(request):

    if not game.game_started: 
        game.player = ((request.form.get('player_1_name')), (request.form.get('player_2_name')))
        game.start_game()
    else:
        location = int(request.form.get('location'))

        game.player_turn(location)

        win_state = game.check_for_win()

        if win_state != 2:
            return redirect(f'/win')
        
        game.next_turn()

    player_name = game.get_current_player_name()
    mark = game.mark[game.current_player_turn]

    html = ""
    with open('player.html') as f: html = f.read()

    html = html.format(player_name = player_name, board = game.board, player_mark = mark, alert_message = game.alert_message)
    
    #added game.alert_message, also a call to the var in player.html

    return html, 200, {'Content-Type': 'text/html'}

@app.get('/win')
async def win(request):
    
    html = ""
    with open('winner.html') as f: html = f.read()

    html = html.format(player_name = game.get_current_player_name())

    return html, 200, {'Content-Type': 'text/html'}

app.run(port=8080)