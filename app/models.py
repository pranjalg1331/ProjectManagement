from django.db import models
from register.models import Profile


class Project(models.Model):
    name=models.CharField(max_length=50,default="unknown-project")
    owner=models.ManyToManyField(Profile,related_name='owned_projects')
    contributor=models.ManyToManyField(Profile,related_name='contributed_projects')
    created_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.name
    
   

STATUS_CHOICES = (
    # "Completed","Pending"
("Completed", "Completed"),
("Pending","Pending")

)

# Create your models here.
class Tasks(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    des=models.CharField(max_length=50,default="")
    assigned=models.ManyToManyField(Profile)
    created_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    due_date=models.DateField(auto_now=False, auto_now_add=False)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default="Pending")
    
    def __str__(self):
        return self.des
    
    def is_pending(self):
        if self.status=="Pending":
            return True
        else:
            return False