import unittest
from django.urls import reverse
from django.test import Client
from .models import FTTSProject, ProjectTrenching, SiteTrenching, FTTSTrenchingImage
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
    defaults["project_name"] = "project_name"
    defaults["updated_at"] = "updated_at"
    defaults["is_active"] = "is_active"
    defaults["project_type"] = "project_type"
    defaults.update(**kwargs)
    if "site_name" not in defaults:
        defaults["site_name"] = create_site()
    return FTTSProject.objects.create(**defaults)


def create_projecttrenching(**kwargs):
    defaults = {}
    defaults["end_date"] = "end_date"
    defaults["updated_at"] = "updated_at"
    defaults["is_active"] = "is_active"
    defaults.update(**kwargs)
    if "project_name" not in defaults:
        defaults["project_name"] = create_fttsproject()
    if "created_by" not in defaults:
        defaults["created_by"] = create_customuser()
    return ProjectTrenching.objects.create(**defaults)

def create_sitetrenching(**kwargs):
    defaults = {}
    defaults["start_date"] = "start_date"
    defaults["end_date"] = "end_date"
    defaults.update(**kwargs)
    if "project_trenching" not in defaults:
        defaults["project_trenching"] = create_projecttrenching()
    if "site_name" not in defaults:
        defaults["site_name"] = create_site()
    if "created_by" not in defaults:
        defaults["created_by"] = create_customuser()
    return SiteTrenching.objects.create(**defaults)


def create_fttstrenchingimage(**kwargs):
    defaults = {}
    defaults["trenching_day"] = "trenching_day"
    defaults["site_trenching_image_1"] = "site_trenching_image_1"
    defaults["site_trenching_image_2"] = "site_trenching_image_2"
    defaults["site_trenching_image_3"] = "site_trenching_image_3"
    defaults["site_trenching_comment"] = "site_trenching_comment"
    defaults["end_date"] = "end_date"
    defaults["updated_at"] = "updated_at"
    defaults["is_active"] = "is_active"
    defaults.update(**kwargs)
    if "site_trenching" not in defaults:
        defaults["site_trenching"] = create_sitetrenching()
    if "posted_by" not in defaults:
        defaults["posted_by"] = create_customuser()
    return FTTSTrenchingImage.objects.create(**defaults)


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
            "project_type": "project_type",
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
            "project_type": "project_type",
            "site_name": create_site().pk,
        }
        url = reverse('erp_fiber_ftts_fttsproject_update', args=[fttsproject.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProjectTrenchingViewTest(unittest.TestCase):
    '''
    Tests for ProjectTrenching
    '''
    def setUp(self):
        self.client = Client()

    def test_list_projecttrenching(self):
        url = reverse('erp_fiber_ftts_projecttrenching_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_projecttrenching(self):
        url = reverse('erp_fiber_ftts_projecttrenching_create')
        data = {
            "end_date": "end_date",
            "updated_at": "updated_at",
            "is_active": "is_active",
            "project_name": create_fttsproject().pk,
            "created_by": create_customuser().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_projecttrenching(self):
        projecttrenching = create_projecttrenching()
        url = reverse('erp_fiber_ftts_projecttrenching_detail', args=[projecttrenching.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_projecttrenching(self):
        projecttrenching = create_projecttrenching()
        data = {
            "end_date": "end_date",
            "updated_at": "updated_at",
            "is_active": "is_active",
            "project_name": create_fttsproject().pk,
            "created_by": create_customuser().pk,
        }
        url = reverse('erp_fiber_ftts_projecttrenching_update', args=[projecttrenching.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SiteTrenchingViewTest(unittest.TestCase):
    '''
    Tests for SiteTrenching
    '''
    def setUp(self):
        self.client = Client()

    def test_list_sitetrenching(self):
        url = reverse('erp_fiber_ftts_sitetrenching_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sitetrenching(self):
        url = reverse('erp_fiber_ftts_sitetrenching_create')
        data = {
            "start_date": "start_date",
            "end_date": "end_date",
            "project_trenching": create_projecttrenching().pk,
            "site_name": create_site().pk,
            "created_by": create_customuser().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sitetrenching(self):
        sitetrenching = create_sitetrenching()
        url = reverse('erp_fiber_ftts_sitetrenching_detail', args=[sitetrenching.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sitetrenching(self):
        sitetrenching = create_sitetrenching()
        data = {
            "start_date": "start_date",
            "end_date": "end_date",
            "project_trenching": create_projecttrenching().pk,
            "site_name": create_site().pk,
            "created_by": create_customuser().pk,
        }
        url = reverse('erp_fiber_ftts_sitetrenching_update', args=[sitetrenching.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
class FTTSTrenchingImageViewTest(unittest.TestCase):
    '''
    Tests for FTTSTrenchingImage
    '''
    def setUp(self):
        self.client = Client()

    def test_list_fttstrenchingimage(self):
        url = reverse('erp_fiber_ftts_fttstrenchingimage_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_fttstrenchingimage(self):
        url = reverse('erp_fiber_ftts_fttstrenchingimage_create')
        data = {
            "trenching_day": "trenching_day",
            "site_trenching_image_1": "site_trenching_image_1",
            "site_trenching_image_2": "site_trenching_image_2",
            "site_trenching_image_3": "site_trenching_image_3",
            "site_trenching_comment": "site_trenching_comment",
            "end_date": "end_date",
            "updated_at": "updated_at",
            "is_active": "is_active",
            "site_trenching": create_sitetrenching().pk,
            "posted_by": create_customuser().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_fttstrenchingimage(self):
        fttstrenchingimage = create_fttstrenchingimage()
        url = reverse('erp_fiber_ftts_fttstrenchingimage_detail', args=[fttstrenchingimage.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_fttstrenchingimage(self):
        fttstrenchingimage = create_fttstrenchingimage()
        data = {
            "trenching_day": "trenching_day",
            "site_trenching_image_1": "site_trenching_image_1",
            "site_trenching_image_2": "site_trenching_image_2",
            "site_trenching_image_3": "site_trenching_image_3",
            "site_trenching_comment": "site_trenching_comment",
            "end_date": "end_date",
            "updated_at": "updated_at",
            "is_active": "is_active",
            "site_trenching": create_sitetrenching().pk,
            "posted_by": create_customuser().pk,
        }
        url = reverse('erp_fiber_ftts_fttstrenchingimage_update', args=[fttstrenchingimage.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
