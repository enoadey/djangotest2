# #import pytest
# from django.test import TestCase
# from data_view_2ndapp.models import *

# #pytestmark = pytest.mark.django_db

# class TestimmoModel(TestCase):

#     def test_model_str(self):
#         id_lot = immo_bienny.objects.create(id_lot="TestingDjango")
#         #nb_piece = immo_bienny.objects.create(nb_piece="This is piece")
#         #product = immo_bienny.objects.create(name="Maison", prix_HT=1000)
#         self. assertEqual(str(id_lot), "DjangoTesting")
#         #assert product.name == "Maison"
#         #assert product.prix_HT == 1000

#     def test_post_users_like(self):
#         testuser = User.objects.create_user(username='testuser', password='67890')
#         testuser2 = User.objects.create_user(username='testuser2', password='67890')
#         id_lot = immo_bienny.objects.create(id_lot="django", nb_piece="new content")
#         id_lot.likes.set([testuser.pk, testuser2.pk])
#         self.assertEqual(id_lot.likes.count(), 2)
