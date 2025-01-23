from .views import *
from django.urls import path, include
from  rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'assignments', AssignmentViewSet, basename='assignments'),
router.register(r'contact', ContactViewSet, basename='contact'),
#router.register(r'questions', QuestionsViewSet, basename='questions'),
router.register(r'options', OptionViewSet, basename='options'),
#router.register(r'certificates', CertificateViewSet, basename='certificates'),
router.register(r'favorite', FavoriteViewSet, basename='favorite'),
router.register(r'favorite_items', FavoriteItemViewSet, basename='favorite_items'),
router.register(r'carts', CartViewSet, basename='carts'),
router.register(r'cart_items', CartItemViewSet, basename='cart_items'),
router.register(r'course_review', CourseReviewViewSet, basename='course_review'),
router.register(r'teacher_rating', TeacherRatingViewSet, basename='teacher_rating'),


urlpatterns = [
    path('', include(router.urls)),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),

    path('', include(router.urls)),
    path('students/', StudentListAPIView.as_view(), name='students_list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='students_detail'),

    path('teacher/', TeacherListAPIView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher_detail'),

    path('follow/', FollowListAPIView.as_view(), name='follow_list'),
    path('follow/<int:pk>/', FollowDetailAPIView.as_view(), name='follow_detail'),

    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),

    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('course/create/<int:pk>/', CourseDetailUpdateDeleteAPIView.as_view(), name='course_create_edit'),
    path('course_list/', CourseListTeacherAPIView.as_view(), name='course_list_teacher'),
    path('course_list/<int:pk>/', CourseDetailTeacherAPIView.as_view(), name='course_list_edit'),

    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('lesson_list/', LessonListTeacherAPIView.as_view(), name='lesson_list_teacher'),
    path('lesson_list/<int:pk>/', LessonDetailTeacherAPIView.as_view(), name='lesson_list_edit'),

    path('exam/', ExamListAPIView.as_view(), name='exam_list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam_detail'),
    path('exam/create/', ExamCreateAPIView.as_view(), name='exam_create'),
    path('exam/create/<int:pk>/', ExamDetailUpdateDeleteAPIView.as_view(), name='exam_create_edit'),
    path('exam_list/', ExamListTeacherAPIView.as_view(), name='exam_list_owner'),
    path('exam_list/<int:pk>/', ExamDetailTeacherAPIView.as_view(), name='exam_list_edit'),

    path('certificates/', CertificateListAPIView.as_view(), name='certificates_list'),
    path('certificates/<int:pk>/', CertificateDetailAPIView.as_view(), name='certificates_detail'),
    path('certificates/create/', CertificateCreateApiView.as_view(), name='certificates_create'),

    path('user_answer/', UserAnswerListAPIView.as_view(), name='user_answer_list'),
    path('user_answer/<int:pk>/', UserAnswerDetailAPIView.as_view(), name='user_answer_detail'),
    path('user_answer_list/', UserAnswerListTeacherAPIView.as_view(), name='user_answer_list_teacher'),
    path('user_answer_list/<int:pk>/', UserAnswerDetailTeacherAPIView.as_view(), name='user_answer_list_edit'),

    path('questions/', QuestionsListAPIView.as_view(), name='questions_list'),
    path('questions/<int:pk>/', QuestionsDetailAPIView.as_view(), name='questions_detail'),
    path('questions/create/', QuestionsCreateAPIView.as_view(), name='questions_create'),
    path('questions/create/<int:pk>/', QuestionsDetailUpdateDeleteAPIView.as_view(), name='questions_create_edit'),
    path('questions_list/', QuestionsListTeacherAPIView.as_view(), name='questions_list_teacher'),
    path('questions_list/<int:pk>/', QuestionsDetailTeacherAPIView.as_view(), name='questions_list_edit'),

]
