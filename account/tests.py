# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import override_settings

from account.models import MyUser
from project_system.settings import TEST_DIR


@override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
class AccountTest(APITestCase):

    super_admin = {
        "email": "admin@test.com",
        "password": "123456"
    }

    def setUp(self):
        print("setUp")
        admin = MyUser.objects.create_superuser(**self.super_admin)
        admin.save()

    def test_is_admin_exists(self):
        admin = MyUser.objects.filter(is_superuser=True)
        self.assertTrue(admin.exists())

    def test_get_token(self):
        response = self.client.post(reverse('token_obtain_pair'),
                                    self.super_admin, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("access" in response.json())

    def tearDown(self):
        pass
