from django.contrib.auth.models import User
from django.db import models
import uuid


class Base(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Lab(Base):
    pass

    def __str__(self):
        return self.title


class Challenge(Base):
    pass

    def __str__(self):
        return self.title


class LabBookmark(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user.username}, Lab: {self.lab.title}"


class ChallengeBookmark(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user.username}, Challenge: {self.challenge.title}"
