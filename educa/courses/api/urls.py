from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("courses", views.CourseViewSet)
router.register("subjects", views.SubjectViewSet)

app_name = "courses"
urlpatterns = [
    # path("subjects/", views.SubjectListView.as_view(), name="subject_list"),
    # path("subjects/<pk>/", views.SubjectDetailView.as_view(), name="subject_detail"),
    path("", include(router.urls)),
]
