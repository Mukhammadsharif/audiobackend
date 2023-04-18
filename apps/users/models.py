import uuid

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from core.utils.files import file_path
from main.models import BaseModel
from users.querysets.user import UsersManager
from users.utils.fields import expires_default, expires_hour


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True, verbose_name=_('email'))  # override default email field
    confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,
                                         verbose_name=_('confirmation code'))
    image = models.ImageField(upload_to=file_path(''), null=True, blank=True, verbose_name=_('Avatar'))
    verified_at = models.DateTimeField(null=True, blank=True, verbose_name=_('verified_at'))
    # TODO: Remove expires_subscription_at
    expires_subscription_at = models.DateField(null=True, blank=True, verbose_name=_('expires_subscription_at'))
    objects = UsersManager()

    def can_access_course(self, course_obj):
        for subscription in self.get_active_subscriptions():
            # If plan is limited by number of courses, check if the particular course is purchased
            if subscription.plan.courses_included:
                if course_obj in subscription.courses.all():
                    return True
            # Else any course works
            else:
                return True
        # By default, no courses are allowed
        return False

    def get_active_subscriptions(self):
        return self.subscription_set.filter(status__in=['active', 'in_trial', 'non_renewing'])

    class Meta(AbstractUser.Meta):
        db_table = 'user_users'
        app_label = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Token(BaseModel):
    key = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name=_('token'))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))
    user = models.ForeignKey(User, models.CASCADE, related_name='tokens', verbose_name=_('user'))
    expires_at = models.DateTimeField(default=expires_default, verbose_name=_('expires_at'))  # token expires in 30 days

    def __str__(self):
        return self.key

    class Meta:
        db_table = 'user_tokens'
        verbose_name = _('token')
        verbose_name_plural = _('tokens')


class ResetPassword(BaseModel):
    key = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name=_('token'))
    user = models.ForeignKey(User, models.CASCADE)
    expires_at = models.DateTimeField(default=expires_hour)

    def __str__(self):
        return self.key

    class Meta:
        db_table = 'user_reset_password'
