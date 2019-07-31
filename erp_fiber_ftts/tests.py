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
    defaults["email"] = "username@tempurl.com"
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
    defaults["end_date"] = "end_date"
    defaults["updated_at"] = "updated_at"
    defaults["is_active"] = "is_active"
    defaults.update(**kwargs)
    if "site_name" not in defaults:
        defaults["site_name"] = create_site()
    if "created_by" not in defaults:
        defaults["created_by"] = create_customuser()
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
            "end_date": "end_date",
            "updated_at": "updated_at",
            "is_active": "is_active",
            "site_name": create_site().pk,
            "created_by": create_customuser().pk,
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
            "end_date": "end_date",
            "updated_at": "updated_at",
            "is_active": "is_active",
            "site_name": create_site().pk,
            "created_by": create_customuser().pk,
        }
        url = reverse('erp_fiber_ftts_fttsproject_update', args=[fttsproject.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


# Daily Productions tests




import unittest
from django.urls import reverse
from django.test import Client
from .models import DailyCivilWorkProduction
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
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


def create_dailycivilworkproduction(**kwargs):
    defaults = {}
    defaults["work_day"] = "work_day"
    defaults["trenched_distance"] = "trenched_distance"
    defaults["backfilled_distance"] = "backfilled_distance"
    defaults["duct_installed_length"] = "duct_installed_length"
    defaults["cable_installed_length"] = "cable_installed_length"
    defaults["site_dailyproduction_comment"] = "site_dailyproduction_comment"
    defaults["is_approved"] = "is_approved"
    defaults.update(**kwargs)
    if "site_name" not in defaults:
        defaults["site_name"] = create_site()
    if "project_name" not in defaults:
        defaults["project_name"] = create_fttsproject()
    if "posted_by" not in defaults:
        defaults["posted_by"] = create_customuser()
    return DailyCivilWorkProduction.objects.create(**defaults)


class DailyCivilWorkProductionViewTest(unittest.TestCase):
    '''
    Tests for DailyCivilWorkProduction
    '''
    def setUp(self):
        self.client = Client()

    def test_list_dailycivilworkproduction(self):
        url = reverse('erp_fiber_ftts_dailycivilworkproduction_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_dailycivilworkproduction(self):
        url = reverse('erp_fiber_ftts_dailycivilworkproduction_create')
        data = {
            "work_day": "work_day",
            "trenched_distance": "trenched_distance",
            "backfilled_distance": "backfilled_distance",
            "duct_installed_length": "duct_installed_length",
            "cable_installed_length": "cable_installed_length",
            "site_dailyproduction_comment": "site_dailyproduction_comment",
            "is_approved": "is_approved",
            "site_name": create_site().pk,
            "project_name": create_fttsproject().pk,
            "posted_by": create_customuser().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_dailycivilworkproduction(self):
        dailycivilworkproduction = create_dailycivilworkproduction()
        url = reverse('erp_fiber_ftts_dailycivilworkproduction_detail', args=[dailycivilworkproduction.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_dailycivilworkproduction(self):
        dailycivilworkproduction = create_dailycivilworkproduction()
        data = {
            "work_day": "work_day",
            "trenched_distance": "trenched_distance",
            "backfilled_distance": "backfilled_distance",
            "duct_installed_length": "duct_installed_length",
            "cable_installed_length": "cable_installed_length",
            "site_dailyproduction_comment": "site_dailyproduction_comment",
            "is_approved": "is_approved",
            "site_name": create_site().pk,
            "project_name": create_fttsproject().pk,
            "posted_by": create_customuser().pk,
        }
        url = reverse('erp_fiber_ftts_dailycivilworkproduction_update', args=[dailycivilworkproduction.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)




