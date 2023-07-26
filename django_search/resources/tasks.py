
from .models import Resource

def parse_resources():
    resources = Resource.objects.all()
    for resource in resources:
        resource.parse()