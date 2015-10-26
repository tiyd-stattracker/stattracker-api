from django.core.management.base import BaseCommand
from faker import Faker



fake = Faker()


def generate_activities():
    from faker import Faker
    import json
    import random
    fake = Faker()
    activities = []
    for _ in range(50):
        activity = {'fields':{'activity_name':fake.catch_phrase(),
                              'activity_date':str(fake.date_time_this_month())[:10],
                              'activity_count':random.choice(range(1,5))},
                    'model':'api.Activity',}
        activities.append(activity)
    with open('./api/fixtures/activities.json', 'w') as f:
        f.write(json.dumps(activities))

class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_activities()
