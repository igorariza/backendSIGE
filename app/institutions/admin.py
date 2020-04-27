from django.contrib import admin
# Register your models here.
from institutions.models import EducationalInstitution, Headquarters

# Register yours models here.
@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ( 'nameIE', 'nitIE', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('is_active',)

@admin.register(Headquarters)
class HeadquartersAdmin(admin.ModelAdmin):
      list_display = ('nameHeadquarters', 'daneHeadquarters', 'ieHeadquarters', 'is_active')
      list_editable = ('is_active',)
      search_fields = ('ieHeadquarters',
                       'is_active')
      

