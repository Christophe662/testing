from django.shortcuts import render


# Create your views here.
def projects_view(request):
    #return HttpResponse ('Contacter nous')
     return render(request,'mesprojets/list.html')
