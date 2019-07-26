from django.test import TestCase

# Create your tests here.
import unittest
from django.urls import reverse
from django.test import Client
from .models import FTTSProject
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "gibeon@gmail.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_fttsproject(**kwargs):
    defaults = {}
    defaults["project_name"] = "project_name"
    defaults["updated_at"] = "updated_at"
    defaults["is_active"] = "is_active"
    defaults.update(**kwargs)
    if "site_name" not in defaults:
        defaults["site_name"] = create_site()
    return FTTSProject.objects.create(**defaults)

class FTTSProjectViewTest(unittest.TestCase):
    '''
    Tests for FTTSProject
    '''
    def setUp(self):
        self.client = Client()

    def test_list_fttsproject(self):
        url = reverse('erp_fiber_ftts_fttsproject_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_fttsproject(self):
        url = reverse('erp_fiber_ftts_fttsproject_create')
        data = {
            "project_name": "project_name",
            "updated_at": "updated_at",
            "is_active": "is_active",
            "site_name": create_site().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_fttsproject(self):
        fttsproject = create_fttsproject()
        url = reverse('erp_fiber_ftts_fttsproject_detail', args=[fttsproject.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_fttsproject(self):
        fttsproject = create_fttsproject()
        data = {
            "project_name": "project_name",
            "updated_at": "updated_at",
            "is_active": "is_active",
            "site_name": create_site().pk,
        }
        url = reverse('erp_fiber_ftts_fttsproject_update', args=[fttsproject.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)