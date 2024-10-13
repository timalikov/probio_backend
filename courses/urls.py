from django.urls import path
from probio_backend.courses.views import CoursesView, LessonsView, ModulesView


urlpatterns = [
    path('api/courses/', CoursesView.as_view(), name='courses_api'),
    path('api/modules/', ModulesView.as_view(), name='modules_api'),
    path('api/lessons/', LessonsView.as_view(), name='lessons_api'),
]