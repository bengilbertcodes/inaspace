<img style="display: block; margin: auto; height: 100px;" src="docs/readme_images/inaspace_logo.webp" alt="inapsace logo"/> 
</br>

# inaspace:<br> A straightforward application for booking rooms within a corporate setting
</br>

![inaspace Mockup](docs/readme_images/inaspace_mockup.webp)

## Table of Contents
- [Introduction](#Introducing 'inaspace')
- [UX](#ux)
- [Design](#design)
- [Project Planning](#project-planning)
    * [Wireframes](#wireframes)
    *  [Database Schema](#database-schema)
        - [Models](Models)
    - [Agile Methodologies ](#agile-methodologies)
        * [Epics](#epics)
        * [User stories](#user-stories)
        * [MoSCoW prioritization](#moscow-prioritization)
        * [Kanban board](#kanban-board)
    - [Technologies Used](#technologies-used)
        * [Languages](#languages)
        * [Frameworks](#frameworks)
        * [Libraries](#libraries)
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

## Introducing 'inaspace'
 ..the ultimate room booking application for multi-purpose organizations. From office reservations to meeting scheduling and rehearsal studio bookings, 'inaspace' streamlines the process with a minimalist yet highly efficient design, enhancing user experience. Easily tailored to fit your organization's structure, 'inaspace' ensures seamless coordination and optimal space utilization, eliminating scheduling conflicts and administrative hassles.

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

### Agile Methodologies

#### Epics

#### User stories

#### MoSCoW prioritization

#### Kanban board

### Technologies Used

#### Languages

#### Frameworks

#### Libraries

#### Tools & Programs

### Testing

### Deployment

#### GitHub

#### Heroku

### Features

### Credits

#### Acknowledgements
