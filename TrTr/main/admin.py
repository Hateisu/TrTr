from django.contrib import admin

# Register your models here.
from .models import *

class admin_view(admin.ModelAdmin):
    fields = ('title')

#Регистрация моделей Базы Данных в панели Админа, для дальнейшей поддержки базы данных
admin.site.register(Post)
admin.site.register(almaty_table)
admin.site.register(astana_table)
admin.site.register(aktay_table)
admin.site.register(aktobe_table)
admin.site.register(karaganda_table)
admin.site.register(kostanay_table)
admin.site.register(turkestan_table)
admin.site.register(shymkent_table)
