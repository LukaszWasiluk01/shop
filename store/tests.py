from django.test import TestCase
from .models import Category

# Create your tests here.

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='toys', slug='toys')
    
    def test_category_model_entry(self):
        data = self.data1
        self.assertEqual(str(data), 'toys')