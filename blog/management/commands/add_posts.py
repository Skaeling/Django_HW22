from django.core.management.base import BaseCommand
from django.core.management import call_command
from blog.models import Post


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        Post.objects.all().delete()

        call_command('loaddata', 'posts_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfuly loaded data from fixture'))
