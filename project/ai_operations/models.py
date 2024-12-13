from django.db import models





# class CustomUser(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=200, unique=True)
#     password = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name



# class Project(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

#     def __str__(self):
#         return self.name



# class Workflow(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='workflows')
#     def __str__(self):
#         return self.name



# class WorkflowBlock(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='workflow_blocks')
#     def __str__(self):
#         return f"WorkflowBlock {self.id}"



# class Block(models.Model):
#     name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50, null=True, blank=True)
#     task = models.CharField(max_length=50, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     position = models.CharField(max_length=100, null=True, blank=True)   
#     execution_order = models.IntegerField(primary_key=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name



# class WFBlockBlock(models.Model):
#     workflowblock = models.ForeignKey(WorkflowBlock, on_delete=models.CASCADE, related_name='blocks')




    

# class TrainTestSplit(models.Model):
#     data = models.CharField(max_length=250)
#     test_size = models.FloatField(default=0.2)
#     random_state = models.IntegerField(blank=True, null=True)


