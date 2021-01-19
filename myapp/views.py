from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    form = StudentRegistration()
    stud  = User.objects.all()
    return render(request,'myapp/add&show.html',{'form':form,'stud':stud})

# @csrf_exempt
def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if(sid==''):
                usr = User(name = name,email = email,password = password)
            else:
                usr = User(id=sid,name = name,email = email,password = password)
            usr.save()
            stud = User.objects.values()
            student_data = list(stud)
            return JsonResponse({'status':'Save','student_data':student_data})
        else:
            return JsonResponse({'status':0})

#this function will update

# def update_data(request, id):
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         pi = User.objects.get(pk=id)
#         fm = StudentRegistration(instance=pi)
#         return render(request, 'myapp/update.html',{'form':fm})

#this function will delete

def delete_data(request):
    if request.method ==  "POST":
        id = request.POST.get('sid')
        pi = User.objects.get(pk=id) #pk=primary key
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def edit_data(request):
    if request.method == "POST":
        id = request.POST.get("sid")
        student = User.objects.get(pk=id)
        student_data = {"id":student.id,"name":student.name,"email":student.email,"password":student.password}
        return JsonResponse(student_data)       