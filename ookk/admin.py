from django.contrib import admin
from ookk.models import Apost,Apublisher

class ApostAdmin(admin.ModelAdmin):
    fields=('subject','pimageA')
admin.site.register(Apost,ApostAdmin)


class ApublisherAdmin(admin.ModelAdmin):
    fields=('user','advtext','advimage')
admin.site.register(Apublisher,ApublisherAdmin)
