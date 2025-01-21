from rest_framework import permissions


class CheckTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'teacher':
            return True
        return False

class CheckUserReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'student':
            return True
        return False


class CheckCourseTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.teacher == request.user


class CheckLessonTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.course.teacher == request.user

