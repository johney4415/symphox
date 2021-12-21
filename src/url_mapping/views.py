from django.shortcuts import render
from rest_framework.views import APIView
from shortener.helper import CustomJsonResponse

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import string
import random
from url_mapping.models import UrlMapping
from django.conf import settings
import urllib
from django.shortcuts import redirect

urllib.parse.urljoin
my_domain = getattr(settings, 'DOMAIN') or 'http://127.0.0.1:8000'


class ShortenerView(APIView):
    @swagger_auto_schema(operation_summary='S01-01 short url',
                         operation_description='given url, return shorted url',
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 'url':
                                 openapi.Schema(
                                     type=openapi.TYPE_STRING,
                                     description='url',
                                     example='https://www.google.com'),
                             }))
    def post(self, request):
        origin_url = request.data.get('url')
        obj, created = UrlMapping.objects.get_or_create(origin_url=origin_url)
        if created:
            obj.pk
            letters = string.ascii_letters
            code = ''.join(random.choice(letters) for i in range(20))
            obj.shortener_url = code
            obj.save()
        else:
            code = obj.shortener_url
        result = {
            "origin_url":
            origin_url,
            "short_url":
            urllib.parse.urljoin(my_domain, f'short/{obj.shortener_url}')
        }
        return CustomJsonResponse(result_data=result, return_message='success')


class RecoveryUrlView(APIView):
    @swagger_auto_schema(
        operation_summary='S01-02 revovery url', )
    def get(self, request, shorted_url):
        errors = {}
        try:
            obj = UrlMapping.objects.get(shortener_url=shorted_url)
        except UrlMapping.DoesNotExist:
            errors['url_error'] = f"url does not exist."
        except Exception as e:
            errors['error'] = e
        if errors:
            return CustomJsonResponse(
                result_data=errors,
                return_message="can not find this url code")
        return redirect(obj.origin_url)
        # result = {"url": obj.origin_url}
        # return CustomJsonResponse(result_data=result, return_message='success')