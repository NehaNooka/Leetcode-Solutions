class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook={s:True for s in supplies} #r-> T/F
        recipe_index={r:i for i,r in enumerate(recipes)}
        def dfs(r):
            if r in can_cook: return can_cook[r]
            if r not in recipe_index: return False # ing not in supplies, return False
            can_cook[r]=False #To avoid circular dep
            for nei in ingredients[recipe_index[r]]:
                if not dfs(nei):
                    return False
            can_cook[r]=True
            return can_cook[r]

        return [ r for r in recipes if dfs(r)]


        