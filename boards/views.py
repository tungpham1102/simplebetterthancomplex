from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewTopicForm
from .models import Board, Topic, Post


# Create your views here.


def home(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'boards/home.html', context)


# def board_topics(request, pk):
#     try:
#         board = Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         raise Http404
#
#     return render(request, 'boards/topics.html', {'board': board})


def board_topics(request, pk):
    boards = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/topics.html', {'boards': boards})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = user
            )
            return redirect('boards:board_topics', pk=board.pk) # Todo: redirect to the create topic page
    else:
        form = NewTopicForm()
        return render(request, 'boards/new_topic.html', {'form': form, 'board':board})
    return render(request, 'boards/new_topic.html', {'board': board})