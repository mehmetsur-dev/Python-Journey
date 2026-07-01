from django.shortcuts import render

posts = [
    {
        'author': 'Mehmet Sur',
        'title': 'Blog poste',
        'content': 'First poste content',
        'date_posted': 'Aug 27, 2025'
    },
    {
        'author': 'SeraCl',
        'title': 'Blog poste 2',
        'content': 'Second poste content',
        'date_posted': 'Aug 28, 2025'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context,)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
