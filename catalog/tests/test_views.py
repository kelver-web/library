from django.test import TestCase, Client
from django.urls import reverse
from model_mommy import mommy

from catalog.models import Category, Product


class TestProductList(TestCase):

    def setUp(self):
        self.url = reverse('catalog:product_list')
        self.client = Client()
        self.products = mommy.make(Product, _quantity=10)

    def tearDown(self):
        for prod in self.products:
            prod.delete()


    def test_view(self):
        responser = self.client.get(self.url)
        self.assertEquals(200, responser.status_code)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)

    def test_quantity_products(self):
        response = self.client.get(self.url)
        product_list = response.context['products']
        self.assertEquals(product_list.count(), 3)

    def test_paginator(self):
        response = self.client.get(self.url)
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages, 4)

    def test_page_not_found(self):
        response = self.client.get('{}?page=5'.format(self.url))
        self.assertEquals(response.status_code, 404)