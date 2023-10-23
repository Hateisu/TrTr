#Это мои методы

#Метод отправки данных в телеграмм
def sendTeleData(Data):#Получаем данные для отпраки
	
	#Импорт для работы бота телеграмм
	import telebot

	#API ключ для доступа к боту
	key = "5509137239:AAFot9WAsjdwcL2jy3tQp46UaFul10pptUI"
	
	#Создаем класс с ботом передавая в него ключ
	bot = telebot.TeleBot(key)

	#ID пользователей для отправки конкретному пользователю
	id_timka="1744884908"
	id_alihan="603317113"
	
	#Команды боту для отпраки пользователям данные
	bot.send_message(id_timka,Data)
	bot.send_message(id_alihan,Data)


#Метод подбора
def get_place_list(city,needed_time,needed_type, age):

	#Импорт данных из базы данных
	from .models import almaty_table, astana_table, turkestan_table, karaganda_table, kostanay_table, aktobe_table, aktay_table, shymkent_table

	#Регистрация переменных
	time_for_human = 0
	operating_objects = None
	will_return_list_objects = []

	#Получение обьектов по соответствию к городу
	if city=='almaty':
		operating_objects = almaty_table.objects.all()
	elif city=='astana':
		operating_objects = astana_table.objects.all()
	elif city=='turkestan':
		operating_objects = turkestan_table.objects.all()
	elif city=='karaganga':
		operating_objects = karaganda_table.objects.all()
	elif city=='kostanay':
		operating_objects = kostanay_table.objects.all()
	elif city=='aktobe':
		operating_objects = aktobe_table.objects.all()
	elif city=='shymkent':
		operating_objects = shymkent_table.objects.all()
	elif city=='aktay':
		operating_objects = aktay_table.objects.all()
	else:
		raise ValueError("\n\nНеверно предоставлены данные по городам,\n ответы могут принимать значения: \nalmaty, astana, turkestan, karaganga, kostanay, aktobe, aktay, shymkent. \n\n ")

	#Получение обьектов по соответствию к времени
	if (needed_time == "less30"):
		time_for_human=30
	elif (needed_time == "less50"):
		time_for_human=50
	elif (needed_time == "less90"):
		time_for_human=90
	elif ((needed_time == "more90") or (needed_time=="")):
		time_for_human= 0-1
	else:
		raise ValueError("\n\nНеверно предоставлены данные по времени,\n ответы могут принимать значения: \nless30, less50, less90, more90, ''. \n\n ")

	#Валидация ответов
	if age == "young":
		pass
	elif age == "mature":
		pass
	elif age == "middile":
		pass
	elif age == "old":
		pass
	else:
		raise ValueError("\n\nНеверно предоставлены данные по возрасту,\n ответы могут принимать значения: \nyoung, mature, middile, old. \n\n ")

	#Валидация ответов
	if needed_type == "nature":
		pass
	elif needed_type == "funny":
		pass
	elif needed_type == "history":
		pass
	elif needed_type == "culture":
		pass
	else:
		raise ValueError("\n\nНеверно предоставлены данные по типу достопримечательности,\n ответы могут принимать значения: \nnature, funny, history, culture. \n\n ")


	#Подбор по атрибутам
	for object_ in operating_objects:
		if object_.typeofwonder==needed_type:
			#print(  ((object_.is_any  ==  True) or (object_.is_young and (age == 'young')) or (object_.is_mature and (age == 'mature')) or (object_.is_middle and (age == 'middile')) or (object_.is_old and (age == 'old')))  )
			if ((object_.is_any  ==  True) or (object_.is_young and (age == 'young')) or (object_.is_mature and (age == 'mature')) or (object_.is_middle and (age == 'middile')) or (object_.is_old and (age == 'old'))):

				if object_.time<time_for_human:
					will_return_list_objects.append(object_)
				elif time_for_human==(0-1):
					will_return_list_objects.append(object_)
	#print(reply)
	return will_return_list_objects