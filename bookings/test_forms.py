from django.test import TestCase
from allauth.account.forms import SignupForm as AllauthSignupForm
from bookings.forms import CustomSignupForm

class TestSignupForm(TestCase):
    
    def test_form_is_valid(self):
        """ Test for all fields """
        form = CustomSignupForm({
			'username': 'testuser',
			'email': 'testuser@example.com',
			'password1': 'ComplexPass123!',
			'password2': 'ComplexPass123!',
			'first_name': 'Test',
			'last_name': 'User',
		})
        self.assertTrue(form.is_valid(), msg='Form is not valid')
    
    def test_form_missing_fields(self):
        """ Test for missing email """
        form = CustomSignupForm({
            'username': 'testuser',
			'email': '',
			'password1': 'ComplexPass123!',
			'password2': 'ComplexPass123!',
			'first_name': 'Test',
			'last_name': 'User',
		})
        self.assertFalse(form.is_valid(), msg='Form is valid')
    
    def test_form_incorrect_email(self):
        """ Test for incorrect email format """
        form = CustomSignupForm({
            'username': 'testuser',
    		'email': 'bobatdotcom',
    		'password1': 'ComplexPass123!',
    		'password2': 'ComplexPass123!',
    		'first_name': 'Test',
    		'last_name': 'User',
        })
        self.assertFalse(form.is_valid(), msg='Form is valid')
