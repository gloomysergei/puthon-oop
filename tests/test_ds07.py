from design.ds07 import Pizza, PizzaBuilder, create_classic_pizza


def test_builder_creates_pizza():
    pizza = (
        PizzaBuilder()
        .set_size("big")
        .set_dough("thin")
        .set_sauce("tomato")
        .set_meat_topping("pepperoni")
        .set_vegetable_topping("olive")
        .set_cheese_topping("mozzarella")
        .get_pizza()
    )

    assert pizza.get_size() == "big"
    assert pizza.get_dough() == "thin"
    assert pizza.get_sauce() == "tomato"
    assert pizza.get_meat_topping() == "pepperoni"
    assert pizza.get_vegetable_topping() == "olive"
    assert pizza.get_cheese_topping() == "mozzarella"


def test_builder_allows_missing_toppings():
    pizza = PizzaBuilder().set_size("small").get_pizza()

    assert pizza.get_size() == "small"
    assert pizza.get_meat_topping() is None
    assert pizza.get_vegetable_topping() is None


def test_create_classic_pizza_returns_margarita():
    pizza = create_classic_pizza()

    assert isinstance(pizza, Pizza)
    assert pizza.get_size() == "big"
    assert pizza.get_dough() == "thin"
    assert pizza.get_sauce() == "tomato"
    assert pizza.get_vegetable_topping() == "basil"
    assert pizza.get_cheese_topping() == "mozzarella"
    assert pizza.get_meat_topping() is None