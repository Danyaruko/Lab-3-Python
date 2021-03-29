from sortorder import SortOrder
from foodstoragegoods import FoodStorageGood
from material import Material
from colour import Colour

class ShopManager():
    def __init__(self, items: list):
        print("Shop manager has come to aid!")
        self.__goods = items

    def sort_by_weight(self, order : SortOrder):
        self.__goods.sort(key= lambda FoodStorageGood: FoodStorageGood._weight_in_grams, reverse= order.value)
        return self.__goods

    def sort_by_colour(self, order: SortOrder):
        self.__goods.sort(key= lambda FoodStorageGood: FoodStorageGood._colour.value, reverse= order.value)
        return self.__goods

    def search_by_material(self, material: Material):
        found_goods = [good for good in self.__goods if good._material == material]
        return found_goods