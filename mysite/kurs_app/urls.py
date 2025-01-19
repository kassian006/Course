from .views import *
from django.urls import path, include
from  rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'students', StudentListViewSet, basename='students'),
router.register(r'teachers', TeacherListViewSet, basename='teachers'),
router.register(r'follows', FollowListViewSet, basename='follows'),
router.register(r'courses', CourseListViewSet, basename='courses'),
router.register(r'lessons', LessonListViewSet, basename='lessons'),
router.register(r'assignments', AssignmentViewSet, basename='assignments'),
router.register(r'options', OptionViewSet, basename='options'),
router.register(r'questions', QuestionsViewSet, basename='questions'),
router.register(r'exams', ExamListViewSet, basename='exams'),
router.register(r'certificates', CertificateViewSet, basename='certificates'),
router.register(r'carts', CartViewSet, basename='carts'),
router.register(r'cart_items', CartItemViewSet, basename='cart_items'),
router.register(r'course_review', CourseReviewViewSet, basename='course_review'),
router.register(r'teacher_rating', TeacherRatingViewSet, basename='teacher_rating'),


urlpatterns = [
    path('', include(router.urls)),
]
