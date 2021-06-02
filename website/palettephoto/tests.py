from django.test import TestCase, Client
from django.urls import reverse

#Test de la page d'accueil
class PageAccueilTestCase(TestCase):
    def test_page_accueil(self):
        response = self.client.get(reverse('palettephoto:index'))
        self.assertTemplateUsed(response, 'palettephoto/base.html')
        self.assertTemplateUsed(response, 'palettephoto/index.html')
        self.assertEqual(response.request.get('PATH_INFO'), "/")
        self.assertEqual(response.status_code, 200)