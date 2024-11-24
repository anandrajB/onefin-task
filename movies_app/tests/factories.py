import factory
from django.contrib.auth import get_user_model
from movies_app.models import Genre, Movies, Collections

User = get_user_model()


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Faker(
        "word", ext_word_list=["Action", "Drama", "Comedy", "Thriller"]
    )


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movies

    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("text")


class CollectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Collections

    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("text")
    created_by = factory.SubFactory(User)
