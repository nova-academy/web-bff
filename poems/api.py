"""Importing modules"""
import threading
import os
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .serializers import PoemSerializer


class PoemView(APIView):
    """Class representing entity to retrieve"""

    def post(self, request):
        """Returns result of miscroservices calls"""

    def __call_apis_multithread(self, request, response):
        pass

    def __analyze_sentiment(self, request):
        pass

    def __get_generate_text(self, url, req, response):
        pass

    def __get_generate_image(self, url, req, response):
        pass
