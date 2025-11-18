from django.db import models


class Todo(models.Model):
    """ Create Todo model with a ForeignKey to the User model """

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    done=models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name_plural = 'Todos'
        verbose_name='Todo'