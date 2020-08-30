from django.shortcuts import render, get_object_or_404

from . models import Blog

# Create your views here.
def allblogs(request):

	blogs= Blog.objects
	return render(request,'blogs/allblogs.html',{'blogs':blogs})

def details(request,blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blogs/details.html',{'blog':detail_blog})