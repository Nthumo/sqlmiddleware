import factory
from factory.faker import faker
from .models import Product

FAKE = faker.Faker()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product