#!/usr/bin/python


def recipe_batches(recipe, ingredients):
    recipe_ingredients = recipe.keys()
    batches = 0
    # Loop until function finds that there aren't enough ingredients
    while 1 == 1:
        for recipe_key in recipe_ingredients:
            # Print message if an ingredient does not exist in ingredients dictionary
            try:
                # Test if there is required amount of current ingredient
                if ingredients[recipe_key] >= recipe[recipe_key]:
                    # Subtract required ingredient quantity from current ingredient dictionary value
                    ingredients[recipe_key] -= recipe[recipe_key]
                # Return current amount of batches if there is not enough of current ingredient
                else:
                    print(f'Not enough {recipe_key}')
                    return batches
            except KeyError:
                print(f'No {recipe_key} in available ingredients')
                return 0
        batches += 1


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    _recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    _ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(_recipe, _ingredients), ingredients=_ingredients))
