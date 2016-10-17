import factory

from apps.{{ cookiecutter.app_name }}.models import {{ cookiecutter.app_name.capitalize() }}


class {{ cookiecutter.app_name.capitalize() }}Factory(factory.Factory):

	class Meta:
		model = {{ cookiecutter.app_name.capitalize() }}

	name = 'Change This'