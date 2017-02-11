from urllib import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import posts
from .forms import PostForm
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
# Create your views here.

'''
post_create = dynamic url 
post_detail = listing of articles
post_list = form
post_update = edit article
post_delete = delte post

'''

def post_create(request, id=None):
	instance = get_object_or_404(posts, id=id)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)
	context = {
		"title" : instance.title,
		"instance" : instance,
		"share_string" : share_string
	}
	return render(request, "post_detail.html", context)

def post_detail(request):
	today = timezone.now().date()
	queryset_list = posts.objects.active()
	if request.user.is_staff or request.user.is_superuser:
		queryset = posts.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(user__first_name__icontains=query)|
			Q(user__last_name__icontains=query) ).distinct()
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request = "posts"
	page = request.GET.get(page_request)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"title" : "loged in",
		"obj_list" : queryset,
		"page_request" : page_request,
		"today" : today
	}
	return render(request, "post_lists.html", context)





def post_list(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "changes are saved")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form" : form,
	}
	return render(request, "post_form.html", context)

def post_update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(posts, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "changes saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title" : instance.title,
		"instance" : instance,
		"form" : form
	}
	return render(request, "post_form.html", context)

def post_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(posts, id=id)
	instance.delete()
	messages.success(request, "changes are saved")
	return redirect("/posts/detail")