from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth import  authenticate,login,logout
from django.shortcuts import render,redirect
from . models import Profile,Student
from django.views.generic import ListView
from .tables import StudentTable

# Create your views here.
def home(request):
    return HttpResponse('Helo person' )


def signup(request):
    try:
        if request.method == 'POST': 
            fname=request.POST.get('fname') 
            emailId=request.POST.get('emailId')
            pwd=request.POST.get('pwd')
            my_user=User.objects.create_user(fname,emailId,pwd)
            my_user.save()
            
            user_model=User.objects.get(username=fname)
            user_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
            user_profile.save()
            
            if my_user is not None:
                login(request,my_user)
                return redirect('/')
            return redirect('/')
    except:
        invalid='User already exists'
        return render(request,'signup.html',{'invalid':invalid})
    return render(request ,'signup.html')

def student_list_view(request):
    # Create a table instance with the queryset
    table = StudentTable(Student.objects.all())
    
    # Render the table instance in the template
    return render(request, 'table.html', {'table': table})
def tables(request):
 context = {
    'segment': 'tables',
    # 'students' : Student.objects.all()
  }
 return render(request, "dynamicTable.html", context)


def index(request):

  context = {
    # 'segment'  : 'index',
    'products' : Student.objects.all()
  }
  return render(request, "student.html", context)
class StudentListView(ListView):
    model = Student
    table_class=StudentTable
    template_name = 'table.html'     
    
    