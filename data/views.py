
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

def info(request):
    response = HttpResponse()
    response.write("<h1>Info</h1>")
    response.write("<p>api/summoner : ranker data</p>")
    response.write("<p>api/champion : champion statistics</p>")
    return response

def riot(request):
    file = open("./riot.txt")
    response = HttpResponse(file, content_type='text/plain')
    return response