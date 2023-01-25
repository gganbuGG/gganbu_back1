
from django.shortcuts import render
from rest_framework.response import Response
from .models import Summoner_rank, Champion
from rest_framework.views import APIView
from .serializer import SummonerSerializer, ChampionSerializer



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
