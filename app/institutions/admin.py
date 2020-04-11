from django.contrib import admin
# Register your models here.
from institutions.models import EducationalInstitution, Headquarters

# Register yours models here.
@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ('codeIE', 'nameIE', 'nitIE', 'is_active')
    list_editable = ('nameIE', 'nitIE', 'is_active')
    search_fields = ('is_active',)

@admin.register(Headquarters)
class HeadquartersAdmin(admin.ModelAdmin):
      list_display = ('codeHeadquarters', 'nameHeadquarters', 'daneHeadquarters', 'codeIE', 'is_active')
      list_editable = ('nameHeadquarters', 'daneHeadquarters', 'is_active')
      search_fields = ('codeIE',
                       'is_active')
      

