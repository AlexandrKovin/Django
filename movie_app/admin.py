from django.contrib import admin, messages
from .models import Movie, Director, Actor
from django.db.models import QuerySet

# Register your models here.

admin.site.register(Director)
admin.site.register(Actor)

class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший'),
        ]

    def queryset(self, request, qs: QuerySet):
        if self.value() == '<40':
            return qs.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return qs.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return qs.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '>=80':
            return qs.filter(rating__gte=80)
        return qs

# Чтобы в админке отобразились новые поля
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # В добавление нового фильма, отображение только выбранных полей
    # fields = ['name', 'rating']
    #exclude = ['slug']
    # Запретить пользователю редактировать поля
    # readonly_fields = ['year']
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status', 'director']
    # Редактирование полей, так как name является ссылкой, то его нельзя редактировать
    list_editable = ['rating', 'currency', 'budget', 'director']
    # Изменение вида фильтра
    filter_horizontal = ['actors']
    # Фильтр при открытии
    ordering = ['rating', '-name']
    # Разделение на страницы
    list_per_page = 10
    # Регистрирование метода set_dollars
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name__istartswith', 'rating']
    # Фильтр
    list_filter = ['name', 'currency',  RatingFilter]

# Чтобы добавился фильтр на наше поле
    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Фигня какая-то'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'Зачет'
        return 'Топ'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EURO)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            # Цвет сообщения
            messages.ERROR
        )


# Чтобы в админке отобразились новые поля
# admin.site.register(Movie, MovieAdmin)
# from movie_app.models import Movie
# from movie_app.models import Director
