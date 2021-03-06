from django.shortcuts import render, redirect,get_object_or_404, HttpResponseRedirect
from .models import Category, Photo
from django.contrib import messages


# Create your views here.
def welcome(request):

    return render(request, 'photos/base.html')
def gallery(request):

    category = request.GET.get('category')
    if category == None:
       photos = Photo.objects.all()
    
    else:
        photos = Photo.objects.filter(category__name__contains=category)

    categories = Category.objects.all()
    # photos = Photo.objects.all()

    context = {'categories': categories, 'photos': photos}

    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo':photo})

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none': 
            category = Category.objects.get(id=data['category'])

        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])

        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image = image,
        )

        messages.info(request, 'Photo added successfully!')
        return redirect('gallery')

    context = {'categories': categories }

    return render(request, 'photos/add.html',context)


def deletePhoto(request, pk):
    
    if request.method == 'POST':
        instance = Photo.objects.get(pk =pk)
        instance.delete()
        print('photo deleted')

        messages.info(request, 'Photo deleted successfully!')

        return redirect('gallery')

    else:
        return render(request, 'photos/photo.html')        

    
def updatePhoto(request):
    if request == 'POST':
        replace = Photo.objects.get()
        replace.update()
        print('Photo replaced!')

    else:
        return render(request, 'photos/update.html')        
