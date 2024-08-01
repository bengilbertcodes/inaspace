/*!
* Start Bootstrap - Bare v5.0.9 (https://startbootstrap.com/template/bare)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/


// to handle timer for django messages
document.addEventListener('DOMContentLoaded', function() {
    var timeoutDuration = 3500; 

    // Select all message boxes
    var messageBoxes = document.querySelectorAll('.message-box');

    // Loop through message boxes and set the timeout
    messageBoxes.forEach(function(box) {
        setTimeout(function() {
            // Use Bootstrap's JavaScript to fade out the alert
            $(box).alert('close');
        }, timeoutDuration);
    });
});
