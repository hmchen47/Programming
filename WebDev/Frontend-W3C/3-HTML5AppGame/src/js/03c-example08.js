function drop(target, event) {
    event.preventDefault();
    target.innerHTML = event.dataTransfer.getData('text/plain');
};