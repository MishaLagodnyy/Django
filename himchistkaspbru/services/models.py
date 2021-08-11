from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255,verbose_name= 'Имя')
    patronymic = models.CharField(max_length=255,verbose_name= 'Отчество')
    lastname = models.CharField(max_length=255,verbose_name= 'Фамилия')
    tel = models.IntegerField(verbose_name="телефон")
    street = models.CharField(max_length=255, verbose_name="улица")
    house = models.PositiveIntegerField(verbose_name="дом")
    building = models.CharField(max_length=5, verbose_name="строение")
    entrance = models.PositiveIntegerField(verbose_name="подъезд")
    flat = models.PositiveIntegerField(verbose_name="квартира")
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.lastname
    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"
        ordering = ['id']


class Courier(models.Model):
    name = models.CharField(max_length=255,verbose_name= 'Имя')
    patronymic = models.CharField(max_length=255,verbose_name= 'Отчество')
    lastname = models.CharField(max_length=255,verbose_name= 'Фамилия')
    def __str__(self):
        return self.lastname
    class Meta:
        verbose_name = "Курьеры"
        verbose_name_plural = "Курьеры"
        ordering = ['id']

class Prices(models.Model):
    thing = models.CharField(max_length=255,verbose_name= 'Вещь')
    service = models.CharField(max_length=255,verbose_name= 'Услуга')
    price = models.IntegerField(verbose_name= 'Цена услуги')
    class Meta:
        verbose_name = "Цены"
        verbose_name_plural = "Цены"
        ordering = ['id']

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    clientId = models.ForeignKey(Client, on_delete=models.SET_NULL, verbose_name='ID Клиента', null=True)
    courierId = models.ForeignKey(Courier, on_delete=models.SET_NULL, verbose_name='ID Курьера', null=True)
    priceId = models.ForeignKey(Prices, on_delete=models.CASCADE, verbose_name='ID Заказа', null=True)
    order_status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"
        ordering = ['id']

class Post(models.Model):
    name_post = models.CharField(max_length=255,verbose_name= 'Заголовок')
    info_post = models.TextField(blank=True,verbose_name= 'Описание')

    class Meta:
        verbose_name = "Пост главной страницы"
        verbose_name_plural = "Пост главной страницы"
        ordering = ['id']

class Questions_And_Answers(models.Model):
    name_question = models.TextField(blank=True,verbose_name= 'Вопрос')
    аnswer_question = models.TextField(blank=True, verbose_name='Ответ')

    class Meta:
        verbose_name = "Вопросы и ответы"
        verbose_name_plural = "Вопросы и ответы"
        ordering = ['id']
class Reviews(models.Model):
    client_id_reviews = models.ForeignKey(Client, on_delete=models.SET_NULL, verbose_name='ID Клиента Отзыв', null=True)
    text_reviews = models.TextField(blank=True, verbose_name='Отзыв')
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзыв"
        ordering = ['id']