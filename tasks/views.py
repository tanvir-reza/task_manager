from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,View
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import TaskForm

# Create your views here.
class HomeView(ListView):
     template_name = 'home.html'
     model = Task
     context_object_name = 'tasks'
     ordering = ['-created']


class TaskListView(LoginRequiredMixin,View):
     login_url = 'login'
     def get(self,request):
          tasks = Task.objects.filter(user=request.user)
          return render(request,'dashboard.html',{'tasks':tasks})


class TaskCreateView(LoginRequiredMixin,View):
     login_url = 'login'
     def get(self,request):
          form = TaskForm()
          dat = "Create Task"
          return render(request,'form.html',{'form':form,'dat':dat})
     def post(self,request):
          user = request.user
          title = request.POST.get('title')
          description = request.POST.get('description')
          image = request.FILES.get('images')
          priority = request.POST.get('priority')
          due_date = request.POST.get('due_date')
          task = Task.objects.create(title=title,description=description,images=image,due_date=due_date,priority=priority,user=user)
          task.save()
          return redirect('/')


class TaskUpdateView(LoginRequiredMixin,View):
     login_url = 'login'
     def get(self,request,pk):
          task = Task.objects.get(id=pk)
          form = TaskForm(instance=task)
          dat = "Update Task"
          return render(request,'form.html',{'form':form,'dat':dat})
     def post(self,request,pk):
          task = Task.objects.get(id=pk)
          form = TaskForm(request.POST,request.FILES,instance=task)
          if form.is_valid():
               form.save()
               return redirect('/')
          else:
               return render(request,'form.html',{'form':form})
          
     


class TaskDetailView(LoginRequiredMixin,View):
     login_url = 'login'
     def get(self,request,pk):
          task = Task.objects.get(id=pk)
          return render(request,'task-details.html',{'task':task})
     
class TaskDeleteView(LoginRequiredMixin,View):
     login_url = 'login'
     def get(self,request,pk):
          task = Task.objects.get(id=pk)
          task.delete()
          return redirect('/')
     




class Login(View):
     def get(self,request):
          if request.user.is_authenticated:
               return redirect('/')
          return render(request,'login.html')
     def post(self,request):
          if request.user.is_authenticated:
               return redirect('/')
          else:
               username = request.POST.get('username')
               password = request.POST.get('password')
               user = auth.authenticate(username=username,password=password)
               if user is not None:
                    auth.login(request,user)
                    return redirect('/')
               else:
                    messages.info(request,'invalid credentials')
                    return redirect('login')
     

class Registration(View):
     def get(self,request):
          return render(request,'registration.html')
     def post(self,request):
          username = request.POST.get('username')
          email = request.POST.get('email')
          password = request.POST.get('password')
          password2 = password

          if len(username) < 4:
               messages.info(request,'Username must be atleast 4 characters')
               return redirect('signup')
          elif len(password) < 8:
               messages.info(request,'Password must be atleast 8 characters')
               return redirect('signup')
          elif password != password2:
               messages.info(request,'Password not match')
               return redirect('signup')

          if password == password2:
               if User.objects.filter(username=username).exists():
                    messages.info(request,'Username Taken')
                    return redirect('signup')
               elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email Taken')
                    return redirect('signup')
               else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    print('user created')
                    return redirect('login')
          return render(request,'registration.html')
     
class LogoutView(View):
     def get(self,request):
          auth.logout(request)
          return redirect('/')