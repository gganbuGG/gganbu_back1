from data.models import Match
from django.core.management.base import BaseCommand

def convert_unixtime(date_time):
    """Convert datetime to unixtime"""
    import datetime
    unixtime = datetime.datetime.strptime(date_time,
                               '%Y-%m-%d %H:%M:%S').timestamp()
    return int(unixtime)
class Command(BaseCommand):
    help = "match Data에서 덱 데이터 저장"
    def handle(self, *args, **kwargs):
        
