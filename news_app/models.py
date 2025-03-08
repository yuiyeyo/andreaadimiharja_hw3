from django.db import models

class Article(models.Model):  
    article_id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.headline


class VisualContent(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file_url = models.URLField(blank=True, null=True) 
    file_type = models.CharField(max_length=10, choices=[("image", "Image"), ("video", "Video")])
    css_class = models.CharField(max_length=100, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return self.name
