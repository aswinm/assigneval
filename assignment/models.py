from django.db import models
from users.models import MyUser

class Assignment(models.Model):
    
    def __unicode__(self):
        return self.name

    aid = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(MyUser)
    sample_copy = models.FileField(upload_to="sample_copies")
    deadline = models.DateTimeField()

class Submission(models.Model):

    def __unicode__(self):
        return self.assignment.name +" , "+ self.user.first_name

    sid = models.AutoField(primary_key = True)
    assignment = models.ForeignKey(Assignment)
    user = models.ForeignKey(MyUser)
    answer = models.FileField(upload_to="answers")
    submitted_at = models.DateTimeField()
    is_plagiarism = models.BooleanField(default=False)
    score = models.FloatField(default=0)
    grade = models.CharField(max_length=2)


# Create your models here.
