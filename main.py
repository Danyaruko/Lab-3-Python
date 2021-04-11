from shopmanager import ShopManager
from basket import Basket
from barrel import Barrel
from lunchbox import Lunchbox
from country import Country
from material import Material
from colour import Colour
from utility import Utility
from sortorder import SortOrder

def main():
    Bertha_the_Barrel = Barrel(size_in_liters=200, weight_in_grams=15000, price_in_uah=500, 
                    colour=Colour.BLUE, country_of_origin=Country.BULGARIA,
                    material=Material.WOOD, utility=Utility.DECORATIVE, hoop_material=Material.METAL)
    print(Bertha_the_Barrel)

    list_of_goods = []
    list_of_goods.append(Bertha_the_Barrel)

    Boksik_the_Lunchbox = Lunchbox(size_in_liters=2, weight_in_grams=200, price_in_uah=80, 
                      colour=Colour.RED, country_of_origin=Country.WESTERN_SAHARA,
                      material=Material.PLASTIC, 
                      number_of_sections=4, print_on_the_top="Dinosaur")
    print(Boksik_the_Lunchbox)

    ContenTainer_the_Lunchbox = Lunchbox(size_in_liters=0.5, weight_in_grams=400, price_in_uah=100, 
                colour=Colour.SILVER, country_of_origin=Country.SWEDEN,
                material=Material.METAL, 
                number_of_sections=2, print_on_the_top="Dinosaur")
    print(ContenTainer_the_Lunchbox)

    Lukoshko_the_Basket = Basket(size_in_liters=20, weight_in_grams=500, price_in_uah=100, 
                      colour=Colour.WOOD, country_of_origin=Country.RUSSIA,
                      material=Material.WOOD_BARK, utility=Utility.OUTDOOR_ALLOWED,
                      number_of_handles=2)
    print(Lukoshko_the_Basket)

    list_of_goods.append(Boksik_the_Lunchbox)
    list_of_goods.append(ContenTainer_the_Lunchbox)
    list_of_goods.append(Lukoshko_the_Basket)
    print(list_of_goods)

    Serega_the_Shop_Manager = ShopManager(list_of_goods)
    Serega_the_Shop_Manager.sort_by_weight( order= SortOrder.DESCENDING)

    print("Sorted list_of_goods by weight")
    print(list_of_goods)

    Serega_the_Shop_Manager.sort_by_colour( order= SortOrder.ASCENDING)

    print("Sorted list_of_goods by colour")
    print(list_of_goods)
    print(Serega_the_Shop_Manager.search_by_material(material= Material.PLASTIC))


if __name__ == "__main__":
    main()
