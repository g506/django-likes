from django.shortcuts import render

# Create your views here.
  
def likes_view(request): 

    return render(request, "likes.html") 