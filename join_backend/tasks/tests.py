from django.test import TestCase
from .models import Task

# Create your tests here.


class TasksModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(
            title="Test Task",
            description="Test Description",
            category="Test Category",
            assigned="Test Assignee",
            dueDate="2023-08-12",
            prio="High",
            status="todo",
        )

    def test_title_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "title")

    def test_description_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")
