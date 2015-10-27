from django.core.management.base import BaseCommand
from faker import Faker


def generate_activities():
    from faker import Faker
    import json
    fake = Faker()
    activities = []
    for _ in range(50):
        activity = {'fields': {'activity_name': fake.catch_phrase(),
                               'start_date': str(fake.date_time_this_month())[:10]},
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
    for _ in range(250):
        log = {'fields': {'activity': random.choice(range(1, 51)),
                          'activity_date': str(fake.date_time_this_month())[:10],
                          'activity_count': random.choice(range(1, 5))},
               'model': 'api.Log', }
        logs.append(log)
    with open('./api/fixtures/logs.json', 'w') as f:
        f.write(json.dumps(logs))


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_activities()
        generate_logs()
