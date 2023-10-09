from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from mock import patch, Mock, MagicMock
from os import environ


class ApiTests(APITestCase):
    """Class representing tests for the api"""
    @patch('requests.post')
    def test_prompt_violates_content_policy(self, mock_request):
        """
        Sent prompt violates content policy
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'violates_content_policy': True
        }
        mock_request.return_value = mock_response
        url = reverse('poem')
        response = self.client.post(
            url, {'prompt': 'naturaleza'}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['violates_content_policy'], True)

    @patch('requests.post')
    def test_success(self, request_mock):
        """
        Generate poem and image successfuly
        """
        mock_response = {
            'violates_content_policy': False,
            'text': 'Poem',
            'image': 'url_image'
        }

        m1 = MagicMock()
        m1.json.return_value = {
            'violates_content_policy': mock_response['violates_content_policy']}
        m2 = MagicMock()
        m2.json.return_value = {'text': mock_response['text']}
        m3 = MagicMock()
        m3.json.return_value = {'image': mock_response['image']}

        request_mock.side_effect = Mock(side_effect=[m1, m2, m3])

        url = reverse('poem')
        response = self.client.post(
            url, {'prompt': 'naturaleza'}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), mock_response)
