
class TeaLeaf:

    def __init__(self , age):
        self._age = age

    @property
    def _age(self):
        return self._age 

    @_age.setter
    def _age(self , age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea Leaf age Must be between 1 and 5 years!")

leaf = TeaLeaf(7)
print(leaf.age)
