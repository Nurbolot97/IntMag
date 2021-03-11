from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from PIL import Image

from .models import *


class NotebookAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe('<span style="color:red;">Загружайте изображение с минимальным разрешением {}x{}</span>'.format(*Product.MIN_VALIDATIONS))

    def clean_data(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_VALIDATIONS
        max_height, max_width = Product.MAX_VALIDATIONS
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Превышен объем возможной загрузки картины')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Загруженная картинка не соответствует требованиям')
        if img.height < max_height or img.width < max_width:
            raise ValidationError('Загруженная картинка не соответствует требованиям')
        return image


class NotebookAdmin(admin.ModelAdmin):
    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):
    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(CartProduct)
admin.site.register(Cart)




