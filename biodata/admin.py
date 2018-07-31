from django.contrib import admin

from . models import Bio, Education, Work, Project
# Register your models here.


class BioAdmin(admin.ModelAdmin):
    list_display = ('title', 'story_text', 'pub_date')
    date_hierarchy = 'pub_date'
    ordering = ['pub_date']

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'education_text', 'image', 'education_years', 'pub_date')
    date_hierarchy = 'pub_date'
    ordering = ['pub_date']


class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'work_text', 'image', 'work_year', 'pub_date')
    date_hierarchy = 'pub_date'
    ordering = ['pub_date']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_text', 'image', 'pub_date')
    date_hierarchy = 'pub_date'
    ordering = ['pub_date']


admin.site.register(Bio, BioAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Project, ProjectAdmin)
