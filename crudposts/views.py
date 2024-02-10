import requests
from django.shortcuts import render
from django.core.paginator import Paginator

def list_posts(request):
    api_url = 'http://jsonplaceholder.typicode.com/posts'
    users_url = 'http://jsonplaceholder.typicode.com/users'
    response = requests.get(api_url)
    users_response = requests.get(users_url)
    posts = response.json()
    users = users_response.json
    return render(request, 'list_posts.html', {'posts': posts, 'users': users})

def post_detail(request, post_id):
    api_url = f'http://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.get(api_url)
    post = response.json()
    # Fetch comments associated with the post
    comments_url = f'http://jsonplaceholder.typicode.com/posts/{post_id}/comments'
    comments_response = requests.get(comments_url)
    comments = comments_response.json()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})

def paginate_posts(request):
    page_number = request.GET.get('p', '')
    api_url = 'http://jsonplaceholder.typicode.com/posts'
    users_url = 'http://jsonplaceholder.typicode.com/users'
    response = requests.get(api_url)
    users_response = requests.get(users_url)
    posts = response.json()
    users = users_response.json()
    paginator = Paginator(posts, 10)  # 10 posts per page
    page = paginator.get_page(page_number)
    return render(request, 'list_posts.html', {'posts': page, 'users': users})

def search_posts(request):
    query = request.GET.get('q', '')
    api_url = f'http://jsonplaceholder.typicode.com/posts?q={query}'
    users_url = 'http://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url)
    response = requests.get(api_url)
    users = users_response.json()
    posts = response.json()
    return render(request, 'search.html', {'posts': posts, 'users': users})

def delete_post(request, post_id):
    api_url = f'http://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.delete(api_url)
    if response.status_code == 200:
        # Handle successful deletion
        return HttpResponse('Post deleted successfully')
    else:
        # Handle deletion failure
        return HttpResponse('Failed to delete post', status=response.status_code)
