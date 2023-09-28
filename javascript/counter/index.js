
const resetButton = document.getElementById("reset");
const increaseButton = document.getElementById("increase");
const decreaseButton = document.getElementById("decrease");
const text = document.getElementById("text");

resetButton.onclick = reset;
increaseButton.onclick = increase;
decreaseButton.onclick = decrease;

let count = 0;
const varName = "Count : ";

function increase() {
    count++;
    text.innerHTML = varName + count;
}

function decrease() {
    count--;
    text.innerHTML = varName + count;
}

function reset() {
    count = 0;
    text.innerHTML = varName + count;
}

text.innerHTML = varName + count;
