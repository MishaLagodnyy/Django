from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'tel', 'street', 'house', 'building' )
    list_display_links = ('id', 'name', 'lastname')
    search_fields = ('lastname',)

class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'patronymic', 'lastname')
    list_display_links = ('id', 'name', 'patronymic', 'lastname')
    search_fields = ('lastname',)
class PricesAdmin(admin.ModelAdmin):
    list_display = ('id', 'thing', 'service', 'price')
    list_display_links = ('id', 'thing', 'service', 'price')
    search_fields = ('thing', 'service',)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'clientId', 'courierId', 'priceId', 'order_status',)
    list_display_links = ('id', 'clientId', 'courierId', 'priceId', 'order_status',)
    search_fields = ('id', 'clientId', 'courierId', 'priceId', 'order_status',)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','name_post',)
    list_display_links = ('id','name_post',)
    search_fields = ('id','name_post',)

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id_reviews', 'text_reviews',)
    list_display_links = ('id', 'client_id_reviews', 'text_reviews',)
    search_fields = ('id', 'client_id_reviews',)

class Questions_And_AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_question', 'аnswer_question',)
    list_display_links = ('id', 'name_question', 'аnswer_question',)
    search_fields = ('id', 'name_question', 'аnswer_question',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Courier, CourierAdmin)
admin.site.register(Prices, PricesAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Questions_And_Answers, Questions_And_AnswersAdmin)
