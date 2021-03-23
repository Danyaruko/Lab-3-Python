from sortorder import SortOrder
from foodstoragegoods import FoodStorageGood
from material import Material
from colour import Colour

class ShopManager():
    def __init__(self):
        print("Shop manager has come to aid!")

    def sort_by_weight(self, items: list, order : SortOrder):
        items.sort(key= lambda FoodStorageGood: FoodStorageGood._weight_in_grams, reverse= order.value)
        self.__goods = items

    def sort_by_colour(self, items: list, order: SortOrder):
        items.sort(key= lambda FoodStorageGood: FoodStorageGood._colour.value, reverse= order.value)
        self.__goods = items

    def search_by_material(self, material: Material):
        found_goods = [good for good in self.__goods if good._material == material]
        return found_goods