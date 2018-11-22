from rest_framework import serializers
from ContestApp.models import Contest,College,Challenge,View_Stats,Submission_Stats

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contest
        fields=('contest_id','hacker_id','name')
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model=College
        fields=('contest_id','college_id')
class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Challenge
        fields=('challenge_id','college_id')
class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=View_Stats
        field=('Challenge_id','total_view','total_unique_view')
class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model=Submission_Stats
        fields=('Challenge_id','total_submission','total_accepted_submissions')