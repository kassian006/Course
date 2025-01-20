from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', )
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
        fields = ['bio', 'student_image']


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['bio', 'student_image']


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['bio', 'teacher_image']


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
        fields = ['category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CourseListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['course_name', 'category', 'level', 'created_by','avg_rating','count_rating']

        def get_avg_rating(self, obj):
            return obj.get_avg_rating()

        def get_count_rating(self, obj):
            return obj.get_count_rating()


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'level', 'price', 'created_by', 'created_at', 'update_at']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['file',]


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
        model = Lesson
        fields = ['title', 'content', 'course', 'teacher']


class LessonVideoDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = LessonVideo
        fields = ['video', 'lesson']


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['options']


class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'questions']


class QuestionsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['questions', 'options']


class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'course', ]


class ExamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'course', 'questions', 'passing_score', 'duration']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['question', 'text', 'is_correct']


class UserAnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['question', 'choice', 'student', 'is_correct', 'students']


class UserAnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['question', 'choice', 'student', 'is_correct', 'students']


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
    class Meta:
        model = CourseReview
        fields = ['student', 'course', 'text', 'stars', 'created_date']


class TeacherRatingSerializer(serializers.ModelSerializer):
    avg_ratings = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()
    check_good = serializers.SerializerMethodField()

    class Meta:
        model = TeacherRating
        fields = ['student', 'teacher', 'rating', 'created_date', 'avg_ratings', 'total_people', 'check_good']

        def get_avg_ratings(self, obj):
            return obj.get_avg_rating()

        def get_total_people(self, obj):
            return obj.get_total_people()

        def get_check_good(self, obj):
            return obj.get_check_good()

