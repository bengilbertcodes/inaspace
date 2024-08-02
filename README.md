<img style="display: block; margin: auto; height: 100px;" src="docs/readme_images/inaspace_logo.webp" alt="inapsace logo"/> 
</br>

# inaspace:<br> 
#### A Simple Solution for Corporate Room Booking
Welcome to inaspace, the straightforward application designed for booking rooms within a corporate setting. Whether you need a space for meetings, conferences, or team sessions, inaspace makes it easy to find and reserve the perfect room. Enjoy a hassle-free experience with our intuitive room management system.

## Deployed Site:
[Click here to view deployed site on Heroku](https://inaspace-4c7fc427a59a.herokuapp.com/)

![inaspace Mockup](docs/readme_images/inaspace_mockup.webp)

## Table of Contents
- [Introduction](#introduction)	
- [UX](#ux)
	* [Account Creation and Login](#account-creation-and-login)
	* [Dashboard Overview](#dashboard-overview)
	* [Room Booking Management](#room-booking-management)
	* [Customisation and Personalisation](#customization-and-personalization)
- [Project Planning](#project-planning)
    * [Wireframes](#wireframes)
    *  [Database Schema](#database-schema)
        - [Models](#models)
    - [Agile Methodologies ](#agile-methodologies)
        * [Epics](#epics)
        * [User stories](#user-stories)
        * [Kanban board](#kanban-board)
    - [Technologies Used](#technologies-used)
        * [Languages](#languages)
        * [Frameworks](#frameworks)
        * [Libraries & Packages](#libraries--packages)
- [Testing](#testing)
- [Features](#features)
    * [Future Features](#future-features)
- [Deployment](#deployment)
    * [GitHub](#github)
    * [Heroku](#heroku)
- [Credits](#credits)
    * [Code](#code)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

## Introduction
 Introducing 'inaspace'..a room booking application for multi-purpose organizations. From office reservations to meeting scheduling and rehearsal studio bookings, 'inaspace' streamlines the process with a minimalist yet highly efficient design, enhancing user experience. Easily tailored to fit your organization's structure, 'inaspace' ensures seamless coordination and optimal space utilization, eliminating scheduling conflicts and administrative hassles.

## UX
The 'inaspace' user experience is designed with simplicity and efficiency in mind, ensuring a seamless interaction from start to finish.

#### Account Creation and Login:
<p>
	<img src="docs/readme_images/inaspace_registration_page.webp" width="33%" alt="Registration view"/>
	<img src="docs/readme_images/inaspace_signin_page.webp" width="33%" alt="Signin view"/>
	<img src="docs/readme_images/inaspace_signout.webp" width="33%" height="185px" alt="Signout view"/>
</p>
Users begin by creating an account with a straightforward sign-up process, providing essential details such as name, email, and a secure password. Once registered, users can easily log in and out with their credentials, and with django-allauth, their data remains private and secure.

#### Dashboard Overview:
<p>
	<img src="docs/readme_images/inaspace-dashboard.webp" width="45%" alt="Dashboard view"/>
</p>
Upon logging in, users are greeted with a clean and intuitive dashboard. This central hub provides a quick overview of current bookings, upcoming reservations, and available rooms. The minimalist design ensures that all necessary information is accessible at a glance.

#### Room Booking Management:
The core functionality of 'inaspace' revolves around its robust room booking system, featuring full CRUD (Create, Read, Update, Delete) capabilities. Messages are displayed to the user confirming their actions thorughout the process:

- Create: Users can effortlessly create new bookings by selecting a room, date, and time slot. Additional details such as the purpose of the booking and any special requirements can be added to ensure everything is prepared in advance.
<p>
	<img src="docs/readme_images/inaspace_newbooking_form.webp" width="45%" alt="Booking form view"/>
</p>

- Read: All current and past bookings are easily accessible. Users can view detailed information about each reservation, including room specifications and booking history.
<p>
	<img src="docs/readme_images/inaspace-dashboard.webp" width="45%" alt="Dashboard view"/>
</p>

- Update: Should changes be necessary, users can quickly modify their bookings. Adjustments to time, date, or room selection are made with just a few clicks, ensuring flexibility and adaptability. Edit Form is rendered with data to be edited and option to cancel action is available.
<p>
	<img src="docs/readme_images/inaspace_edit_booking.webp" width="45%" alt="Edit booking form view"/>
</p>

- Delete: If a booking is no longer needed, users can simply delete it, freeing up the space for others and maintaining an organized schedule.
<p>
	<img src="docs/readme_images/inaspace_confirm_delete.webp" width="45%" alt="Delete booking view"/>
</p>

#### Customization and Personalization:
'inaspace' can be tailored to fit the unique structure of any organization. Administrators can customize room details, booking rules, and user permissions, ensuring the application aligns perfectly with organizational needs. This adaptability ensures that 'inaspace' remains a valuable tool for any multi-purpose organization, regardless of size or complexity.


## Project planning

### Wireframes
#### Home Page
<p>
  <img src="docs/readme_images/inaspace_mobile_view.webp" height="300px" alt="mobile wireframe"/>
  <img src="docs/readme_images/inaspace_tablet_view.webp" height="300px" alt="tablet wireframe"/> 
</p>

#### Profile Page 
<p>
  <img src="docs/readme_images/inaspace_home_mobile.webp" height="300px" alt="mobile wireframe"/>
  <img src="docs/readme_images/inaspace_home_tablet.webp" height="300px" alt="tablet wireframe"/> 
</p>

### Database Schema
  <img src="docs/readme_images/inaspace_ER_diagram.webp" width="75%" alt="mobile wireframe"/>

### Models
#### User
The User model is based on Django's built-in authentication system, providing a robust and secure way to manage user accounts. It includes standard fields such as username, password, email, and has been extended by adding first_name and last_name, is_staff and joined_date.

#### Room
The Room model represents the various rooms available for booking within the inaspace application. Each room has the following attributes:

- name: A unique identifier for the room. In this case a fictional building was created featuring 4 floors of rooms numbered 101 - 115, 201 - 215 etc. 
- description: Detailed information about the room, including features and amenities.
- capacity: The maximum number of occupants the room can accommodate.

#### Booking
The Booking model allows users to reserve rooms for specific dates and times. It includes the following fields:

- user: A reference to the User who made the booking.
- room: A reference to the Room being booked.
- start_time: The starting time of the booking.
- end_time: The ending time of the booking.
- booking_date: The date for which the booking is made.


### Agile Methodologies

#### Epics
The development process was structured into three main Epics: Setup, User Account Management, and CRUD Functionality. Each Epic was broken down into specific User Stories to ensure a systematic and organized development workflow. Githubs Kanban board feature was used to manage the process.
<br>

  <img src="docs/readme_images/inaspace-kanban.webp" alt="mobile wireframe"/>

#### User stories
1. As a developer I can setup the project so that it is ready for implementing core features.
2. As a developer I can create base.html so that other pages can reuse the layout.
3. As a developer I can create static resources so that so that assets, css and js work throughout the site.
4. As a user I can sign up/create an account so that I can access website features.
5. As a user I can see custom 403, 404 and 500 error pages so that I can understand what error has occurred
6. As a user I can see a home page when first arriving so that information about the app is easily accessible.
7. As a logged in user I can select a room and time so that I can create a room booking.
8. As a logged in user I can select edit or delete so that I can amend an existing booking associated with my account.
9. As a user I can recieve feedback when performing CRUD operations so that I know it was complete successfully.
10. As a User I can use clearly presented forms so that perform actions within the site.
11. As a developer I can deploy app to heroku so that users can access the site.
12. As a developer I can create wireframes so that I can have a clear idea of how my site will look.
13. As a developer I can create a detailed README.md so that others can understand my methodologies for creating 'inaspace'.
14. As a developer I can use djangos automated testing features so that ensure functionality of all site elements.
15. As a developer I can create a databse schema so that all relevant data are stored and accessible.
16. As a developer I can use UserPassesTestMixin so that database is proteted from unauthorised access.
17. As a user I can see different navigation options so that I can log out when logged in and vice-versa.
18. As a User I can logout so that I can leave the app.
19. As a site admin I can see all bookings so that I can manage the booking system effectively.
20. As a User I can view a list of my open bookings.
21. As a Developer I can manually test all aspects of the app so that I can ensure the app functions as expected.

Details of the acceptance criteria for the USer Stories is found via the link to the Kanban Board in the following section.

Note: 3 other user stories have been added to Future Development Ideas below.

#### Kanban board
[Click here to view Kanban board on Github](https://github.com/users/bengilbertcodes/projects/6/views/1)

### Technologies Used

#### Languages
- HTML
- CSS 
- Javascript
- Python

#### Frameworks
- Django
- Bootstrap 5

#### Libraries & Packages
- JQuery
- django-allauth
- DataTable [link to datatables.net](https://datatables.net/)
- jQuery Timepicker

#### Tools & Programs
- VSCode
- Github Pages
- Github Kanban Board

### Testing

### Deployment

#### GitHub

#### Heroku

### Features

### Credits

#### Acknowledgements
