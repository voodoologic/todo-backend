from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a test task
        self.task = Task.objects.create(
            name="Test Task",
            description="This is a test task.",
            due_date="2023-12-31",
            priority="medium",
            completed=False,
            user=self.user
        )

    def test_task_str(self):
        # Test the string representation of the Task model
        self.assertEqual(str(self.task), "Test Task")