
from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def test_str_method(self):
        product = Product.objects.create(
            name="Test", description="desc", price=100, stock=10
        )
        self.assertEqual(str(product), "Test")
