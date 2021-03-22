from django.test import TestCase
from .models import Category, Photo


class CategoryTestClass(TestCase):

    def setUp(self):

        self.travel = Category(name= 'Travel')

    def test_instance(self):

        self.assertTrue(isinstance(self.travel, Category))

    def test_save_method(self):

        self.travel.save_travel()
        travels = Category.objects.all()
        self.assertTrue(len(travels)>0)


class PhotoTestClass(TestCase):

    def setUp(self):
        self.travel = Category(name= 'Travel')
        self.image = Photo(category=self.travel, description = 'Am in the test module', )

    def test_instance(self):

        self.assertTrue(isinstance(self.image, Photo))


    def tearDown(self):
        Category.objects.all().delete()
        Photo.objects.all().delete()