from django.core.management import BaseCommand
from product.models import Category, Product
from pathlib import Path
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories(filepath='fixtures/category_data.json'):
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    # Здесь мы получаем данные из фикстурв с категориями

    @staticmethod
    def json_read_products(filepath='fixtures/product_data.json'):
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        # Удалите все продукты
        # Удалите все категории

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category['pk'],
                        name=category['fields']['name'],
                        description=category['fields'].get('description', ''))
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)
        #
        # # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product['pk'],
                        name=product["fields"]["name"], description=product["fields"].get('description', ''),
                        photo=product['fields'].get('photo', ''),
                        purchase_price=product["fields"].get('purchase_price', 0),
                        category=Category.objects.get(pk=product["fields"]['category']),
                        creation_date=product['fields']['creation_date'],
                        last_modified_date=product['fields']['last_modified_date']
                        )
            )
        #
        # # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

        #print(product_for_create)
        #print(category_for_create)
