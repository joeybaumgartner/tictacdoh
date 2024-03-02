async function updateBoard() {
    const response = await fetch('/board');
    const data = await response.json();

    for(var i = 0; i < 9; ++i) {
        document.querySelector('#board_' + i).innerHTML = data[i]
    }
}