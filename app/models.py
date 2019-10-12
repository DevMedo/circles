from django.db import models

# Create your models here.
class Circle(models.Model):
    name = models.CharField(max_length=60)
    students = models.ManyToManyField('Student',blank=True, related_name='circle_students')
    posts = models.ManyToManyField('Post',blank=True, related_name='circle_posts')
    rank = models.IntegerField()
    def __str__(self):
        return self.name+str(self.id)
class Student(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    circles = models.ManyToManyField('Circle',blank=True, related_name='student_circles')
    posts = models.ManyToManyField('Post',blank=True, related_name='student_posts')
    points = models.IntegerField()
    def __str__(self):
        return self.name+str(self.id)
    
class Post(models.Model):
    circle_entity = models.ForeignKey(Circle, on_delete=models.CASCADE)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.TextField()
    points = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=60)
    replays = models.ManyToManyField('Replay',blank=True, related_name='post_replays')
    def __str__(self):
        return 'post'+str(self.id)

class Replay(models.Model):
    post_entity = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'replay'+str(self.id)
