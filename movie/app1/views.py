from django.shortcuts import render,redirect

# Create your views here.
from app1.models import Movie

from app1.forms import MovieForm
from django.urls import reverse_lazy

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
#
# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'movie':k})
class Home(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="movie"


    def get_queryset(self):
        qs=super().get_queryset()
        # queryset=qs.filter(title="Amaran")
        queryset=qs.filter(title__icontains="a")
        # queryset=qs.filter(year__gt=2014)
        # queryset = qs.filter(year__lt=2023)
        # queryset=qs.filter(title__startswith="a")
        return queryset


    # def get_context_data(self):
    #     context=super().get_context_data()
    #     context['name']="Arun"
    #     context['Age']=25
    #     return context

    extra_context={'name':'Arun','age':24}

# def addmovies1(request):
#     if(request.method=="POST"):
#         form=MovieForm(request.POST,request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#     form=MovieForm()
#     context={'form':form}
#     return render(request,'add1.html',context)

# def addmovie(request):
#     if(request.method=="POST"):
#         t=request.POST['t']
#         d=request.POST['d']
#         y=request.POST['y']
#         l=request.POST['l']
#         i=request.FILES.get('i')
#
#         m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
#         m.save()
#         return home(request)
#     return render(request,'add.html')

# def details(request,t):
#     k=Movie.objects.get(id=t)
#     return render(request,'details.html',{'movie':k})


class AddMovie(CreateView):
    model=Movie
    fields=['title','description','year','language','image']
    template_name="add1.html"
    context_object_name="movie"
    success_url=reverse_lazy('app1:home')

class Detail(DetailView):
    model=Movie
    template_name="details.html"
    context_object_name="movie"





# def edit(request,m):
#     k=Movie.objects.get(id=m)
#     if (request.method=="POST"):
#         k.title=request.POST['t']
#         k.description=request.POST['d']
#         k.year=request.POST['y']
#         k.language=request.POST['l']
#         k.image=request.FILES.get('i')
#
#
#         if(request.FILES.get('i')==None):
#             k.save()
#         else:
#             k.image=request.FILES['i']
#             k.save()
#             return Home(request)
#
#     return render(request,'edit.html',{'movie':k})
class Update(UpdateView):
    model=Movie
    fields=['title','description','year','language','image']
    template_name="edit.html"
    success_url=reverse_lazy('app1:home')

# def delete(request,h):
#     k=Movie.objects.get(id=h)
#     k.delete()
#     return Home(request)

class Delete(DeleteView):
    model=Movie
    template_name="delete.html"
    success_url=reverse_lazy('app1:home')
