from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # categories = models.CharField(max_length=200,choices=categoriy)
    image   = models.ImageField(upload_to='image/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on', '-updated_on', '-timestamp']

#auto create slug field using title.
#https://medium.com/@dev_mike_del/django-slugs-a-models-journey-85ce5625a7bf
#the above link to generate uniqe slug 
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    def get_edit_url(self):
        return f"{self.get_absolute_url()}/update"

    def __str__(self):
        return self.title



