from django.db import models
import uuid


class STUDENT_COURSE_STATUS(models.TextChoices):
    PENDING = 'pending'
    ACCEPTED = 'accepted'


class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=20,
        choices=STUDENT_COURSE_STATUS.choices,
        default=STUDENT_COURSE_STATUS.PENDING
    )
    course_id = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE
    )
    student_id = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE
    )
