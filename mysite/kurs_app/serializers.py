from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','bio', 'student_image']


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['bio', 'student_image']


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','bio', 'teacher_image']


class TeacherDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['subscription', 'created_date']


class FollowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['subscription', 'created_date']


class FollowDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['subscription', 'created_date']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CourseListSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer()
    avg_rating = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id','course_name', 'category', 'level', 'created_by','avg_rating','count_rating']

    def get_avg_rating(self, obj):
            return obj.get_avg_rating()

    def get_count_rating(self, obj):
            return obj.get_count_rating()


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_course = CourseListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'category_course']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListTeacherSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer()
    class Meta:
        model = Course
        fields = ['id','course_name', 'price', 'created_by', 'category']


class CourseDetailTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['title', 'contact_number', 'social_network']


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id','file',]


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['file', ]


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'students']


class LessonVideoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = LessonVideo
        fields = ['id','title', 'content', 'course', 'teacher']


class LessonVideoDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = LessonVideo
        fields = ['video', 'lesson']


class LessonFileListSerializers(serializers.ModelSerializer):
    class Meta:
        model = LessonFile
        fields = '__all__'


class LessonFileDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = LessonFile
        fields = '__all__'


class LessonLanguagesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = LessonLanguages
        fields = '__all__'


class LessonLanguagesDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = LessonLanguages
        fields = '__all__'



# class OptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Option
#         fields = ['options']


class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'questions']


class QuestionsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['questions', 'options']


class QuestionsListTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class QuestionsDetailTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class LessonListTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonDetailTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id','title', 'course', ]


class ExamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'course', 'questions', 'passing_score', 'duration']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['course', 'issued_at', 'certificate', 'student']


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['question', 'text', 'is_correct']


class UserAnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['id','question', 'choice', 'student', 'is_correct', 'students']


class UserAnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['question', 'choice', 'student', 'is_correct', 'students']


class ExamListTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ExamDetailTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class UserAnswerListTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'


class UserAnswerDetailTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['owner']


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ['course', 'favorite']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user']


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['cart', 'course', 'assignment',  'quantity']


class CourseReviewSerializer(serializers.ModelSerializer):
    student = UserProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = CourseReview
        fields = ['student', 'course', 'text', 'rating', 'created_date']


class TeacherRatingSerializer(serializers.ModelSerializer):
    avg_ratings = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()
    check_good = serializers.SerializerMethodField()

    class Meta:
        model = TeacherRating
        fields = ['student', 'teacher', 'rating', 'created_date', 'avg_ratings', 'total_people', 'check_good']

    def get_avg_rating(self, obj):
            return obj.get_avg_rating()

    def get_count_rating(self, obj):
            return obj.get_total_people()


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer()
    contact_course = ContactSerializer(read_only=True, many=True)
    teacher = TeacherListSerializer(read_only=True)
    lesson_course = LessonListSerializer(read_only=True, many=True)
    teachers = TeacherRatingSerializer(read_only=True, many=True)
    course_review = CourseReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'level', 'price', 'created_by', 'created_at', 'update_at',
                  'contact_course', 'teacher', 'lesson_course', 'teachers', 'course_review']
