from .models import Category, Exam, Lesson, Course, Contact
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Exam)
class ProductTranslationOptions(TranslationOptions):
    fields = ('exam_title',)

@register(Lesson)
class ProductTranslationOptions(TranslationOptions):
    fields = ('lesson_name',)

@register(Course)
class ProductTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')

@register(Contact)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)


