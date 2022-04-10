from django.contrib import admin
from django.db.models.query_utils import subclasses
from .models import *
# Register your models here.
class UniversityAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

class DegreeAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

class EducationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

class MajorProjectAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

class CurrencyAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    
class CurriculumAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

class TeacherInfoAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('user',)}

class TeacherSubjectAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('user',)}

admin.site.register(TeacherInfo,TeacherInfoAdmin)
admin.site.register(TeachAvailability)
admin.site.register(University,UniversityAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Degree,DegreeAdmin)
admin.site.register(MajorProject,MajorProjectAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Curriculum,CurriculumAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(TeacherSubject, TeacherSubjectAdmin)
admin.site.register(SelectField)