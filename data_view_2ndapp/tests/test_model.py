from django.test import TestCase
from data_view_2ndapp.models import immo_bienny

# class ModelTesting(TestCase):
#     def setUp(self):
#         self.data_view = immo_bienny.objects.create(id_lot='django', nb_piece='django')


#     def test_post_model(self):
#         d = self.data_view
#         self.assertTrue(isinstance(d, immo_bienny))
#         self.assertEqual(str(d, 'django'))

class ModelTesting(TestCase):
    @classmethod
    def setUpTestmodel(cls):
        immo_bienny.objects.create(id_lot="42_4_GardenCity-Inten'City_Bouygues", typologie="Appartemente")

    def test_id_lot_label(self):
        immo = immo_bienny.objects.get(id=1)
        field_label = immo._meta.get_field('id_lot').verbose_name
        self.assertEqual(field_label, 'id_lot')

    def test_date_extraction_label(self):
        immo = immo_bienny.objects.get(id=1)
        field_label = immo._meta.get_field('date_extraction').verbose_name
        self.assertEqual(field_label, 'date_extraction')

    def test_id_lot_max_length(self):
        immo = immo_bienny.objects.get(id=1)
        max_length = immo._meta.get_field('id_lot').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_id_lot_Appartement_commae(self):
        immo = immo_bienny.objects.get(id=1)
        expected_object_name = f'{immo.id_lot}, {immo.Appartemente}'
        self.assertEqual(str(immo), expected_object_name)



