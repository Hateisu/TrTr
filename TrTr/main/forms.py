from django import forms

from .models import Post

#Создание Формы для поддержки Google-form-ы
class PostForm(forms.ModelForm):
    class Meta:
        wonder_ranges=(('funny','Отдых и развлечения'),('history','Исторический тип'),('nature','Природный тип'),('culture','Культурный тип'))
        city_ranges = (
        ('almaty','Алматы'),
        ('astana','Астана'),
        ('aktay','Актау'),
        ('aktobe','Актобе'),
        ('karaganda','Караганда'),
        ('kostanay','Костанай'),
        ('turkestan','Туркестан'),
        ('shymkent','Шымкент')
        )
        age_ranges = (
        ('young', 'Молодой (до 18 лет)'),
        ('mature', 'Зрелый (от 19 до 34 лет)'),
        ('middile', 'Средний (от 35 до 59 лет)'),
        ('old', 'Пожилой (от 60 до 74 лет)'))
        time_ranges=(
        ('less30','до 30 минут'),
        ('less50','от 30 до 50 минут'),
        ('less90','от 50 минут до 1,5 часов'),
        ('more90','от 1,5 часов и более')
        )
        model = Post
        fields = ('name', 'age','city','needed_time','needed_type','recomendations')
        widgets = {
            #RadioSelect - это множественный выбор
            'needed_type': forms.RadioSelect(choices=wonder_ranges),
            'city':forms.RadioSelect(choices=city_ranges),
            'age':forms.RadioSelect(choices=age_ranges),
            'needed_time':forms.RadioSelect(choices=time_ranges)
        }
