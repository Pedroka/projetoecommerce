from django.test import TesteCase
from catalog.models import Category, Product
from model_mommy import mommy
from django.core.urlresolvers import reverse

class CategoryTeste(TesteCase):
    def setUp(self):
        self.category = momm.make('catalog.Category')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.category.get_absolute_url(),
            reverse('catalog:category',kwargs={'slug':self.category.slug})
        )

class ProductTeste(TesteCase):
    def setUp(self):
        self.product = momm.make(Product,slug='produto')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.product.get_absolute_url(),
            reverse('catalog:product',kwargs={'slug':'produto'})
        )
