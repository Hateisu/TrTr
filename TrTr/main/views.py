#Импорты
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage, timezone

#Импорт Формы
from .forms import PostForm

#Импорт Пагинатора
from django.core.paginator import Paginator

#Импорт моих функций
from .my_utils import sendTeleData, get_place_list
# Create your views here.

#Создание метода для Гугл Формы и дальнейшее подключение к url
def forms(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			reply = ""
			my_list = get_place_list(post.city,post.needed_time,post.needed_type,post.age)
			for i in my_list:
				reply=reply+i.name+", "
			ret_text=("ФИО отправителя: "+post.name+'\n'+"Возраст: "+post.age+'\n'+"Город: "+post.city+'\n'+"Время: "+post.needed_time+'\n'+"Тип: "+post.needed_type+'\n'+"Дата: "+str(timezone.now())+'\n'+'\n'+"Рекомендации :  "+reply+"")
			sendTeleData(ret_text)
			post.recomendations = reply
			#post.published_date = timezone.now()
			post.save()
		else:
			pass
			#print("пришел неверный ответ")
	else:
		form = PostForm()
	return render(request, 'google_form/forms.html', {'form': form})

#Метод Главной страницы
def main_page(request):
	return render(request, 'frontend/index.html')

#Метод страницы с Подбором
def tours(request):
	context = {}
	if request.method == 'GET':
		time = request.GET.get('time', 'Invalid')
		age = request.GET.get('age', 'Invalid')
		type_ = request.GET.get('type', 'Invalid')
		place = request.GET.get('place', 'Invalid')
		objects_pointer= []
		if place !="Invalid" and age !="Invalid" and type_ !="Invalid" and time !="Invalid":
			objects_pointer =  get_place_list(place, time, type_, age)		
		#context = {'object_list':objects_pointer,}
		context1 = Paginator(objects_pointer, 3)
		page = int(request.GET.get('page', 0))
		pages = context1.get_page(page)
		if page==0:
			context = {
				   }
		else:
			context = {'object_list':context1.page(page),
				   'pages':context1,
				   'current':pages,
				   }

	return render(request, 'frontend/dostoprim.html',context)


#Внедрение Ajax 
def tours_filter(request):
	#if request.method =='GET':
	#	print("It is get")
	is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
	if is_ajax:
	#	print("doin some ajax")
		#print(request.GET.get('answer_time', ''))
		if request.method == 'GET':
			time = request.GET.get('time', 'Invalid')
			age = request.GET.get('age', 'Invalid')
			type_ = request.GET.get('type', 'Invalid')
			place = request.GET.get('place', 'Invalid')
			objects_pointer =  get_place_list(place, time, type_, age)	
			print(objects_pointer[1].name)
			return JsonResponse({'response':str(objects_pointer[1].image.url)})
		return JsonResponse({'status': 'Invalid request'}, status=400)
	else:
		return HttpResponseBadRequest('Invalid request')


