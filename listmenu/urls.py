from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('', views.index, name='index'),
	path('insert/', views.insert, name='insert'),
	path('insert/inserted/', views.inserted, name='inserted'),
	path('delfood/<int:id>', views.delfood, name='delfood'),
	path('editfood/<int:id>', views.editfood, name='editfood'),
	path('editfood/editedfood/<int:id>', views.editedfood, name='editedfood'),
	path('editdrink/<int:id>', views.editdrink, name='editdrink'),
	path('editdrink/editeddrink/<int:id>', views.editeddrink, name='editeddrink'),
	path('deldrink/<int:id>', views.deldrink, name='deldrink'),
	path('thehome/', views.thehome, name='thehome'),
	path('gallery/', views.gallery, name='gallery'),
]

urlpatterns += staticfiles_urlpatterns()