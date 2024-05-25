from django.contrib import admin
import apps.one_image.models as model

@admin.register(model.Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('name', 'build_date', 'work_goal')
    search_fields = ('name', 'work_goal')
    prepopulated_fields = {
        'slug': ('name', 'build_date'),
    }

@admin.register(model.Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('field_name',)
    search_field = ('field_name',)


@admin.register(model.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'family', 'age', 'email', 'education_degree', 'education_field',)
    search_field = ('name', 'family', 'education_field', 'education_degree',)
    prepopulated_fields = {
        'slug': ('name', 'family',)
    }
    
    
@admin.register(model.Honor)
class HonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'honor_field', 'owner',)
    prepopulated_fields = {
        'slug': ('name',)
    }
    search_fields = ('name', 'owner', 'honor_field',)
    