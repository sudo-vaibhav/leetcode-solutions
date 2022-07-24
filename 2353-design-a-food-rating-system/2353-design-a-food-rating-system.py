from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.m = defaultdict(SortedSet)
        self.foodMap = {}
        self.foodCuisine = {}
        for i,cus in enumerate(cuisines):
            self.m[cus].add((-ratings[i],foods[i]))
            self.foodMap[foods[i]] = -ratings[i]
            self.foodCuisine[foods[i]] = cuisines[i] 
    def changeRating(self, food: str, newRating: int) -> None:
            entry = (self.foodMap[food],food)
            cus = self.foodCuisine[food]
            self.m[cus].remove(entry)
            newEntry = (-newRating,food)
            self.m[cus].add(newEntry)
            self.foodMap[food] = -newRating
    
    def highestRated(self, cuisine: str) -> str:
        return self.m[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)