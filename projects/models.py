from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=50)
    github = models.URLField(max_length=500)
    linkedin = models.URLField(max_length=500)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    github_url = models.URLField(max_length=500)
    keyword = models.CharField(max_length=50)
    key_skill = models.CharField(max_length=50)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100)

    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
        max_length=500)

    timestamp = models.DateField(
        auto_now_add=True,
        max_length=500,
        )

    profiles = models.ManyToManyField(
        Profile,
        related_name="certificates",
        max_length=500,
    )

    def __str__(self):
        return self.name
