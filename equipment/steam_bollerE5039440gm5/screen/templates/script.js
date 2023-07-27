function handleKeyPress(event, inputId, tag) {
  if (event.keyCode === 13) {
    event.preventDefault();
    var form = document.forms[0];
    var inputValue = document.getElementById(inputId).value;
    form.elements[tag].value = inputValue;
    form.submit();
  }
}
