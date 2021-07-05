from django.db import models


class Course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='Course', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']
