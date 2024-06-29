from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    personals = Person.objects.all()
    return render(request, "index.html", {"personals": personals})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        # รับข้อมู
        name = request.POST["name"]
        age = request.POST["age"]
        # บันทึกข้อมูล
        person = Person.objects.create(
            name = name,
            age = age
        )
        person.asave()
        messages.success(request, "บันทึกข้อมูลเรียบร้อย")
        # เปลี่ยนเส้นทาง
        return redirect("/")
    else:        
        return render(request, "form.html")

def edit(requst, person_id):
    if requst.method == "POST":
        person = Person.objects.get(id=person_id)
        print(person.name)
        person.name = requst.POST["name"]    
        person.age = requst.POST["age"]
        person.save()
        messages.success(request, "บันทึกข้อมูลเรียบร้อย")
        # เปลี่ยนเส้นทาง
        return redirect("/")
    else:        
        # ดึงข้อมูลประชากรที่ต้องการแก้ไข
        person = Person.objects.get(id=person_id)
        print(person.name)
        return render(requst, "edit.html", {"person": person})