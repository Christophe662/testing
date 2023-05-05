from django.shortcuts import render

# Create your views here.

def mycv_view(request):
    #return HttpResponse ('Contacter nous')
     return render(request,'moncv/list.html')