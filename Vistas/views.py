# HttpResponse is used to
# pass the information
# back to view
import requests

from django.shortcuts import render
from django.views import View
# Defining a function which
# will receive request and
# perform task depending
# upon function definition
class SecondView(View):
    def get(self, request):
        # get the list of todos
        response = requests.get('https://jsonplaceholder.typicode.com/photos/')
        # transfor the response to json objects
        photos = response.json()
        return render(request, "Vistas/list.html", {"photos": photos})

class MyView(View):
    def get(self, request):
              
        return render(request, "home.html")
