from typing import Optional

class Pizza:
    def __init__(
        self,
        size: Optional[str],
        dough: Optional[str],
        sauce: Optional[str],
        meat_topping: Optional[str],
        vegetable_topping: Optional[str],
        cheese_topping: Optional[str],
    ) -> None:
        self._size = size
        self._dough = dough
        self._sauce = sauce
        self._meat_topping = meat_topping
        self._vegetable_topping = vegetable_topping
        self._cheese_topping = cheese_topping

    def get_size(self) -> Optional[str]:
        return self._size

    def get_dough(self) -> Optional[str]:
        return self._dough

    def get_sauce(self) -> Optional[str]:
        return self._sauce

    def get_meat_topping(self) -> Optional[str]:
        return self._meat_topping

    def get_vegetable_topping(self) -> Optional[str]:
        return self._vegetable_topping

    def get_cheese_topping(self) -> Optional[str]:
        return self._cheese_topping

    @staticmethod
    def builder() -> "PizzaBuilder":
        return PizzaBuilder()

# BEGIN (write your solution here)
class PizzaBuilder:
    def __init__(self) -> None:
        # сначала ничего не задано
        self._size: Optional[str] = None
        self._dough: Optional[str] = None
        self._sauce: Optional[str] = None
        self._meat_topping: Optional[str] = None
        self._vegetable_topping: Optional[str] = None
        self._cheese_topping: Optional[str] = None
    
    # методы для установки ингредиентов    
    def set_size(self, size: str) -> 'PizzaBuilder':
        self._size = size
        return self
    
    def set_dough(self, dough: str) -> 'PizzaBuilder':
        self._dough = dough
        return self
        
    def set_sauce(self, sauce: str) -> 'PizzaBuilder':
        self._sauce = sauce
        return self
    
    def set_meat_topping(self, meat_topping: str) -> 'PizzaBuilder':
        self._meat_topping = meat_topping
        return self
        
    def set_vegetable_topping(self, vegetable_topping: str) -> 'PizzaBuilder':
        self._vegetable_topping = vegetable_topping
        return self
            
    def set_cheese_topping(self, cheese_topping: str) -> 'PizzaBuilder':
        self._cheese_topping = cheese_topping
        return self
    
    def get_pizza(self) -> Pizza:
        return Pizza(
            size = self._size,
            dough = self._dough,
            sauce = self._sauce,
            meat_topping = self._meat_topping,
            vegetable_topping = self._vegetable_topping,
            cheese_topping = self._cheese_topping
        )

def create_classic_pizza():
    pizza = (
        Pizza.builder()
        .set_size('big')
        .set_dough('thin')
        .set_sauce('tomato')
        .set_vegetable_topping('basil')
        .set_cheese_topping('mozzarella')
        .get_pizza()
    )
    return pizza
# END

