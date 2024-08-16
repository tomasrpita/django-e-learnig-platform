from rest_framework import generics
from django.db.models import Count
from courses.api.serializers import SubjectSerializer
from courses.models import Subject
from courses.api.pagination import StandardPagination


class SubjectListView(generics.ListAPIView):
    # queryset = Subject.objects.all()
    queryset = Subject.objects.annotate(total_courses=Count("courses"))

    serializer_class = SubjectSerializer
    pagination_class = StandardPagination


class SubjectDetailView(generics.RetrieveAPIView):
    # queryset = Subject.objects.all()
    queryset = Subject.objects.annotate(total_courses=Count("courses"))

    serializer_class = SubjectSerializer
