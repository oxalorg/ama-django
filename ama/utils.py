import os
import random

from django.conf import settings


random_name_file = 'endangered-animalia.txt'
def get_random_name():
    with open(os.path.join(settings.BASE_DIR, random_name_file)) as fp:
        return random.choice(fp.readlines())
