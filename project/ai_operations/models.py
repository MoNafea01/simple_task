from django.db import models

# Create your models here.
class Workflow(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Node(models.Model):
    workflow = models.ForeignKey(Workflow, related_name='nodes', on_delete=models.CASCADE)
    node_type = models.CharField(max_length=255)  # e.g., 'dataLoader', 'preprocessor', 'modelTrainer', etc.
    config = models.JSONField()  # Store the configuration as a JSON
    order = models.IntegerField()  # Order of execution
