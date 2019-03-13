from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from .models import TodoItem, SubItem, Post
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
import csv, io, codecs
import pandas as pd
from pandas import DataFrame
import django_filters


# Create your views here.
# def todoView(request):
# 	all_todo_items = TodoItem.objects.all()
# 	return render(request, 'todo.html',
# 		{'all_items': all_todo_items})

#
# def addTodo(request):
# 	new_item = TodoItem(content=request.POST['content'])
# 	new_item.save()
# 	return HttpResponseRedirect('/')
#
# def deleteTodo(request, todo_id):
# 	item_to_delete = TodoItem.objects.get(id=todo_id)
# 	item_to_delete.delete()
# 	return HttpResponseRedirect('/')
#
# def subItemView(request):
# 	all_subItems = SubItem.objects.all()
# 	return render(request, 'subitem.html',
# 		{'all_subitems': all_subItems})
#
# def addSubItem(request):
# 	all_todo_items = TodoItem.objects.all()
# 	mainItem = all_todo_items[0]
# 	new_subitem = SubItem(title = request.POST['title'], mainItem = mainItem)
# 	new_subitem.save()
# 	return HttpResponseRedirect('/subItemView/')
#
# def deleteSubItem(request, subItem_id):
# 	subItem_to_delete = SubItem.objects.get(id=subItem_id)
# 	subItem_to_delete.delete()
# 	return HttpResponseRedirect('/subItemView/')

#then watch video of contrib auth
#then try for users and posts as relationship

def index(request):
	# return render(request, 'index.html')

	all_posts = Post.objects.all()
	return render(request, 'index.html', {'all_posts': all_posts})
	# return render(request, 'index.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()

	context = {'form': form}
	return render(request, 'registration/register.html', context)

###
def createPost(request):
	return render(request, 'createpost.html')

def addPost(request):
	user = request.user

	if user:
		title = request._post['title']
		description = request._post['description']
		source = request._post['source']
		keywords = request._post['keywords']
		dataset = request.FILES['csv_file']
		data = pd.read_csv(dataset)

		# try to get just first few cols and rows
		# dataset_crop = pd.read_csv(dataset, nrows=5)
		# if data.shape[0] > 3 & data.any():
		# dataset_crop = data[:2]
		# dataset_crop = data.iloc[0:2, 0:2]

		# 3/8
		cropped_dataset_a = data.iloc[:5, :4]
		data_crop_html = cropped_dataset_a.to_html()

		# use this code if breaks 3/8
		# dataset_crop = dataset

		# dataset_crop_a = data.head(5)
		# if dataset_crop_a is not None:
		# 	dataset_crop = dataset_crop_a


		# dataset_crop_b = dataset_crop_a.to_csv('out.csv')
		# dataset_crop_c = pd.read_csv(dataset_crop_b)
		# dataset_crop_d = dataset_crop_c.head(3)

			# 	dataset_crop = data.head[5]
		# count_row = data.shape[0]
		# count_col = data.shape[1]

		# if count_row > 3:
			# dataset_crop = data.head(5)
		# dataset_crop = data.iloc[1]


		data_html = data.to_html()
		new_post = Post(title=title, description=description, source=source, keywords=keywords, dataset=dataset, data_crop_html=data_crop_html, data_html=data_html, poster=user)

		# new_post = Post(title=title, description=description, dataset=dataset, poster=user)
		#new csv code
		# csvfile = request.files['csv_file']
		# dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
		# csvfile.open()
		# reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
		# new_post = Post(title=title, description=description, poster=user)
		# new_post = Post(title=request._post['title'], poster=user)

		new_post.save()
		id = request.user.id
		url = reverse('userPosts', args=[id])
		return HttpResponseRedirect(url)
		# return HttpResponseRedirect('/')
	else:
		# change this redirect to login page
		return HttpResponseRedirect('/')


def userPosts(request, user_id):
	user = User.objects.get(pk=user_id)
	context = {
		"user": user,
		"posts": user.tables.all()
	}
	return render(request, "userposts.html", context)
	# return render(request, "userposts.html")

def deletePost(request, post_id):
	post_to_delete = Post.objects.get(id=post_id)
	post_to_delete.delete()
	id = request.user.id
	url = reverse('userPosts', args=[id])
	return HttpResponseRedirect(url)

def searchResults(request):
	#add search logic here: precise match against keywords and titles?
	#so right below here put logic for taking all posts and only selecting where
	#word in title or keywrods starts with precise query term

	# 3/11 code
	query = request.GET['query']
	# filtered_posts = Post.objects.filter(keywords__icontains="brands")
	filtered_posts = Post.objects.filter(keywords__icontains=query)

	context = {
		# "query": request.GET['query'],
		"query": query,
		# "all_posts": Post.objects.all()
		"all_posts": filtered_posts
	}
	return render(request, 'searchResults.html', context)

def singleTable(request, post_id):
	post = Post.objects.get(pk=post_id)

	# dataset = pd.read_csv(post.dataset)
	# cropped_dataset_a = dataset.iloc[:5, :4]
	# cropped_dataset_b = cropped_dataset_a.to_html()

	context = {
		"post": post
		# "cropped_dataset": cropped_dataset_b
	}
	return render(request, "singleTable.html", context)