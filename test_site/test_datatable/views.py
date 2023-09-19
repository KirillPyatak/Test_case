import datetime
from django.shortcuts import render
from .models import Modalities, Studies
import random
from datetime import timedelta
import uuid
def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

def init_db(request):

    studies = Studies.objects.all()
    modalities = Modalities.objects.all()
    return render(request, 'test_datatable/init_db.html', {'studies': studies, 'modalities': modalities})

