from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        student_list = [
            {'last_name': 'Petrov', 'first_name': 'Petr'},
            {'last_name': 'Ivanov', 'first_name': 'Ivan'},
            {'last_name': 'Semenov', 'first_name': 'Semen'},
            {'last_name': 'Aleksandrov', 'first_name': 'Aleksandr'},
        ]

        # for student_item in student_list:             #способ добавления по одному
        #     Student.objects.create(**student_item)

        student_for_create = []
        for student_item in student_list:
            student_for_create.append(
                Student(**student_item)
            )
        Student.objects.bulk_create(student_for_create) #способ добавления сразу пакетом bulk_create()
