
from django.shortcuts import render
from rest_framework.response import Response
from .models import Summoner_rank, Champion
from rest_framework.views import APIView
from .serializer import SummonerSerializer, ChampionSerializer



class ChampionAPI(APIView):
    def get(self, request):
        queryset = Champion.objects.all()
<<<<<<< HEAD
        serializer = ChampionSerializer(queryset, many=True)
        time = Champion.objects.all().order_by('-updated_time')[0].updated_time
        serializer = {
            "updated_time" : time,
            "data" : serializer.data
        }
        return Response(serializer)
=======
        # print(queryset)
        serializer = ChampionSerializer(queryset, many=True)
        return Response(serializer.data)
>>>>>>> 61f17bcd7104d2bbaacf7ecba4842ffebeeeb11d

class SummonerAPI(APIView):
    def get(self, request):
        queryset = Summoner_rank.objects.all()
<<<<<<< HEAD
        serializer = SummonerSerializer(queryset, many=True)
        time = Summoner_rank.objects.all().order_by('-updated_time')[0].updated_time
        serializer = {
            "updated_time" : time,
            "data" : serializer.data
        }
        return Response(serializer)
=======
        print(queryset)
        serializer = SummonerSerializer(queryset, many=True)
        return Response(serializer.data)
>>>>>>> 61f17bcd7104d2bbaacf7ecba4842ffebeeeb11d
