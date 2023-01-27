
from django.shortcuts import render
from rest_framework.response import Response
from .models import Summoner_rank, Champion
from rest_framework.views import APIView
from .serializer import SummonerSerializer, ChampionSerializer
from django.http import HttpResponse



class ChampionAPI(APIView):
    def get(self, request):
        queryset = Champion.objects.all()
        serializer = ChampionSerializer(queryset, many=True)
        time = Champion.objects.all().order_by('-updated_time')[0].updated_time
        serializer = {
            "updated_time" : time,
            "data" : serializer.data
        }
        return Response(serializer)

class SummonerAPI(APIView):
    def get(self, request):
        queryset = Summoner_rank.objects.all()
        serializer = SummonerSerializer(queryset, many=True)
        time = Summoner_rank.objects.all().order_by('-updated_time')[0].updated_time
        serializer = {
            "updated_time" : time,
            "data" : serializer.data
        }
        return Response(serializer)

def riot(request):
    filename = "riot.txt"
    content = '51ebe893-3b0b-4f97-8906-aa3da442230a'
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response

def info(request):
    return render(request, 'data/info.html')
