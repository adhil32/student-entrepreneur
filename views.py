from django.shortcuts import render
def home(request):
    return render(request,'app1/home.html')
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        
    return render(request,'app1/signup.html')
def signin(request):
    return render(request,'app1/signin.html')
def signout(request):
    return render(request,'app1/signout.html')




