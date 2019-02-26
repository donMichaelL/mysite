from django.test import TestCase

from .models import Story


class StoryTestModel(TestCase):
    def setUp(self):
        Story.objects.create(title="New Title", text="text")

    def test_story_created(self):
        self.assertEqual(Story.objects.count(), 1)

    def test_story_str(self):
        self.assertEqual(Story.objects.first().__str__(), "New Title")
        
