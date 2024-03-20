from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    return render(request, "main/index.html", {})


def training(request):
    return render(request, "main/trainings.html", {})

def eqpt(request):
    return render(request, "main/eqpt.html", {})