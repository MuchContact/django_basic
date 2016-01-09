from django.db import models

class App(models.Model):
    """
    Application used to service requests on behalf of end-users
    """
    id = models.SlugField(primary_key=True, max_length=64, unique=True, default='',
                          validators=[])
    title = models.CharField(max_length=100, blank=True, default='')
