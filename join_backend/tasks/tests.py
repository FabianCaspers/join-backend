from django.test import TestCase
from .models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

# Create your tests here.


class TasksModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass', email='testuser@example.com')
        cls.token, _ = Token.objects.get_or_create(user=cls.user)
        cls.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            category="Test Category",
            assigned="Test Assignee",
            dueDate="2023-08-12",
            prio="High",
            status="todo",
        )

    def setUp(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_title_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "title")

    def test_description_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")
        
    def test_get_task(self):
        response = self.client.get(f'https://fabiancaspersdjango.pythonanywhere.com/task/{self.task.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_post_task(self):
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'category': 'New Category',
            'assigned': 'New Assignee',
            'dueDate': '2023-08-12',
            'prio': 'Low',
            'status': 'todo',
        }
        response = self.client.post('https://fabiancaspersdjango.pythonanywhere.com/task/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'New Task')

    def test_patch_task(self):
        data = {
            'title': 'Updated Task',
        }
        response = self.client.patch(f'https://fabiancaspersdjango.pythonanywhere.com/task/{self.task.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Task')

    def test_delete_task(self):
        response = self.client.delete(f'https://fabiancaspersdjango.pythonanywhere.com/task/{self.task.id}/')
        self.assertEqual(response.status_code, 204)
