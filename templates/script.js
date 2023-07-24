function handleKeyPress(event) {
            if (event.keyCode === 13) {
                event.preventDefault();
                document.forms[0].submit();
            }
        }