from django.test import TestCase
from modeling.models import Creature
from django.http import HttpRequest
from modeling.views import *

class CreatrueModelTest(TestCase):
    def test_retrieving_items(self):
        Creature.objects.create(c_id="355488")
        first_item = Creature.objects.first()
        self.assertEqual(first_item.c_id, "355488")

    
    def test_search_results(self):
        Creature.objects.create(c_name="Roach")
        # because in test environment,
        # the test db is empty, so we have to create a record for test
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = "Roa"
        response = results(request)
        self.assertIn("Roa", response.content.decode())

    def test_creature_search(self):
        Creature.objects.create(c_name="Roach", location="3333")
        creature, pages = creature_search(['3333'])
        self.assertEqual(pages, 1)
        self.assertEqual('Roach', creature[0].c_name)

    def test_location_detail(self):
        Creature.objects.create(c_name="Roach", location="3333")
        Creature.objects.create(c_name="Python", location="2222", c_id="09852")
        response = self.client.post(
            '/location_detail',
            data={'locations': '2222,3333,'}
        )
        self.assertIn('Roach', response.content.decode())
        self.assertIn('Python', response.content.decode())

    def test_page(self):
        for i in range(15):
            Creature.objects.create(c_name="Roach"+str(i), c_id=str(i), location="3333")
        response = self.client.get('/location_detail/3/',{'locations':'3333,'})
        self.assertIn("<td><b>3</b></td>", response.content.decode())

    def test_auto(self):
        Creature.objects.create(c_name="Children's Python", c_id="1111")
        Creature.objects.create(c_name="Pygmy Python", c_id="1112")
        request = HttpRequest()
        request.method = "GET"
        request.GET['item_text'] = "Python"
        response = auto(request).content.decode()
        self.assertIn('Pygmy Python', response)