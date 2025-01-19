from rest_framework import viewsets, generics
from .models import *
from .serializers import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset =UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class StudentListViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer


class StudentDetailViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer


class TeacherListViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer


class TeacherDetailViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer


class FollowListViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowListSerializer


class FollowDetailViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowDetailSerializer


class CategoryListViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CourseListViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer


class CourseDetailViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class LessonListViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer


class LessonDetailViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class ExamListViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer


class ExamDetailViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class UserAnswerListViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerListSerializer


class UserAnswerDetailViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerListSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class FavoriteListViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = FavoriteSerializer


class FavoriteItemDetailViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CourseReviewViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer


class TeacherRatingViewSet(viewsets.ModelViewSet):
    queryset = TeacherRating.objects.all()
    serializer_class = TeacherRatingSerializer

