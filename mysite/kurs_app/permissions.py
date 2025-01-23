from rest_framework import permissions


class CheckCreateCourse(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status in ['teacher', 'admin']:
            return True
        return False


class GiveCertificate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status in ['student', 'admin']:
            return True
        return False


class CreateCertificate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status in ['teacher', 'admin']:
            return True
        return False


class CheckUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'admin':
            return True
        return False