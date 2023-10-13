from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Eleve)
admin.site.register(Professeur)
admin.site.register(Cour)
admin.site.register(Devoir)
admin.site.register(Info)
admin.site.register(Matiere)
admin.site.register(Note)
admin.site.register(etablissement)