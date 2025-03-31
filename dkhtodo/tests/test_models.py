from django.test import TestCase
from django.contrib.auth.models import User
from dkhtodo.models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        # Create a test task
        self.task = Task.objects.create(
            name="Test Task",
            description="This is a test task.",
            due_date="2025-03-30",
            priority="medium",
            completed=False,
            user=self.user
        )

    def test_task_str(self):
        """Test the string representation of the Task model."""
        self.assertEqual(str(self.task), "Test Task")

    def test_task_creation(self):
        """Test that a Task instance is created correctly."""
        self.assertEqual(self.task.name, "Test Task")
        self.assertEqual(self.task.description, "This is a test task.")
        self.assertEqual(self.task.due_date.strftime('%Y-%m-%d'), "2025-03-30")
        self.assertEqual(self.task.priority, "medium")
        self.assertFalse(self.task.completed)
        self.assertEqual(self.task.user, self.user)