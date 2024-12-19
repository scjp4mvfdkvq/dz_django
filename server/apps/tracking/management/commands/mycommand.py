from django.core.management.base import BaseCommand
from argparse import ArgumentParser

class Command(BaseCommand):
    help = 'Команда для вывода имени пользователя в консоль'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help='Имя пользователя')

    def handle(self, *args, **options):
        name = options['name']
        self.stdout.write(f'Приветствую, {name}!')