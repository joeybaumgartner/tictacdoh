async function playerTurn(data) {

    try {
        payload = { "location": data, "token": getCookies().token };
        const response = await fetch('/play', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            redirect: "follow",
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if(!result.redirect_url) {
            setGameBoardData(result);
        }
        else {
            location.href = result.redirect_url
        }
    }
    catch (error) {
        console.error("Error:", error);
    }
}

function setGameBoardData(data) {
    document.querySelector('#player_name').innerHTML = data.player_name;
    document.querySelector('#player_mark').innerHTML = data.player_mark;
    document.querySelector('#alert_message').innerHTML = data.alert_message;

    if(data.alert_message) {    
        document.querySelector('#alert_message').classList.add("notice");
    }
    else {
        document.querySelector('#alert_message').classList.remove("notice");
    }

    for(var i = 0; i < 9; ++i) {
        document.querySelector('#board_' + i).innerHTML = data.board[i];
    }

    //document.getElementById("token").value = data.token
}

async function getGameStatus() {
    const response = await fetch('/gameStatus');
    const result = await response.json();

    if(result) {
        setGameBoardData(result);

        if(result.win_state >= 0) {
            location.href = "/win"
        }
    }
}

function getCookies() {
    cookies = document.cookie.split(';').map(item => item.split('=')).reduce((acc, [k, v]) => (acc[k.trim().replace('"', '')] = v) && acc, {});

    return cookies;
}