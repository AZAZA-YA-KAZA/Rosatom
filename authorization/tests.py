from django.test import SimpleTestCase
from django.urls import reverse


class AuthorizationTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/auth/")
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("auth"))
        self.assertTemplateUsed(response, "authorization/auth.html")

