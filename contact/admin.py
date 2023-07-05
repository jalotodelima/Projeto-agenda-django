from django.contrib import admin
from contact import models

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone')
    ordering = '-id',  # ordenação descrescente.. por isso o menos na frente
    # list_filter = 'created date' # filtrar ao lado
    search_fields = 'id', 'first_name', 'last_name'
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'phone', 'last_name'
    list_display_links = 'first_name', 'id'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = '-id',  # ordenação descrescente.. por isso o menos na frente
