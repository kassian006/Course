from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class OptionInline(admin.TabularInline):
    model = Option
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


admin.site.register(Questions, QuestionAdmin)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]


class LessonVideoInline(admin.TabularInline):
    model = LessonVideo
    extra = 1


class LessonFileInline(admin.TabularInline):
    model = LessonFile
    extra = 1

class LessonLanguagesInline(admin.TabularInline):
    model = LessonLanguages
    extra = 1


@admin.register(Lesson)
class ProductAdmin(TranslationAdmin):
    inlines = [LessonVideoInline, LessonFileInline, LessonLanguagesInline]


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(Category, Exam, Course, Contact)
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
#admin.site.register(Option)
admin.site.register(Assignment)
admin.site.register(Certificate)
admin.site.register(UserAnswer)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)
admin.site.register(CourseReview)
admin.site.register(TeacherRating)

