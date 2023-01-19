
from django.shortcuts import render
from rest_framework.response import Response
from .models import Summoner_rank, Champion
from rest_framework.views import APIView
from .serializer import SummonerSerializer, ChampionSerializer



class ChampionAPI(APIView):
    def get(self, request):
        queryset = Champion.objects.all()
        # print(queryset)
        serializer = ChampionSerializer(queryset, many=True)
        return Response(serializer.data)

class SummonerAPI(APIView):
    def get(self, request):
        queryset = Summoner_rank.objects.all()
        print(queryset)
        serializer = SummonerSerializer(queryset, many=True)
        return Response(serializer.data)
