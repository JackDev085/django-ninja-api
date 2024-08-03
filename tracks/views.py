from django.shortcuts import render

def form(request):
  if request.method =="POST":
    pass
  return render(request, "form.html")