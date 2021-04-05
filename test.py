import unittest
from shopmanager import ShopManager
from basket import Basket
from barrel import Barrel
from lunchbox import Lunchbox
from country import Country
from material import Material
from colour import Colour
from utility import Utility
from sortorder import SortOrder


class TestFoodStorageGoods(unittest.TestCase):
    def setUp(self):
        self.Bertha_the_Barrel = Barrel(size_in_liters=200, weight_in_grams=15000, price_in_uah=500, 
                                        colour=Colour.BLUE, country_of_origin=Country.BULGARIA,
                                        material=Material.WOOD, utility=Utility.DECORATIVE,
                                        hoop_material=Material.METAL)

        self.Boksik_the_Lunchbox = Lunchbox(size_in_liters=2, weight_in_grams=200, price_in_uah=80, 
                                            colour=Colour.RED, country_of_origin=Country.WESTERN_SAHARA,
                                            material=Material.PLASTIC, 
                                            number_of_sections=4, print_on_the_top="Dinosaur")

        self.ContenTainer_the_Lunchbox = Lunchbox(size_in_liters=0.5, weight_in_grams=400, price_in_uah=100, 
                                                  colour=Colour.SILVER, country_of_origin=Country.SWEDEN,
                                                  material=Material.METAL, 
                                                  number_of_sections=2, print_on_the_top="Dinosaur")

        self.Lukoshko_the_Basket = Basket(size_in_liters=20, weight_in_grams=500, price_in_uah=100, 
                                          colour=Colour.WOOD, country_of_origin=Country.RUSSIA,
                                          material=Material.WOOD_BARK, utility=Utility.OUTDOOR_ALLOWED,
                                          number_of_handles=2)

        list_of_goods = [self.Bertha_the_Barrel, self.Boksik_the_Lunchbox,
                         self.ContenTainer_the_Lunchbox, self.Lukoshko_the_Basket]
        self.material = Material.PLASTIC
        self.Serega_the_Shop_Manager = ShopManager(list_of_goods)

    def test_sort_by_weight(self):
        self.assertEqual(self.Serega_the_Shop_Manager.sort_by_weight(SortOrder.ASCENDING), 
                        [self.Boksik_the_Lunchbox, self.ContenTainer_the_Lunchbox, self.Lukoshko_the_Basket,
                         self.Bertha_the_Barrel])

    def test_sort_by_colour(self):
        self.assertEqual(self.Serega_the_Shop_Manager.sort_by_colour(SortOrder.ASCENDING), 
                        [self.Boksik_the_Lunchbox, self.Bertha_the_Barrel, 
                         self.ContenTainer_the_Lunchbox, self.Lukoshko_the_Basket])

    def test_search_by_material(self):
        self.assertEqual(self.Serega_the_Shop_Manager.search_by_material(self.material),
        [self.Boksik_the_Lunchbox])
        
    def test_str(self):
        expected_str_basket=f"Size: 20 l\n"\
                            f"Weight: 500 g\n"\
                            f"Price: 100 UAH\n"\
                            f"Colour: WOOD\n"\
                            f"Manufactured in: RUSSIA\n"\
                            f"Material: WOOD_BARK\n"\
                            f"Utility: OUTDOOR_ALLOWED\n"\
                            f"Number of handles: 2\n"
        expected_str_barrel=f"Size: 200 l\n"\
                            f"Weight: 15000 g\n"\
                            f"Price: 500 UAH\n"\
                            f"Colour: BLUE\n"\
                            f"Manufactured in: BULGARIA\n"\
                            f"Material: WOOD\n"\
                            f"Utility: DECORATIVE\n"\
                            f"Hoop material: METAL\n"
        expected_str_lunchbox=f"Size: 2 l\n"\
                              f"Weight: 200 g\n"\
                              f"Price: 80 UAH\n"\
                              f"Colour: RED\n"\
                              f"Manufactured in: WESTERN_SAHARA\n"\
                              f"Material: PLASTIC\n"\
                              f"Number of sections: 4\n"\
                              f"Print on the top: Dinosaur\n"
        self.assertEqual(str(self.Bertha_the_Barrel), expected_str_barrel)
        self.assertEqual(str(self.Boksik_the_Lunchbox), expected_str_lunchbox)
        self.assertEqual(str(self.Lukoshko_the_Basket), expected_str_basket)

    def test_repr(self):
        expected_list=f"[Size: 2 l\n"\
                      f"Weight: 200 g\n"\
                      f"Price: 80 UAH\n"\
                      f"Colour: RED\n"\
                      f"Manufactured in: WESTERN_SAHARA\n"\
                      f"Material: PLASTIC\n"\
                      f"Number of sections: 4\n"\
                      f"Print on the top: Dinosaur\n"\
                      f", Size: 200 l\n"\
                      f"Weight: 15000 g\n"\
                      f"Price: 500 UAH\n"\
                      f"Colour: BLUE\n"\
                      f"Manufactured in: BULGARIA\n"\
                      f"Material: WOOD\n"\
                      f"Utility: DECORATIVE\n"\
                      f"Hoop material: METAL\n"\
                      f", Size: 0.5 l\n"\
                      f"Weight: 400 g\n"\
                      f"Price: 100 UAH\n"\
                      f"Colour: SILVER\n"\
                      f"Manufactured in: SWEDEN\n"\
                      f"Material: METAL\n"\
                      f"Number of sections: 2\n"\
                      f"Print on the top: Dinosaur\n"\
                      f", Size: 20 l\n"\
                      f"Weight: 500 g\n"\
                      f"Price: 100 UAH\n"\
                      f"Colour: WOOD\n"\
                      f"Manufactured in: RUSSIA\n"\
                      f"Material: WOOD_BARK\n"\
                      f"Utility: OUTDOOR_ALLOWED\n"\
                      f"Number of handles: 2\n"\
                      f"]"    
        self.assertEqual(repr(self.Serega_the_Shop_Manager.sort_by_colour(SortOrder.ASCENDING)), expected_list) 


    