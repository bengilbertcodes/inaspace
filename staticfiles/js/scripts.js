/*!
* Start Bootstrap - Bare v5.0.9 (https://startbootstrap.com/template/bare)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/

document.addEventListener('DOMContentLoaded', function () {
		function reorderFields() {
			if (window.innerWidth < 768) {
				// Small screen
				const order = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']; // Custom order for small screens
				order.forEach(function (fieldName) {
					const element = document.querySelector(`.form-field[data-field="${fieldName}"]`);
					if (element) {
						document.querySelector('#left-column').appendChild(element);
					}
				});
			} else {
				// Large screen, reset order
				const leftColumnFields = ['email', 'first_name', 'password1'];
				const rightColumnFields = ['username', 'last_name', 'password2'];
				leftColumnFields.forEach(function (fieldName) {
					const element = document.querySelector(`.form-field[data-field="${fieldName}"]`);
					if (element) {
						document.querySelector('#left-column').appendChild(element);
					}
				});
				rightColumnFields.forEach(function (fieldName) {
					const element = document.querySelector(`.form-field[data-field="${fieldName}"]`);
					if (element) {
						document.querySelector('#right-column').appendChild(element);
					}
				});
			}
		}

		window.addEventListener('resize', reorderFields);
		reorderFields(); // Initial call
	});

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

$(document).ready(function () {
	// Custom date sorting plugin
	$.fn.dataTable.ext.type.order['date-dd-mmm-yyyy-pre'] = function (d) {
		var parts = d.split(' ');
		var day = parts[0];
		var month = parts[1];
		var year = parts[2];
		var months = {
			"Jan": "01",
			"Feb": "02",
			"Mar": "03",
			"Apr": "04",
			"May": "05",
			"Jun": "06",
			"Jul": "07",
			"Aug": "08",
			"Sep": "09",
			"Oct": "10",
			"Nov": "11",
			"Dec": "12"
		};
		return Date.parse(year + '-' + months[month] + '-' + day);
	};
	
	// Check if DataTable is already initialized
	if (!$.fn.DataTable.isDataTable('#bookings-table')) {
		// Initialize DataTable
		$('#bookings-table').DataTable({
			"columnDefs": [
					{ "type": "date-dd-mmm-yyyy", "targets": 1 },
					{ "orderable": false, "targets": [3, 4] }
				],
				"order": [[1, 'asc']]
			});
		}
	});

$(document).ready(function () {
    // Initialize time pickers
    $('#id_start_time').timepicker({
        'timeFormat': 'H:i',
        'step': 15,
        'minTime': '08:00',
        'maxTime': '21:45'
    });

    $('#id_end_time').timepicker({
        'timeFormat': 'H:i',
        'step': 15,
        'minTime': '08:15',
        'maxTime': '22:00'
    });

    // Set end_time default to start_time + 1 hour
    $('#id_start_time').on('changeTime', function () {
        var startTime = $(this).timepicker('getTime');
        if (startTime) {
            var endTime = new Date(startTime.getTime() + 60 * 60 * 1000); // add 1 hour
            $('#id_end_time').timepicker('setTime', endTime);
        }
    });

    // Ensure date cannot be in the past
    $('#id_date').on('change', function () {
        var selectedDate = new Date($(this).val());
        var today = new Date();
        today.setHours(0, 0, 0, 0); // Set today's date to midnight

        if (selectedDate < today) {
            alert('Date cannot be in the past');
            $(this).val('');
        }
    });
});
