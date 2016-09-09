from django.test import TestCase
from django.conf import settings


class SettingsTestCase(TestCase):

    def test_modified_settings(self):
        with self.settings(CHATTERBOT={'name': 'Jim'}):
            self.assertIn('name', settings.CHATTERBOT)
            self.assertEqual('Jim', settings.CHATTERBOT['name'])

    def test_name_setting(self):
        from django.core.urlresolvers import reverse

        api_url = reverse('chatterbot:chatterbot')
        response = self.client.get(api_url)

        self.assertEqual(response.status_code, 405)
        self.assertIn('detail', response.content)
        self.assertIn('name', response.content)
        self.assertIn('Django ChatterBot Example', response.content)