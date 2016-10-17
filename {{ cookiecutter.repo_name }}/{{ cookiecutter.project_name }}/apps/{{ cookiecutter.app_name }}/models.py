from django.db import models

class {{ cookiecutter.app_name.capitalize() }}(models.Model):
	id = models.UUIDField(
		primary_key=True, 
		default=uuid.uuid4, 
		editable=False
	)
	name = models.CharField(max_length=100)
