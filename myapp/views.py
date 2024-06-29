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

def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]    
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "บันทึกข้อมูลเรียบร้อย")
        # เปลี่ยนเส้นทาง
        return redirect("/")
    else:        
        # ดึงข้อมูลประชากรที่ต้องการแก้ไข
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html", {"person": person})
    
def delete(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request, "ลบข้อมูลเรียบร้อย")
        # เปลี่ยนเส้นทาง
    return redirect("/")