from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contest,College,Challenge,View_Stats,Submission_Stats
from .serializers import ContestSerializer,CollegeSerializer,ChallengeSerializer,ViewSerializer,SubSerializer

# Create your views here.

class ContestView(APIView):
    def get(self,request,format=None):
        contests=Contest.objects.all()
        serializer=ContestSerializer(contests,many=True)
        return Response(serializer.data)


