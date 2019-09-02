#from django.shortcuts import render

#def index(request):
 #   """home page"""
 #   return render(request, 'index1.html')

# Create your views here.

from django.shortcuts import render

# Create your views here.
def index(request):
    """learning logs homepage"""
    return render(request, 'meal_planner_app/index.html')

def help(request):
    """learning logs homepage"""
    return render(request, 'meal_planner_app/help.html')

