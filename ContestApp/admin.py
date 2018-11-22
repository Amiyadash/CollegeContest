from django.contrib import admin
from ContestApp.models import Contest,College,Challenge,View_Stats,Submission_Stats
# Register your models here.

admin.site.register(Contest)
admin.site.register(College)
admin.site.register(Challenge)
admin.site.register(View_Stats)
admin.site.register(Submission_Stats)