function autoResizeTextarea() {
    const textInput = document.getElementById('textarea');
    const lines = textInput.value.split('\n').length;
    textInput.rows = Math.min(lines, 3);
}

document.getElementById('textarea').addEventListener('input', autoResizeTextarea);