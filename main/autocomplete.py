from .models import Post
from faker import Faker
fake = Faker()

def search_db(n):
    for i in range(0, n):
        Post.objects.create(
            post = fake.title()
            )