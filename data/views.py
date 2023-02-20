
from django.shortcuts import render
from rest_framework.response import Response
from .models import Summoner_rank, Champion, Deck, StandardDeck
from rest_framework.views import APIView
from .serializer import SummonerSerializer, ChampionSerializer, OneDeckSerializer, StandardSynergySerializer
from django.http import HttpResponse


class ChampionAPI(APIView):
    def get(self, request):
        queryset = Champion.objects.all().order_by('-fre')
        serializer = ChampionSerializer(queryset, many=True)
        time = Champion.objects.all().order_by('-updated_time')[0].updated_time
        time = f"{time.year}년{time.month}월{time.day}일{time.hour}시{time.minute}분"
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
        time = f"{time.year}년{time.month}월{time.day}일{time.hour}시{time.minute}분"
        serializer = {
            "updated_time" : time,
            "data" : serializer.data
        }
        return Response(serializer)

class OneDeckAPI_winrate(APIView):
    def get(self, request):
        queryset = Deck.objects.all().order_by("-winrate")[:10]
        serializer = OneDeckSerializer(queryset, many=True)
        time = Deck.objects.all().order_by('-updated_time')[0].updated_time
        time = f"{time.year}년{time.month}월{time.day}일{time.hour}시{time.minute}분"
        serializer = {
            "updated_time" : time,
            "data" : serializer.data
        }
        return Response(serializer)

class OneDeckAPI_windefencerate(APIView):
    def get(self, request):
        queryset = Deck.objects.all().order_by("-windefencerate")[:10]
        serializer = OneDeckSerializer(queryset, many=True)
        time = Deck.objects.all().order_by('-updated_time')[0].updated_time
        time = f"{time.year}년{time.month}월{time.day}일{time.hour}시{time.minute}분"
        serializer = {
            "updated_time" : time,
            "data" : serializer.data
        }
        return Response(serializer)

class OneDeckAPI_avgplace(APIView):
    def get(self, request):
        queryset = Deck.objects.all().order_by("avgplace")[:10]
        serializer = OneDeckSerializer(queryset, many=True)
        time = Deck.objects.all().order_by('-updated_time')[0].updated_time
        time = f"{time.year}년{time.month}월{time.day}일{time.hour}시{time.minute}분"
        serializer = {
            "updated_time" : time,
            "data" : serializer.data
        }
        return Response(serializer)


def riot(request):
    filename = "riot.txt"
    content = 'df00023e-6d26-4549-836c-ecfd264c7d78'
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response

def info(request):
    return render(request, 'data/info.html')

class SynergyAPI_winrate(APIView):
    def get(self, request):
        queryset = StandardDeck.objects.all().order_by("-fre")
        serializer = StandardSynergySerializer(queryset, many=True)
        time = StandardDeck.objects.all().order_by('-updated_time')[0].updated_time
        time = f"{time.year}년{time.month}월{time.day}일{time.hour}시{time.minute}분"
        serializer = {
            "updated_time" : time,
            "data" : serializer.data
        }
        return Response(serializer)