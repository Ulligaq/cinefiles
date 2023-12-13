from django.test import SimpleTestCase, TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Review

# Create your tests here.

class ReviewHomePageTests(TestCase):                ## We're using TestCase rather than SimpleTest case
    def test_homeExists(self):                      ## Because we need to query for the reviews on home
        response = self.client.get("")              ## And further, because almost all pages inherit
        self.assertEqual(response.status_code, 200) ## From home, probably everything will need it.

class ReviewDetailTests(TestCase): 
    def setUp(self):
        
        self.user = User.objects.create_user( ## I use the base django user model here, as
            username='testUser',              ## in time of writing these tests the user model
            password='testPassword'           ## is being updated for the profile page functions
        )                                     ## that model will have its own tests in its module

        self.review = Review.objects.create(  ## This is just the review model, though minus
            movie='testMovie',                ## the date field, given that it's auto assigned
            thumbnail='testImage',
            title='testTitle',
            content='testContent',
            author=self.user                  ## Technically, there's nothing stopping this from
        )                                     ## later having integration with the custom user model
                                              ## though it's... eh? not needed.

    def test_get_absolute_url(self):         ## Tests the existance of the review's page
        reviewUrl = f'/review/{self.review.pk}/'
        self.assertEqual(self.review.get_absolute_url(), reviewUrl)
