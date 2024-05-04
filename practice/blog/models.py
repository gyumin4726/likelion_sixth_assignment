from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField('Tag', blank=True)
    likes = models.ManyToManyField(User, related_name='liked_blogs', blank=True)  # 좋아요를 나타내는 필드

    class Meta:
        db_table = 'blog'
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]
    
# 댓글
class Comment(models.Model):
    cotent = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'content'

    def __str__(self):
        return self.content + ' | ' + str(self.author)
    
# 태그

class Tag(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'tag'
    
    def __str__(self):
        return self.name
    
# 좋아요

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blog')  # 사용자와 블로그 게시물의 중복 좋아요 방지

    def __str__(self):
        return f'{self.user.username} likes {self.blog.title}'