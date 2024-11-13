from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from app.models import Question, Answer, Tag, QuestionLike


def paginate(objects_list, request, attr='page', per_page=4):
    page_num = str(request.GET.get(attr, 1))

    page_num = int(page_num) if page_num.isdigit() else 1
    page_num = 1 if page_num <= 0 or page_num > len(objects_list) else page_num

    paginator = Paginator(objects_list, per_page)
    page = paginator.page(page_num)
    return page


def index(request):
    questions = []
    for q in Question.objects.new():
        questions.append(
            {
                'question': q,
                'tags': q.tags.all(),
                'answers_amt': len([ans for ans in Answer.objects.all() if ans.question.id == q.id]),
            }
        )
    # questions = Question.objects.new()
    # Tag.objects.add_tags(questions)
    # Question.objects.add_answers_amt(questions, Answer.objects.all())

    page = paginate(questions, request, attr='')

    return render(
        request,
        'index.html',
        context={
            'questions': page.object_list,
            'page_obj': page,
        },
    )


def hot(request):
    questions = []
    for q in Question.objects.best():
        questions.append(
            {
                'question': q,
                'tags': q.tags.all(),
                'answers_amt': len([ans for ans in Answer.objects.all() if ans.question.id == q.id]),
            }
        )

    page = paginate(questions, request)

    return render(
        request,
        'hot.html',
        context={
            'questions': page.object_list,
            'page_obj': page,
        },
    )


def question(request, question_id):
    try:
        question_ = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404

    answers = [ans for ans in list(Answer.objects.all()) if ans.question.id == question_id]
    tags = question_.tags.all()

    return render(
        request,
        'question.html',
        context={
            'question': question_,
            'responds': answers,
            'tags': tags,
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
    tag_questions = []
    # def questions_by_tag(main_tag)
    for q in Question.objects.all():
        for tag_ in q.tags.all():
            if tag_.name == main_tag:
                tag_questions.append(
                    {
                        'question': q,
                        'tags': q.tags.all(),
                        'answers_amt': len([ans for ans in Answer.objects.all() if ans.question.id == q.id])
                    }
                )
                break

    return render(
        request,
        'tag.html',
        context={
            'tag': main_tag,
            'tag_questions': tag_questions,
            'answers_amt': len([ans for ans in Answer.objects.all() if ans.question.id == q.id])
        },
    )
