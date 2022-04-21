from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from eithers.forms import QuestionForm, CommentForm
from .models import Question, Comment
from random import *

# 메인화면
def index(request):
    questions = Question.objects.order_by('-pk')
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)

# 랜덤 페이지 번호 생성
def random(request):
    q_num = Question.objects.count()
    num = randint(1, q_num)

    return redirect('eithers:detail', num)


# 글작성
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():  # 유효성 검사
            question = form.save()
            return redirect('eithers:index')
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)


@require_safe
def detail(request, pk):
    
    question = get_object_or_404(Question, pk=pk)
    comment_form = CommentForm()
    comments = question.comment_set.all()
    if comments.count() != 0:
        Red = round((comments.filter(pick = 'Red').count())/comments.count() * 100, 2)
        Blue = round((comments.filter(pick = 'Blue').count())/comments.count() * 100, 2)

    else:
        Red = 0
        Blue = 0

    context = {
        'question': question,
        'comment_form' : comment_form,
        'comments' : comments,
        'Red' : Red,
        'Blue' : Blue,
    }

    return render(request, 'eithers/detail.html', context)

@require_POST
def comment_create(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.que = question
        comment.save()
    return redirect('eithers:detail', question.pk)

    
    