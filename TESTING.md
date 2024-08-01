# inaspace: A Room Booking app - Testing details

[Main README.md file](README.md) <br>
[View the website on Heroku]()

## Validator Testing

### HTML
All the HTML files were checked with [W3C Markup Validation Service](https://validator.w3.org/) and errors identified addressed.

**Exclusions:**

Some errors involving Django elements, such as Summernote features or Bootstrap, were excluded. These errors were acknowledged but not modified as they are integral to the correct functionality of the website.


### CSS

CSS files were checked with [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator.html.en) with no errors.

### JavaScript
JS files were checked with [JSHint](https://jshint.com/) with no errors.


### Python 
[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python code. All the errors highlighted were fixed. 

## Lighthouse Testing
I performed Lighthouse tests using Chrome Dev tools in an incognito window.

- **Homepage**:


- **Profile page**:    

- **About page**:


- **Register page**:


- **Login page**:


- **Logout page**:


## Manual testing


## User Stories completion

To check User Stories completion, please refer to the [Kanban Board]().

## Automated testing
The functionalities tested in bookings/test_forms.py were: 
- All user input fields in CustomSignupForm
- User input fields for BookingForm <br>
<img src="docs/testing_images/.webp" height="100px" alt="CustomSignupForm Results">


## Browser Compatibility
Below are the browsers that have been tested:

## Responsiveness 
The website's responsiveness has been tested using Google Chrome Developer Tools. To ensure compatibility across different devices, various screen resolutions were simulated.

The website displays responsively across a wide range of devices and screen sizes.

## Bugs resolved