from django.contrib import admin
from .models import Sport, Ctavka, Total

# Register your models here.
class CtavkaAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'coefficient', 'published', 'sport', 'total')
    #search_fields = ('title', 'content')



admin.site.register(Sport)
admin.site.register(Ctavka,CtavkaAdmin)
admin.site.register(Total)
