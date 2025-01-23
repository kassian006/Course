from django_filters import FilterSet
from .models import Course, Lesson, Teacher, Category, Exam


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt'],
        }


class LessonFilter(FilterSet):
    class Meta:
        model = Lesson
        fields = {
            'created_date': ['gt', 'lt'],
        }


class TeacherFilter(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'position': ['exact'],
            'work_experience': ['gt', 'lt'],
      }


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['exact'],
        }

class ExamFilter(FilterSet):
    class Meta:
        model = Exam
        fields = {
            'exam_title': ['exact'],
        }