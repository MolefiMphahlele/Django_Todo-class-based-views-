from django.test import TestCase, RequestFactory, SimpleTestCase
from .views import TaskList
from django.urls import reverse, resolve
from django.contrib.auth.models import AnonymousUser, User

#the question is whether I need to use setup() to create a test case user
# does the test case user already have to be an exisiting user?
# for testing views, call setup()

class UrlsTesting(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username = "John",
            email = "John@email.com",
            password = "ThisIsJohn1"
        )

    def test_TaskList(self):
        request = RequestFactory().get('/')
        view = TaskList()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('tasks',context)
