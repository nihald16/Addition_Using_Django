from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        a=int(request.POST['num1'])
        b=int(request.POST['num2'])
        c=a+b
        print(c)
    return render(request,'index.html')
