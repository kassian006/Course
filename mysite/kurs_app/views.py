from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilter, CategoryFilter, LessonFilter, TeacherFilter, ExamFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import CheckTeacher, CheckLessonTeacher, CheckCourseTeacher
from .paginations import CourseNumberPagination, StudentNumberPagination, TeacherNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    pagination_class = StudentNumberPagination


class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer


class TeacherListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TeacherFilter
    search_fields = ['position', 'role']
    ordering_fields = ['work_experience']
    pagination_class = TeacherNumberPagination


class TeacherDetailAPIView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer


class FollowListAPIView(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowListSerializer


class FollowDetailAPIView(generics.RetrieveAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowDetailSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = Category
    search_fields = ['category_name']


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['course_name']
    ordering_fields = ['update_at']
    pagination_class = CourseNumberPagination


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

    # def get(self, request):
    #     courses = Course.objects.all()
    #     serializer = CourseDetailSerializer(courses, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     courses = Course.objects.all()
    #     for course in courses:
    #         course.price = request.data.get("price", course.price)
    #         course.save()
    #
    #     serializer = CourseDetailSerializer(courses, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    def get_queryset(self):
        return Course.objects.filter(id=self.request.user.id)


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [CheckTeacher]


class CourseDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [CheckTeacher]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LessonFilter
    search_fields = ['lesson_name']
    ordering_fields = ['created_date']
    pagination_class = CourseNumberPagination


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class LessonFileListAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonFileListSerializers


class LessonFileDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonFileDetailSerializers


class LessonLanguagesListAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonLanguagesListSerializers


class LessonLanguagesDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonLanguagesDetailSerializers


class CourseListTeacherAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListTeacherSerializer
    permission_classes = [CheckTeacher]


class CourseDetailTeacherAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailTeacherSerializer
    permission_classes = [CheckTeacher, CheckCourseTeacher]

    def get_queryset(self):
        return Course.objects.filter(id=self.request.user.id)


class LessonListTeacherAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListTeacherSerializer
    permission_classes = [CheckTeacher]


class LessonDetailTeacherAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailTeacherSerializer
    permission_classes = [CheckTeacher, CheckLessonTeacher]

    def get_queryset(self):
        return Lesson.objects.filter(id=self.request.user.id)


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    pagination_class = CourseNumberPagination


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class QuestionsListAPIView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsListSerializer
    pagination_class = CourseNumberPagination


class QuestionsDetailAPIView(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsDetailSerializer


class QuestionsCreateAPIView(generics.CreateAPIView):
    serializer_class = QuestionsListSerializer


class QuestionsDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsDetailSerializer


class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ExamFilter
    search_fields = ['exam_title']
    ordering_fields = ['passing_score']


class ExamDetailAPIView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer

    def get_queryset(self):
        return Course.objects.filter(id=self.request.user.id)


class ExamCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer


class ExamDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class QuestionsListTeacherAPIView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = CourseListTeacherSerializer
    permission_classes = [CheckTeacher]


class QuestionsDetailTeacherAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsDetailTeacherSerializer
    permission_classes = [CheckTeacher, CheckCourseTeacher]

    def get_queryset(self):
        return Questions.objects.filter(id=self.request.user.id)


class ExamListTeacherAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListTeacherSerializer
    permission_classes = [CheckTeacher]


class ExamDetailTeacherAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailTeacherSerializer
    permission_classes = [CheckTeacher, CheckCourseTeacher]

    def get_queryset(self):
        return Exam.objects.filter(id=self.request.user.id)


# class ChoiceViewSet(viewsets.ModelViewSet):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer


class UserAnswerListAPIView(generics.ListAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerListSerializer


class UserAnswerDetailAPIView(generics.RetrieveAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerListSerializer

    def get_queryset(self):
        return Course.objects.filter(id=self.request.user.id)


class UserAnswerListTeacherAPIView(generics.ListAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerListTeacherSerializer
    permission_classes = [CheckTeacher]


class UserAnswerDetailTeacherAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerDetailTeacherSerializer
    permission_classes = [CheckTeacher, CheckCourseTeacher]

    def get_queryset(self):
        return UserAnswer.objects.filter(id=self.request.user.id)


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class FavoriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CourseReviewViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer


class TeacherRatingViewSet(viewsets.ModelViewSet):
    queryset = TeacherRating.objects.all()
    serializer_class = TeacherRatingSerializer

