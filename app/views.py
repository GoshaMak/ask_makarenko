import copy
from random import shuffle

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

QUESTIONS = [
    {
        'title': f'title {i}',
        'id': i,
        'text': f'text for question {i}',
    } for i in range(30)
]


def paginate(objects_list, request, per_page=2):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(objects_list, per_page)
    page = paginator.page(page_num)
    return page


def index(request):
    page = paginate(QUESTIONS, request)

    return render(
        request,
        # 'question.html',
        'index.html',
        context={
            'questions': page.object_list,
            'page_obj': page,
        },
    )


def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    shuffle(hot_questions)

    page = paginate(hot_questions, request)

    return render(
        request,
        'hot.html',
        context={
            'questions': page.object_list,
            'page_obj': page,
        },
    )


def question(request, question_id):
    question_ = QUESTIONS[question_id]
    responds_ = QUESTIONS[0:2]
    return render(
        request,
        'question.html',
        context={
            'question': question_,
            'responds': responds_,
        },
    )


def signup(request):
    return render(
        request,
        'signup.html',
    )


def login(request):
    return render(
        request,
        'login.html',
    )


def ask(request):
    return render(
        request,
        'ask.html',
    )


def tag(request, main_tag):
    tag_questions = copy.deepcopy(QUESTIONS)
    shuffle(tag_questions)

    return render(
        request,
        'tag.html',
        context={
            'tag': main_tag,
            'tag_questions': tag_questions,
        },
    )
