from shopmanager import ShopManager
from basket import Basket
from barrel import Barrel
from lunchbox import Lunchbox
from country import Country
from material import Material
from colour import Colour
from utility import Utility
from sortorder import SortOrder


Bertha = Barrel(size_in_liters=200, weight_in_grams=15000, price_in_uah=500, 
                colour=Colour.BLUE, country_of_origin=Country.BULGARIA,
                material=Material.WOOD, utility=Utility.DECORATIVE, hoop_material=Material.METAL)

print(Bertha)

list_of_goods = []
list_of_goods.append(Bertha)

Boksik = Lunchbox(size_in_liters=2, weight_in_grams=200, price_in_uah=80, 
                colour=Colour.RED, country_of_origin=Country.WESTERN_SAHARA,
                material=Material.PLASTIC, 
                number_of_sections=4, print_on_the_top="Dinosaur")
print(Boksik)

ContenTainer = Lunchbox(size_in_liters=0.5, weight_in_grams=400, price_in_uah=100, 
                colour=Colour.SILVER, country_of_origin=Country.SWEDEN,
                material=Material.METAL, 
                number_of_sections=2, print_on_the_top="Dinosaur")
print(Boksik)

Lukoshko = Basket(size_in_liters=20, weight_in_grams=500, price_in_uah=100, 
                colour=Colour.WOOD, country_of_origin=Country.RUSSIA,
                material=Material.WOOD_BARK, utility=Utility.OUTDOOR_ALLOWED,
                number_of_handles=2)
print(Lukoshko)

list_of_goods.append(Boksik)
list_of_goods.append(Lukoshko)
print(list_of_goods)

Serega = ShopManager()
Serega.sort_by_weight(list_of_goods, order= SortOrder.DESCENDING)

print(list_of_goods)

Serega.sort_by_colour(list_of_goods, order= SortOrder.ASCENDING)

print(list_of_goods)

print(Serega.search_by_material(material= Material.PLASTIC))