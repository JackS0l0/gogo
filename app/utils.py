from articles.models import Locations
from main.models import MainSettings
def common_data():
    return{
        'locations':Locations.objects.all().order_by('name'),
        'ms':MainSettings.objects.all(),
    }