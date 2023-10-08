from django.shortcuts import render,redirect
from bookms.forms import BooksForm
from bookms.models import Books

# Create your views here.
def getAllBooks(request):
    booksms=Books.objects.all()
    print("Hello everybody")
    return render(request,"index.html",{"Booksms": booksms})
def addBooksms(request):
    if request.method=="POST":
        form1=BooksForm(request.POST)
        print(form1.is_valid())
        if form1.is_valid():
            try:
                form1.save()
                return redirect("/get-all-books")
            except:
                pass
            else:
                print("something went to wrong")
    else:
        form1=BooksForm()
        return render(request,"addbooks.html",{'form':form1})
    def delete(request,id):
        bookms=Books.objects.get(id=id)#select* from bookms where id=1
        bookms.delete()
        return redirect("/get-all-books")
    def edit(request, id):
        bookms = Books.objects.get(id=id)
        return render(request,"edit.html",{'bookms': bookms})
def update(request, id):
    bookms = Books.objects.get(id=id)
    form1 = BooksForm(request.POST,isinstance=bookms)
    if form1.is_valid():
        try:
            form1.save()
            return redirect("/get-all-books")
        except:
            pass
        else:
            print("something went to wrong")
        return render(request, "edit.html", {'bookms': bookms})