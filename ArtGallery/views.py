from django.shortcuts import render,redirect
from django.views import View
from .models import Art
from .forms import ArtForm

class Index(View):
  def get(self,request):
    return redirect('/read')

class CreateEntry(View):
  def get(self,request):
    form = ArtForm()  
    return render(request,'create.html',{'form':form})
  
  def post(self,request):
    form = ArtForm(request.POST,request.FILES) 

    if form.is_valid():
      form.save()  
      return redirect('/')  

    form = ArtForm()

class ReadEntry(View):
  def get(self,request):
    art=Art.objects.all()
    for i in art:
      if i.arttype=="P":
        i.arttype="Painting"
      if i.arttype=="S":
        i.arttype="Sketching"
      if i.arttype=="O":
        i.arttype="Other"
      if i.arttype=="N":
        i.arttype="None"
    return render(request,'read.html',{'arts':art})

class UpdateEntry(View):
  def get(self, request,id):
    art = Art.objects.get(id=id)
    return render(request,'update.html', {'art':art})
  
  def post(self,request,id):
    print(request)
    art = Art.objects.get(id=id)  
    for i in request.POST:
      if i == 'title':
        if art.title != request.POST['title']:
          print(request)
          art.title = request.POST['title']
      if i == 'arttype':
        if art.arttype != request.POST['arttype']:
          print(request.POST['arttype'])
          art.arttype = request.POST['arttype']
      if i == 'saleStatus':
        if art.saleStatus != request.POST['saleStatus']:
          print(request.POST['saleStatus'])
          art.saleStatus = request.POST['saleStatus']
      if i == 'quantity':
        if art.quantity != request.POST['quantity']:
          print(request.POST['quantity'])
          art.quantity = request.POST['quantity']
      if i == 'price':
        if art.price != request.POST['price']:
          print(request.POST['price'])
          art.price = request.POST['price']
      if i == 'date':
        if art.date != request.POST['date'] and request.POST['date'] != '':
          print(request.POST['date'])
          art.date = request.POST['date']
      if i == 'desc':
        if art.desc != request.POST['desc'] and request.POST['desc'] != '':
          print(request.POST['desc'])
          art.desc = request.POST['desc']
    

    for i in request.FILES:
      if i == 'artImg':
        if request.FILES['artImg'] != '':
          art.artImg = request.FILES['artImg']
    
    art.save()
    return redirect("/read")  




class DeleteEntry(View):
    def get(self,request,id):
        art = Art.objects.get(id=id)  
        art.delete()  
        return redirect("/read")      

