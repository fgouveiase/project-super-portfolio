from rest_framework import serializers
from projects.models import (
    Profile, Project, Certificate, CertifyingInstitution)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class CertificateNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['name']


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateNestedSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = "__all__"

    def create(self, validated_data):
        certificates = validated_data.pop("certificates")

        institution = CertifyingInstitution.objects.create(
            **validated_data,
            )

        for certificate in certificates:
            Certificate.objects.create(
                certifying_institution=institution,
                **certificate,
            )

        return institution
