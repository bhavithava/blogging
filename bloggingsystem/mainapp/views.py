from django.shortcuts import render, get_object_or_404, redirect

from mainapp.models import BlogDetails


# Create your views here.
def blogpost(request):
    return render(request, 'mainapp/blogpost.html')

def add_blog_details(request):
    if request.method == 'POST':
        blogtitle = request.POST.get('blogtitle')
        blogtype = request.POST.get('blogtype')
        description = request.POST.get('description')
        location = request.POST.get('location')
        bloggerdetails = request.POST.get('bloggerdetails')

        blog_details = BlogDetails.objects.create(
            blogtitle=blogtitle,
            blogtype=blogtype,
            description=description,
            location=location,
            bloggerdetails=bloggerdetails,
        )
        blog_details.save()
        return render(request, 'mainapp/datainserted.html')
    return render(request, 'mainhomepage.html')

def view_blog_details(request):
    blog_details_list = BlogDetails.objects.all()
    return render(request, 'mainapp/view_blog_details.html',{'blog_details_list':blog_details_list})

def edit_blog_details(request, blog_id):
    blog_details = get_object_or_404(BlogDetails, id=blog_id)
    if request.method == 'POST':
        blog_details.blogtitle = request.POST.get('blogtitle')
        blog_details.blogtype = request.POST.get('blogtype')
        blog_details.description = request.POST.get('description')
        blog_details.location = request.POST.get('location')
        blog_details.bloggerdetails = request.POST.get('bloggerdetails')
        blog_details.save()
        return redirect('mainapp:view_blog_details')
    return render(request, 'mainapp/edit_blog_details.html',{'blog_details':blog_details})

def delete_blog_details(request, blog_id):
    blog_details = get_object_or_404(BlogDetails, id=blog_id)
    if request.method == 'POST':
        blog_details.delete()
        return redirect('mainapp:view_blog_details')
    return render(request, 'mainapp/edit_blog_details.html',{'blog_details':blog_details})

from userapp.models import OpenBlog
def comment_list(request):
    comment_list = OpenBlog.objects.all()
    return render(request, 'mainapp/comment_list.html', {'comment_list':comment_list})