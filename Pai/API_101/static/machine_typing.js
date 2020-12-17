const h1 = document.querySelector('h1');
const message = 'Hello World!'

letter = 0

function addLetter(){
    h1.textContent += message[letter];
    letter++;
    if(letter === message.length) clearInterval(index);
}

const index = setInterval(addLetter, 200);