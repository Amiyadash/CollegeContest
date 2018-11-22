from django.db import models

# Create your models here.


class Contest(models.Model):
    contest_id=models.IntegerField(primary_key=True)
    hacker_id=models.IntegerField()
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name
class College(models.Model):
    contest_id=models.ForeignKey(Contest,on_delete=models.CASCADE)
    college_id = models.IntegerField(primary_key=True)

    def __unicode__(self):
        return self.college_id
class Challenge(models.Model):
    challenge_id=models.IntegerField(primary_key=True)
    college_id=models.ForeignKey(College,on_delete=models.CASCADE)

    def __int__(self):
        return self.challenge_id
class View_Stats(models.Model):
    Challenge_id=models.ForeignKey(Challenge,on_delete=models.CASCADE)
    total_view=models.IntegerField(max_length=10)
    total_unique_view = models.IntegerField(max_length=10)
class Submission_Stats(models.Model):
    Challenge_id=models.ForeignKey(Challenge,on_delete=models.CASCADE)
    total_submission =models.IntegerField(max_length=10)
    total_accepted_submissions= models.IntegerField(max_length=10)



