from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


@admin.register(Category)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Follow)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Option)
admin.site.register(Questions)
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CourseReview)
admin.site.register(TeacherRating)

