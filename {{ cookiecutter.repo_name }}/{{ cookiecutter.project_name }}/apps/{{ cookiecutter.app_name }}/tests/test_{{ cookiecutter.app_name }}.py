from django.test import TestCase

from .factories import {{ cookiecutter.app_name.capitalize() }}Factory


class {{ cookiecutter.app_name.capitalize() }}TestCase(TestCase):

    def test_create_{{ cookiecutter.app_name.capitalize() }}(self):
        {{ cookiecutter.app_name }} = {{ cookiecutter.app_name.capitalize() }}Factory()
        {{ cookiecutter.app_name }}.save()

        new_{{ cookiecutter.app_name }} = Brands.objects.first()

        self.assertEqual(new_{{ cookiecutter.app_name }}.name, {{ cookiecutter.app_name.capitalize() }}Factory.name)
