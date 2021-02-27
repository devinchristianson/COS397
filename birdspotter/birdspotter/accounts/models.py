from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group
from django.contrib import messages
from django.utils import timezone
import uuid


class User(AbstractUser):
    """Custom user implementation
    Attributes:
        username (str): user specified username, used as unique identifier
    """
    username = models.CharField(max_length=30, unique=True)
    user_id = models.UUIDField(primary_key=False,
                               default=uuid.uuid4, editable=False, unique=True)

    def to_dict(self):
        return {
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

    def is_admin(self):
        return self.groups.filter(name='Admin').exists()

    def make_active(self):
        self.is_active = True
        self.save()

class GroupRequest(models.Model):
    """
    Role request model that allows admin approve or deny group requests
    """
    groups = ['Admin', 'Privileged', 'Registered']

    GROUP_CHOICES = [(a, a) for a in groups]

    request_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name='requesting_user')
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, default='Registered')
    submitted_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='approving_user')
    reviewed_date = models.DateTimeField(blank=True, null=True)


    def approve_request(self, request):
        self.approved = True
        self.reviewed_by = request.user
        self.reviewed_date = timezone.now()
        try:
            permission_group = Group.objects.get(name=self.group)
            self.user.groups.add(permission_group)
            if self.group == 'Registered':
                breakpoint()
                user = User.objects.get(username=request.user.username)
                user.make_active()
            messages.success(request, f'User {self.user} successfully added to {self.group}')
        except Exception as c:
            messages.error(request, f'Permission group {self.group} does not exist')
        self.save()


    def deny_request(self, request):
        self.approved = False
        self.reviewed_by = request.user
        self.reviewed_date = timezone.now()
        self.save()