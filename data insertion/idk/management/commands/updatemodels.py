from django.core.management.base import BaseCommand
import pandas as pd
from idk.models import ExlData


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Database connections
        df = pd.read_csv('Book2.csv')
        for AGE, FARE, NAME, GITHUB in zip(df.Age, df.Fare, df.Name):
            models = ExlData(age=AGE, fare=FARE, name=NAME)
            models.save()
