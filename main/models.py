from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    section=models.ForeignKey(Section,blank=True,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='images')
    date = models.DateField()

    def __str__(self):
        return self.name

    def summary(self):
        return self.description[:100]

    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Video(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    youtubelink=models.CharField(max_length=1000,null=True,blank=True)
    file=models.FileField(upload_to='video',null=True,blank=True)

    def __str__(self):
        return self.name