from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .form import RegForm, crimeform
from .models import CriminalTable, RegisterTable

# Create your views here.

class add_missing(View):
    def get(self, request):
        return render(request, "add missing.html")

class registration(View):
    def get(self,request):
        return render(request,"registration.html")
    def post(self, request):
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("registerd successfully"); window.location="/registration"</script>''')

           
class add_new_criminal(View):
    def get(self,request):
        return render(request,"add new criminal.html")  
    def post(self,request):
        form=crimeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("registered successfully"); window.location="/view_criminal"</script>''')


class Edit_criminal(View):
    def get(self,request,id):
        c=CriminalTable.objects.get(id=id)
        return render(request,"editcriminal.html",{'val':c})
    def post(self,request,id):
        c=CriminalTable.objects.get(id=id)
        form=crimeform(request.POST,request.FILES,instance=c)
        if form.is_valid():
            form.save()
            return redirect('view_criminal')
class complaint(View):
    def get(self,request):
        return render(request,"complaint.html") 
    

class view_criminal(View):
    def get(self,request):
        obj = CriminalTable.objects.all()
        return render(request,"criminal.html", {'val': obj})
 
class delete_c(View):
    def get(self, request, c_id):
        obj =  CriminalTable.objects.get(id=c_id)
        obj.delete()
        return HttpResponse('''<script>alert("delete successfully"); window.location="/view_criminal"</script>''')


class view_user(View):
    def get(self,request):
        obj =RegisterTable.objects.all()
        return render(request,"view users.html", {'val': obj})
    
class delete_u(View):
    def get(self, request, u_id):
        obj =view_userTable.objects.get(id=u_id)
        obj.delete()
        return HttpResponse('''<script>alert("delete successfully"); window.location="/view_user"</script>''')
