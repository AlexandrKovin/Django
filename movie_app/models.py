from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Валидация полей Модели
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField(default='test@gmail.com')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('one_director', args=[self.id])

class Actor(models.Model):
    MALE = 'М'
    FEMALE = 'F'

    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        else:
            return f'Актриса {self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('one_actor', args=[self.id])

class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]


    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, blank=True,
                                 validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    # Установление связи один ко многим
    # PROTECT не дает удалить (режиссера) тогда когда он связан
    # CASCADE удаляет не только (Режиссера ну и фильмы которые он снял)
    # SET_NULL можно удалить (Режиссера и проставит вместо него NULL)
    # При создании связи, ттакже создается поле обратной связи _set (g.movie_set.all())
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actor)

# Сохранение вручную save()
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Movie, self).save(*args, *kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

# Переопределяет наши экземпляры.
    def __str__(self):
        return f'{self.name} - {self.rating}%'