from django.shortcuts import render, HttpResponse, redirect
from myApp.models import *

def index(request):
    return render(request,'index.html')


def listportfolio(request):
    alluser=customuser.objects.all()
    return render(request,'listportfolio.html',{'users':alluser})


def portfolio(request,myid):
    userportfolio=customuser.objects.get(id=myid)
    myDict={
        'userportfolio':userportfolio
    }
    return render(request,'portfolio.html',myDict)

def profile(request):
    return render(request,'profile.html')

def editprofile(request):
    current_user=request.user
    if request.method == 'POST':
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        image=request.FILES.get('image')
        phone=request.POST.get('phone')
        skills=request.POST.get('skills')
        work_experience=request.POST.get('work_experience')
        education=request.POST.get('education')
        address=request.POST.get('address')
        city=request.POST.get('city')
        country=request.POST.get('country')
        about=request.POST.get('about')
        
        current_user.full_name=full_name
        current_user.email=email
        current_user.phone=phone
        current_user.skills=skills
        current_user.work_experience=work_experience
        current_user.education=education
        current_user.address=address
        current_user.city=city
        current_user.country=country
        current_user.about=about
        if image:
            current_user.image=image
        current_user.save()
        return redirect("profile")
    return render(request,'editprofile.html')



from django.contrib.auth import authenticate, login, logout

def signin(requset):
    if requset.method == 'POST':
        username=requset.POST.get('username')
        password=requset.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            login(requset,user)
            return redirect("listportfolio")
        
    return render(requset,'signin.html')


def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            user=customuser.objects.create_user(username=username, password=password)
            user.full_name=full_name
            user.email=email
            user.phone=phone
            user.save()
            return redirect("signin")
    return render(request,'signup.html')

def signout(request):
    logout(request)
    return redirect("signin")


from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
def contact_user(request, myid):
    userportfolio = get_object_or_404(customuser, id=myid)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Construct the message
        subject = f"New Contact from {name}"
        body = f"Message from {name} ({email}):\n\n{message}"


        send_mail(
            subject,
            body,
            email,  
            [userportfolio.email],     
            fail_silently=False,
        )

        return HttpResponse('Thank you for contacting!')

    return render(request, 'contact.html', {'userportfolio': userportfolio})