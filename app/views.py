# Django's imports
from django.shortcuts import render

# Developer's imports
from django.contrib.auth.decorators import login_required

# Model's imports
from .models import Channel, Content
from accounts.models import CustomUser

# Forms' imports
from .forms import PostForm


# Central view, where the user will be redirected after login
@login_required
def index(request):
    context = {
        "channel": Channel.objects.all(),
    }
    return render(request, "index.html", context)


@login_required
def channel(request, pk):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    user = CustomUser.objects.all()
    sidebar = Channel.objects.all()
    channel = Channel.objects.get(id=pk)
    content = Content.objects.all()
    form = PostForm()

    context = {
        'user': user,
        "sidebar": sidebar,
        "channel": channel,
        "form": form,
        "content": content,
    }

    return render(request, "channel.html", context)
