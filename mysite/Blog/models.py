from django.db import models
from django.contrib.auth.models import User

#models
#to keep draft and published posts separated when rendered out with templates.
STATUS = (
    (0, "Draft"), 
    (1, "Publish")
)

class Post(models.Model):
    blog_title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length = 200, unique = True)
    blog_author =models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_post')
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    blog_content = models.TextField()
    status = models.IntegerField(choices = STATUS, default = 0)

    #meta
    class Meta:
        ordering = [ 'blog_author', '-created_on' ]

    #methods
    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
