from django.contrib import admin
from django.urls import path
from userauth import views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home),
    path('signup/',views.signup, name='signup'),
    path('student/', views.student_list_view, name='student_list'),
    path('', views.tables, name='tables'),
    path('dynamicstudent', views.index,  name='student'),
 
]