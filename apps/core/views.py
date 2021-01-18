from django.shortcuts import render
from django.views import View

# Create your views here.

class frontpage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/frontpage.html')

class privacy(View):
    def get(self, request, *args, **kwargs):
        return render(request, "core/privacy.html")

class terms(View):
    def get(self, request, *args, **kwargs):
        return render(request, "core/terms.html")

class plans(View):
    def get(self, request, *args, **kwargs):
        return render(request, "core/plans.html")