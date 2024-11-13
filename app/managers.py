from django.db import models


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by("-created_at")
        # questions = []
        # for q in self.order_by("-created_at"):
        #     questions.append({'question', q})
        # return questions

    def best(self):
        return self.annotate(like_count=models.Count('questionlike')).order_by('-like_count')

#     def add_answers_amt(self, questions, answers):
#         for q in questions:
#             q.add('answers_amt', len([ans for ans in answers if ans.question.id == q.id]))
#
#
# class TagManager(models.Manager):
#     def add_tags(self, a):
#         for elem in a:
#             elem.add('tags', elem.tags.all())
