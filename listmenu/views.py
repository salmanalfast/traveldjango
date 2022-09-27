from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import foodmenu, drinkmenu

def index(request):
	template = loader.get_template('index.html')
	thefoods = foodmenu.objects.all().values()
	thedrinks = drinkmenu.objects.all().values()
	context = {
		'thefoods' : thefoods,
		'thedrinks' : thedrinks,
	}
	return HttpResponse(template.render(context,request))

def thehome(request):
	template = loader.get_template('thehome.html')
	return HttpResponse(template.render())

def insert(request):
	template = loader.get_template('insertmenu.html')
	return HttpResponse(template.render({}, request))

def inserted(request):
	category = request.POST['category']
	if category == 1:
		x = request.POST['name']
		y = request.POST['price']
		thefoods = foodmenu(foods=x, price=y)
		thefoods.save()
	elif category == 2:
		a = request.POST['name']
		b = request.POST['price']
		thedrinks = drinkmenu(drinks=a, price=b)
		thedrinks.save()
	return HttpResponseRedirect(reverse('index'))

def editfood(request, id):
	thefood = foodmenu.objects.get(id=id)
	template = loader.get_template('edit.html')
	context = {
		'thefood' : thefood,
	}
	return HttpResponse(template.render(context, request))

def editedfood(request, id):
	x = request.POST['name']
	y = request.POST['price']
	food = foodmenu.objects.get(id=id)
	food.foods = x
	food.price = y
	food.save()
	return HttpResponseRedirect(reverse('index'))

def delfood(request, id):
	foods = foodmenu.objects.get(id=id)
	foods.delete()
	return HttpResponseRedirect(reverse('index'))

def editdrink(request, id):
	drink = drinkmenu.objects.get(id=id)
	template = loader.get_template('editd.html')
	context ={
		'drink' : drink,
	}
	return HttpResponse(template.render(context, request))

def editeddrink(request, id):
	drink = drinkmenu.objects.get(id=id)
	x = request.POST['name']
	y = request.POST['price']
	drink.drinks = x
	drink.price = y
	drink.save()
	return HttpResponseRedirect(reverse('index'))

def deldrink(request, id):
	deld = drinkmenu.objects.get(id=id)
	deld.delete()
	return HttpResponseRedirect(reverse('index'))

def gallery(request):
	template = loader.get_template('slideshow.html')
	return HttpResponse(template.render())