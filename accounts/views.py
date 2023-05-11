from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.views import View
from django.contrib import messages

from .models import Vehicle
# Create your views here.

class RegistrationView(View):
    def get(self, request):
        return render(request, 'accounts/index.html')

    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        context = {
            'fieldVal': request.POST,
        }
        if len(password) < 8:
            messages.error(request, 'Password too short')
            return render(request, 'accounts/index.html', context=context)

        user = User.objects.create_user(
            username=username, password=password, email=email)
        user.is_active = True
        user.save()
        return render(request, 'accounts/index.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/index.html')
    
    def post(self,request):
        username = request.POST['username']
        passwaord = request.POST['password']

        user = auth.authenticate(username=username, password=passwaord)

        if user:
            if user.is_active:
                auth.login(request, user)
                return redirect('view')
            return redirect('login')
        return redirect('register')
    

class LookView(View):
    def get(self,request):
        vehicle=Vehicle.objects.all()
        return render(request,'accounts/view.html',context={'vehicle':vehicle})
                

class AddView(View):
    def get(self, request):
        return render(request, 'accounts/add.html')
    def post(self,request):
        number = request.POST["vnumber"]
        description = request.POST["vdescription"]
        type = request.POST["vtype"]
        model = request.POST["vmodel"]
        Vehicle.objects.create(number=number,type=type,model=model,description=description)
        return render(request, 'accounts/add.html',context={'values':request.POST})
    
class EditView(View):
    def get(self, request,id):
        vehicle=Vehicle.objects.get(pk=id)
        return render(request, 'accounts/edit.html',context={'vehicle':vehicle})
    def post(self,request,id):
        number = request.POST["vnumber"]
        description = request.POST["vdescription"]
        type = request.POST["vtype"]
        model = request.POST["vmodel"]
        vehicle=Vehicle.objects.get(pk=id)
        vehicle.number=number
        vehicle.type=type
        vehicle.description=description
        vehicle.model=model
        vehicle.save()
        return redirect('view')
    

class DeleteView(View):
    def get(self, request,id):
        vehicle=Vehicle.objects.get(pk=id)
        vehicle.delete()
        return redirect('view')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, "You have been logged out")
        return redirect('login')