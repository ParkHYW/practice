from django.contrib import admin
from .models import Blog
from .models import Friends
from .models import Team
# Register your models here.

admin.site.register(Blog)
admin.site.register(Friends)
admin.site.register(Team)