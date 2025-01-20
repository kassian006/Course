from django_filters import FilterSet
from .models import Course, Lesson, Teacher, Category


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'category': ['exact']
        }


class LessonFilter(FilterSet):
    class Meta:
        model = Lesson
        fields = {
            'title': ['exact'],
            'created_date': ['gt', 'lt']
        }


class TeacherFilter(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'position': ['exact'],
            'work_experience': ['gt', 'lt'],
            'role': ['exact']
      }


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['exact']
        }
