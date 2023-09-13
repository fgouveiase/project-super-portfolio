from django.shortcuts import render
from rest_framework import viewsets
from projects.models import (Profile, Project,
                             Certificate, CertifyingInstitution)
from .serializers import (
    ProfileSerializer, ProjectSerializer,
    CertificateSerializer, CertifyingInstitutionSerializer)
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if self.request.method == "GET":
            profile = Profile.objects.get()

            return render(request, "profile_detail.html", {
                "profile": profile,
                "projects": profile.projects.all(),
                "certificates": profile.certificates.all(),
            })

        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
