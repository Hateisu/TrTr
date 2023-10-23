from django.db import models
# Create your models here.

#Модель для Формы
class Post(models.Model):
	age_ranges = (
        ('young', 'Молодой (до 18 лет)'),
        ('mature', 'Зрелый (от 19 до 34 лет)'),
        ('middile', 'Средний (от 35 до 59 лет)'),
        ('old', 'Пожилой (от 60 до 74 лет)'),)
	city_ranges = (
    	('almaty','Алматы'),
    	('astana','Астана'),
    	('aktay','Актау'),
    	('aktobe',''),
    	('karaganda',''),
    	('kostanay',''),
    	('turkestan','Туркестан'),
    	('shymkent',''),
    	)
	wonder_ranges=(
		('funny','Отдых и развлечения'),
		('history','Исторический'),
		('nature','Природный'),
		('culture','Культурный'),
		)
	time_ranges=(
		('less30','до 30 минут'),
		('less50','от 30 до 50 минут'),
		('less90','от 50 минут до 1,5 часов'),
		('more90','от 1,5 часов и более'),
		)
	name= models.CharField(max_length=150,verbose_name='Наименование',unique=True)
	age= models.CharField(max_length=150,verbose_name='Возраст', choices=age_ranges)
	city= models.CharField(max_length=150,verbose_name='Город', choices=city_ranges)
	needed_type = models.CharField(max_length=150,verbose_name='Тип', choices=wonder_ranges)
	needed_time = models.CharField(max_length=20,verbose_name='Время',choices=time_ranges,blank=True)
	recomendations = models.CharField(max_length=2000,verbose_name='Рекомендации',blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Короче юзер'
		verbose_name_plural = 'Пользователи'
		ordering = ['-id']

#Прочие модели и их атрибуты
class almaty_table(models.Model):
	wonder_ranges=(
		('funny','Отдых и развлечения'),
		('history','Исторический тип'),
		('nature','Природный тип'),
		('culture','Культурный тип'),
		)

	name = models.CharField(max_length=150,verbose_name='Наименование',unique=True)
	typeofwonder = models.CharField(max_length=150,verbose_name='Тип', choices=wonder_ranges)
	image = models.ImageField(upload_to='almaty', verbose_name='Картинка', blank=True)
	price = models.IntegerField(verbose_name='Цена', blank=True)
	description = models.CharField(max_length=150,verbose_name='Описание',blank=True)
	is_any = models.BooleanField(verbose_name='Для всех возрастов',default=False)
	is_young = models.BooleanField(verbose_name='Для Молодой (до 18 лет)',default=False)
	is_mature = models.BooleanField(verbose_name='Зрелый (от 19 до 34 лет)',default=False)
	is_middle = models.BooleanField(verbose_name='Средний (от 35 до 59 лет)',default=False)
	is_old = models.BooleanField(verbose_name='Пожилой (от 60 до 74 лет)',default=False)
	time = models.IntegerField(verbose_name='Время до точки с центра города (в минутах)')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Алматы'
		verbose_name_plural = 'Алматы'
		ordering = ['-id']

class astana_table(models.Model):
	wonder_ranges=(
		('funny','Отдых и развлечения'),
		('history','Исторический тип'),
		('nature','Природный тип'),
		('culture','Культурный тип'),
		)

	name = models.CharField(max_length=150,verbose_name='Наименование',unique=True)
	typeofwonder = models.CharField(max_length=150,verbose_name='Тип', choices=wonder_ranges)
	image = models.ImageField(upload_to='astana', verbose_name='Картинка', blank=True)
	price = models.IntegerField(verbose_name='Цена', blank=True)
	description = models.CharField(max_length=150,verbose_name='Описание',blank=True)
	is_any = models.BooleanField(verbose_name='Для всех возрастов',default=False)
	is_young = models.BooleanField(verbose_name='Для Молодой (до 18 лет)',default=False)
	is_mature = models.BooleanField(verbose_name='Зрелый (от 19 до 34 лет)',default=False)
	is_middle = models.BooleanField(verbose_name='Средний (от 35 до 59 лет)',default=False)
	is_old = models.BooleanField(verbose_name='Пожилой (от 60 до 74 лет)',default=False)
	time = models.IntegerField(verbose_name='Время до точки с центра города (в минутах)')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Астана'
		verbose_name_plural = 'Астана'
		ordering = ['-id']

class aktay_table(models.Model):
	wonder_ranges=(
		('funny','Отдых и развлечения'),
		('history','Исторический тип'),
		('nature','Природный тип'),
		('culture','Культурный тип'),
		)

	name = models.CharField(max_length=150,verbose_name='Наименование',unique=True)
	typeofwonder = models.CharField(max_length=150,verbose_name='Тип', choices=wonder_ranges)
	image = models.ImageField(upload_to='aktay', verbose_name='Картинка', blank=True)
	price = models.IntegerField(verbose_name='Цена', blank=True)
	description = models.CharField(max_length=150,verbose_name='Описание',blank=True)
	is_any = models.BooleanField(verbose_name='Для всех возрастов',default=False)
	is_young = models.BooleanField(verbose_name='Для Молодой (до 18 лет)',default=False)
	is_mature = models.BooleanField(verbose_name='Зрелый (от 19 до 34 лет)',default=False)
	is_middle = models.BooleanField(verbose_name='Средний (от 35 до 59 лет)',default=False)
	is_old = models.BooleanField(verbose_name='Пожилой (от 60 до 74 лет)',default=False)
	time = models.IntegerField(verbose_name='Время до точки с центра города (в минутах)')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Актау'
		verbose_name_plural = 'Актау'
		ordering = ['-id']

class aktobe_table(models.Model):
	wonder_ranges=(
		('funny','Отдых и развлечения'),
		('history','Исторический тип'),
		('nature','Природный тип'),
		('culture','Культурный тип'),
		)

	name = models.CharField(max_length=150,verbose_name='Наименование',unique=True)
	typeofwonder = models.CharField(max_length=150,verbose_name='Тип', choices=wonder_ranges)
	image = models.ImageField(upload_to='aktobe', verbose_name='Картинка', blank=True)
	price = models.IntegerField(verbose_name='Цена', blank=True)
	description = models.CharField(max_length=150,verbose_name='Описание',blank=True)
	is_any = models.BooleanField(verbose_name='Для всех возрастов',default=False)
	is_young = models.BooleanField(verbose_name='Для Молодой (до 18 лет)',default=False)
	is_mature = models.BooleanField(verbose_name='Зрелый (от 19 до 34 лет)',default=False)
	is_middle = models.BooleanField(verbose_name='Средний (от 35 до 59 лет)',default=False)
	is_old = models.BooleanField(verbose_name='Пожилой (от 60 до 74 лет)',default=False)
	time = models.IntegerField(verbose_name='Время до точки с центра города (в минутах)')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Актобе'
		verbose_name_plural = 'Актобе'
		ordering = ['-id']

class karaganda_table(models.Model):
	wonder_ranges=(
		('funny','Отдых и развлечения'),
		('history','Исторический тип'),
		('nature','Природный тип'),
		('culture','Культурный тип'),
		)

	name = models.CharField(max_length=150,verbose_name='Наименование',unique=True)
	typeofwonder = models.CharField(max_length=150,verbose_name='Тип', choices=wonder_ranges)
	image = models.ImageField(upload_to='karaganda', verbose_name='Картинка', blank=True)
	price = models.IntegerField(verbose_name='Цена', blank=True)
	description = models.CharField(max_length=150,verbose_name='Описание',blank=True)
	is_any = models.BooleanField(verbose_name='Для всех возрастов',default=False)
	is_young = models.BooleanField(verbose_name='Для Молодой (до 18 лет)',default=False)
	is_mature = models.BooleanField(verbose_name='Зрелый (от 19 до 34 лет)',default=False)
	is_middle = models.BooleanField(verbose_name='Средний (от 35 до 59 лет)',default=False)
	is_old = models.BooleanField(verbose_name='Пожилой (от 60 до 74 лет)',default=False)
	time = models.IntegerField(verbose_name='Время до точки с центра города (в минутах)')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Караганда'
		verbose_name_plural = 'Караганда'
		ordering = ['-id']

class kostanay_table(models.Model):
	wonder_ranges=(
		('funny','Отдых и развлечения'),
		('history','Исторический тип'),
		('nature','Природный тип'),
		('culture','Культурный тип'),
		)

	name = models.CharField(max_length=150,verbose_name='Наименование',unique=True)
	typeofwonder = models.CharField(max_length=150,verbose_name='Тип', choices=wonder_ranges)
	image = models.ImageField(upload_to='kostanay', verbose_name='Картинка', blank=True)
	price = models.IntegerField(verbose_name='Цена', blank=True)
	description = models.CharField(max_length=150,verbose_name='Описание',blank=True)
	is_any = models.BooleanField(verbose_name='Для всех возрастов',default=False)
	is_young = models.BooleanField(verbose_name='Для Молодой (до 18 лет)',default=False)
	is_mature = models.BooleanField(verbose_name='Зрелый (от 19 до 34 лет)',default=False)
	is_middle = models.BooleanField(verbose_name='Средний (от 35 до 59 лет)',default=False)
	is_old = models.BooleanField(verbose_name='Пожилой (от 60 до 74 лет)',default=False)
	time = models.IntegerField(verbose_name='Время до точки с центра города (в минутах)')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Костанай'
		verbose_name_plural = 'Костанай'
		ordering = ['-id']


class turkestan_table(models.Model):
	wonder_ranges=(
		('funny','Отдых и развлечения'),
		('history','Исторический тип'),
		('nature','Природный тип'),
		('culture','Культурный тип'),
		)

	name = models.CharField(max_length=150,verbose_name='Наименование',unique=True)
	typeofwonder = models.CharField(max_length=150,verbose_name='Тип', choices=wonder_ranges)
	image = models.ImageField(upload_to='turkestan', verbose_name='Картинка', blank=True)
	price = models.IntegerField(verbose_name='Цена', blank=True)
	description = models.CharField(max_length=150,verbose_name='Описание',blank=True)
	is_any = models.BooleanField(verbose_name='Для всех возрастов',default=False)
	is_young = models.BooleanField(verbose_name='Для Молодой (до 18 лет)',default=False)
	is_mature = models.BooleanField(verbose_name='Зрелый (от 19 до 34 лет)',default=False)
	is_middle = models.BooleanField(verbose_name='Средний (от 35 до 59 лет)',default=False)
	is_old = models.BooleanField(verbose_name='Пожилой (от 60 до 74 лет)',default=False)
	time = models.IntegerField(verbose_name='Время до точки с центра города (в минутах)')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Туркестан'
		verbose_name_plural = 'Туркестан'
		ordering = ['-id']



class shymkent_table(models.Model):
	wonder_ranges=(
		('funny','Отдых и развлечения'),
		('history','Исторический тип'),
		('nature','Природный тип'),
		('culture','Культурный тип'),
		)

	name = models.CharField(max_length=150,verbose_name='Наименование',unique=True)
	typeofwonder = models.CharField(max_length=150,verbose_name='Тип', choices=wonder_ranges)
	image = models.ImageField(upload_to='shymkent', verbose_name='Картинка', blank=True)
	price = models.IntegerField(verbose_name='Цена', blank=True)
	description = models.CharField(max_length=150,verbose_name='Описание',blank=True)
	is_any = models.BooleanField(verbose_name='Для всех возрастов',default=False)
	is_young = models.BooleanField(verbose_name='Для Молодой (до 18 лет)',default=False)
	is_mature = models.BooleanField(verbose_name='Зрелый (от 19 до 34 лет)',default=False)
	is_middle = models.BooleanField(verbose_name='Средний (от 35 до 59 лет)',default=False)
	is_old = models.BooleanField(verbose_name='Пожилой (от 60 до 74 лет)',default=False)
	time = models.IntegerField(verbose_name='Время до точки с центра города (в минутах)')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Щымкент'
		verbose_name_plural = 'Шымкент'
		ordering = ['-id']






