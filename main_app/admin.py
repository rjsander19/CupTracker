from django.contrib import admin
from .models import Cup
from .models import Cup, Use, Content

admin.site.register(Cup)
admin.site.register(Use)
admin.site.register(Content)