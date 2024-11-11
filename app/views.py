import copy
from random import shuffle

from django.core.paginator import Paginator
from django.shortcuts import render

QUESTIONS = [
    {
        'title': f'title {i}',
        'id': i,
        'text': f'text for question {i}',
    } for i in range(30)
]


def paginate(objects_list, request, attr='page', per_page=4):
    page_num = str(request.GET.get(attr, 1))

    page_num = int(page_num) if page_num.isdigit() else 1
    page_num = 1 if page_num <= 0 or page_num > len(objects_list) else page_num

    paginator = Paginator(objects_list, per_page)
    page = paginator.page(page_num)
    return page


def index(request):
    page = paginate(QUESTIONS, request, attr='')

    print(f"{page=}")

    return render(
        request,
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
    if not str(question_id).isdigit():
        question_id = QUESTIONS[0]['id']
    if not question_id in [q['id'] for q in QUESTIONS]:
        question_id = int(question_id)

    question_ = QUESTIONS[question_id]
    responds_ = QUESTIONS[0:2]  # question answers

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


def settings(request):
    return render(
        request,
        'settings.html',
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
