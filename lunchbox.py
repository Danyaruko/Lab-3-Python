from foodstoragegoods import FoodStorageGood
from country import Country
from material import Material
from colour import Colour

class Lunchbox(FoodStorageGood):
    def __init__(self, size_in_liters=0.0, weight_in_grams=0.0, price_in_uah=0.0, 
                 colour=Colour.TRANSPARENT, material=Material.WOOD, 
                 country_of_origin=Country.RUSSIA, number_of_sections=0, 
                 print_on_the_top="None"):
        super().__init__(size_in_liters, weight_in_grams, price_in_uah, 
                         colour, material, country_of_origin,)
        print("It's a lunchbox!")
        self.__number_of_sections = number_of_sections
        self.__print_on_the_top = print_on_the_top
        
    def __str__(self):
        return f"{super().__str__()}\n"\
               f"Number of sections: {self.__number_of_sections}\n"\
               f"Print on the top: {self.__print_on_the_top}\n"

    def __repr__(self):
        return f"{super().__repr__()}\n"\
               f"Number of sections: {self.__number_of_sections}\n"\
               f"Print on the top: {self.__print_on_the_top}\n"