from django.core.management.base import BaseCommand, CommandError
from application.models import Post, Category
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'deletes all the posts of a selected category'

    def add_arguments(self, parser):
        parser.add_argument('categories', type=str)

    def handle(self, *args, **options):
        category = options['categories']
        posts = Post.objects.filter(categories=category)
        posts.delete()
        self.stdout.write(self.style.SUCCESS(f'Posts of category {category} were successfully deleted'))

# python3 manage.py deleteposts 2     --number represents a category, does not work if write --categories=politics


