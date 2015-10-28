from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker


def generate_activities():
    from faker import Faker
    import json
    fake = Faker()
    activities = []
    for user in User.objects.all():
        for _ in range(5):
            activity = {'fields': {'activity_name': fake.catch_phrase(),
                                   'start_date': "2015-09-30",
                                   'user': user.pk},
                        'model': 'api.Activity', }
            activities.append(activity)
    with open('./api/fixtures/activities.json', 'w') as f:
        f.write(json.dumps(activities))

def generate_logs():
    from faker import Faker
    import json
    import random
    fake = Faker()
    logs = []
    for user in User.objects.all():
        for activity in user.activities.all():
            for date in ['2015-10-0{}'.format(day) for day in range(1,10)]
                log = {'fields': {'activity': activity,
                                  'activity_date': date,
                                  'activity_count': random.choice(range(1, 5))},
                       'model': 'api.Log', }
                logs.append(log)
    with open('./api/fixtures/logs.json', 'w') as f:
        f.write(json.dumps(logs))


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_activities()
        generate_logs()
