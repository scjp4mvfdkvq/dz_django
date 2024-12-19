from django.core.management import CommandError

try:
    from .mycommand import Command
except ImportError:
    raise CommandError('Error importing command')

__all__ = ['Command']
