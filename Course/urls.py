from django.urls import path
from Course import views


urlpatterns = [
    path('courses/',views.CourseList.as_view()),
    path('courses/<int:pk>/',views.CourseDetail.as_view()),
    path('users/',views.UserList.as_view()),
    path('users/<int:pk>/',views.UserDetail.as_view()),
]
