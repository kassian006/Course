from .models import Category, UserProfile
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)
