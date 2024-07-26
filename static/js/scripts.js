/*!
* Start Bootstrap - Bare v5.0.9 (https://startbootstrap.com/template/bare)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


// To handle auto populate on end_time when user selects start_time
document.addEventListener('DOMContentLoaded', function() {
    const startTimeInput = document.querySelector('input[name="start_time"]');
    const endTimeInput = document.querySelector('input[name="end_time"]');

    startTimeInput.addEventListener('change', function() {
        const startTime = new Date(startTimeInput.value);
        if (startTime) {
            const endTime = new Date(startTime.getTime() + 60 * 60 * 1000); // Add 1 hour
            endTimeInput.value = endTime.toISOString().slice(0, 16); // Format to "YYYY-MM-DDTHH:MM"
        }
    });
});
