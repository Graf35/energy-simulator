//function handleKeyPress(event, inputId, tag) {
//  if (event.keyCode === 13) {
//    event.preventDefault();
//    var form = document.forms[0];
//    var inputValue = document.getElementById(inputId).value;
//    form.elements[tag].value = inputValue;
//    form.submit();
//  }
//}

function handleEnterKeyPress(event, inputId, formTag) {
  if (event.key === 'Enter') {

    event.preventDefault();
    const inputValue = document.getElementById(inputId).value;
    document.querySelector(formTag).value = inputValue;
    document.querySelector(formTag).submit();
  }
}
