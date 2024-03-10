from django.shortcuts import render
from .models import *
# Create your views here.
def viewblogs(request):
    return render(request, 'userapp/viewblogs.html')

from mainapp.models import BlogDetails
from django.contrib.auth.decorators import login_required
@login_required(login_url='login1')
def blog_details_list(request):
    blog_details_list = BlogDetails.objects.all()
    return render(request, 'userapp/viewblogs.html', {'blog_details_list': blog_details_list})

def adduserprofile(request):
    return render(request, 'userapp/adduserprofile.html')

def submit_form(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        phone_number = request.POST['phone_number']
        date_of_birth = request.POST['date_of_birth']
        bio = request.POST['bio']

        user = User(first_name=firstname,
                    last_name=lastname,
                    phone_number=phone_number,
                    date_of_birth=date_of_birth,
                    bio=bio)
        user.save()
        return render(request, 'userhomepage.html')
    return render(request, 'userhomepage.html')

from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import *
def open_blog(request,blog_id):
    blog_details = get_object_or_404(BlogDetails, id=blog_id)
    if request.method == 'POST':
        form = OpenBlogForm(request.POST, request.FILES)
        if form.is_valid():
            open_blog = form.save(commit=False)
            open_blog.blog_details = blog_details
            open_blog.save()

            subject = 'Blog Opened Successfully'
            message = 'Thank you for Viewing our blog'
            from_email='vbhavitha1506@gmail.com'
            send_mail(subject, message, from_email)

        return redirect('userapp:blog_details_list')
    else:
        form = OpenBlogForm()

    return render(request, 'userapp/open_blog.html', {'BlogDetails':blog_details, 'form':form})

