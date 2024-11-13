from django.core.management import BaseCommand
from app.models import *


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("ratio", nargs="+", type=int)

    def handle(self, *args, **options):
        ratio = options["ratio"][0]
        data = {
            "users_amt": 10_000 * ratio,
            "questions_amt": 100_000 * ratio,
            "answers_amt": 1_000_000 * ratio,
            "tags_amt": 10_000 * ratio,
            "likes_amt": 2_000_000 * ratio,
        }

        user = Profile.objects.first().user
        self.stdout.write(f"{Question.objects.all()[1].tags.all()}")
