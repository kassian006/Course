from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

STATUS_CHOICES = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
)


class UserProfile(AbstractUser):
    address = models.CharField(max_length=54)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField()
    data_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='student')

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Student(UserProfile):
    role = models.CharField(max_length=15, choices=[('student', 'student')], default='student')
    headline = models.CharField(max_length=60)
    Facebook = models.URLField(null=True, blank=True)
    Linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Teacher(UserProfile):
    education = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    work_experience = models.PositiveSmallIntegerField(null=True, blank=True)
    role = models.CharField(max_length=15, choices=[('teacher', 'teacher')], default='teacher')


    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Follow(models.Model):
    subscription = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subscription')
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        unique_together = ('subscription',)

    def __str__(self):
        return f'{self.subscription}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Course(models.Model):
    course_name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    CHOICES_LEVEL = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    )
    level = MultiSelectField(max_length=46, choices=CHOICES_LEVEL)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    language = models.CharField(max_length=24)

    def __str__(self):
        return f'{self.course_name}'

    def get_avg_rating(self):
        ratings = self.course_review.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def get_count_rating(self):
        ratings = self.course_review.all()
        if ratings.exists():
            return ratings.count()
        return 0


class Lesson(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_avg_rating(self):
        ratings = self.lesson_review.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def get_count_rating(self):
        ratings = self.lesson_review.all()
        if ratings.exists():
            return ratings.count()
        return 0


class LessonVideo(models.Model):
    video = models.URLField(null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='video')

    def __str__(self):
        return f"{self.lesson}-videos"


class LessonFile(models.Model):
    file = models.FileField(upload_to='lesson_files/', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='file')

    def __str__(self):
        return f"{self.lesson}-files"


class Assignment(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='assignments')

    def __str__(self):
        return f'{self.title}, {self.due_date}'


class Option(models.Model):
    options = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.options}'


class Questions(models.Model):
    questions = models.CharField(max_length=122)
    options = models.ManyToManyField(Option)

    def __str__(self):
        return f'{self.questions}'


class Exam(models.Model):
    title = models.CharField(max_length=32)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Questions)
    passing_score = models.PositiveSmallIntegerField()
    duration = models.DurationField(default=timedelta(hours=1))

    def __str__(self):
        return f'{self.title}, {self.passing_score}, {self.duration}'


class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_certificate')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return f'{self.issued_at}'


class Choice(models.Model):
    question = models.ForeignKey(Questions, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=243)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.question.text}: {self.choice.text} ({'Correct' if self.is_correct else 'Wrong'})"


class Favorite(models.Model):
    owner = models.OneToOneField(Student, on_delete=models.CASCADE)


class FavoriteItem(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='favorite')


class Cart(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)


class CourseReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_review')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_review')
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)
    ])
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f'{self.student} - {self.course}'


class TeacherRating(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teachers')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.teacher} - {self.rating}'

    def get_avg_rating(self):
        ratings = self.course_reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def get_total_people(self):
        ratings = self.course_reviews.all()
        if ratings.exists():
            if ratings.count() > 3:
                return f'3+'
            return ratings.count()
        return 0


    def get_check_good(self):
        ratings = self.course_reviews.all()
        if ratings.exists():
            num = 0
            for i in ratings:
                if i.rating > 3:
                    num += 1
            return f'{round((num * 100) / ratings.count())}%'
        return f'0%'
