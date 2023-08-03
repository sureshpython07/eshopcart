from django.test import TestCase
from shopapp.models import Product
# Create your tests here.


class ModelTesting(TestCase):
    def setUp(self):
        self.item = Product.objects.create(name='django', price=100)

    def test_product_model(self):
        ins = self.item
        self.assertTrue(isinstance(self.item, Product))
        self.assertEqual(str(ins), 'django')

    def tearDown(self):
        print('tesing tear down')
