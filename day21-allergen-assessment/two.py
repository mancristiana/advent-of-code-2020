
def main():
    with open('input.txt') as file:
        lines = file.read().split("\n")
    allergensDictionary = {}
    for line in lines:
        ingredients, allergens = getIngredientsAndAllergens(line)
        for allergen in allergens:
            if (allergen in allergensDictionary):
                allergensDictionary[allergen].append(ingredients)
            else:
                allergensDictionary[allergen] = [ingredients]
    print(solve(allergensDictionary))


def getIngredientsAndAllergens(line):
    [ingredientsData, allergensData] = line.replace(
        ")", "").split(" (contains ")
    ingredients = ingredientsData.split(" ")
    allergens = allergensData.split(", ")
    return ingredients, allergens


def solve(allergensDictionary):
    for allergen, ingredientLists in allergensDictionary.items():
        allergensDictionary[allergen] = findCommonIngredients(ingredientLists)
    ingredientsContainingAllergens = getIngredientsContainingAllergens(allergensDictionary)
    sortedIngredients = sorted(ingredientsContainingAllergens.items(), key=lambda x: x[1])
    return ",".join([ingredient for ingredient, allergen in sortedIngredients])
    

def findCommonIngredients(ingredientLists):
    commonIngredients = []
    firstList = ingredientLists[0]
    for ingredient in firstList:
        isCommon = True
        for listIndex in range(1, len(ingredientLists)):
            if (not ingredient in ingredientLists[listIndex]):
                isCommon = False
                break
        if (isCommon):
            commonIngredients.append(ingredient)
    return commonIngredients

def getIngredientsContainingAllergens(allergensDictionary):
    ingredients = {}
    
    while len(allergensDictionary.keys()) > 0:
        for allergen, possibleIngredients in allergensDictionary.items():
            if (len(possibleIngredients) == 1):
                foundIngredient = possibleIngredients[0]
                ingredients[foundIngredient] = allergen
                allergensDictionary.pop(allergen)
                for a in allergensDictionary.keys():
                    if (foundIngredient in allergensDictionary[a]):
                        allergensDictionary[a].remove(foundIngredient)
                break

    return ingredients

if __name__ == "__main__":
    main()
