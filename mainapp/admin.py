from django import forms
from django.contrib import admin

from .models import *


class NotebookCategoryChoiceField(forms.ModelChoiceField):
    pass


class NotebookAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return NotebookCategoryChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(CartProduct)
admin.site.register(Cart)




