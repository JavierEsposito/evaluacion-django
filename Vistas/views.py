# HttpResponse is used to
# pass the information
# back to view
import requests

from django.shortcuts import render
from django.views import View

class SecondView(View):
    def get(self, request):
        response = requests.get('https://jsonplaceholder.typicode.com/photos/')
        photos = response.json()
        return render(request, "Vistas/list.html", {"photos": photos})

class MyView(View):
    def get(self, request):
        return render(request, "home.html")
