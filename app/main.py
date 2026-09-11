"""Module for animal feeding simulation."""


class Animal:
    """Base class representing an animal that can eat."""

    def __init__(self, name: str, appetite: int, is_hungry: bool = True) -> None:
        """Initialize the animal with name, appetite, and hunger status.

        Args:
            name (str): The name of the animal.
            appetite (int): Food points needed to be full.
            is_hungry (bool): Whether the animal is hungry. Defaults to True.
        """
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        """Print a greeting with the animal's name."""
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        """Feed the animal if hungry.

        Returns:
            int: Number of food points eaten, or 0 if not hungry.
        """
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):
    """Cat class inheriting from Animal with fixed appetite of 3."""

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        """Initialize the cat.

        Args:
            name (str): The name of the cat.
            is_hungry (bool): Whether the cat is hungry. Defaults to True.
        """
        super().__init__(name, 3, is_hungry)

    def catch_mouse(self) -> None:
        """Simulate catching a mouse."""
        print("The hunt began!")


class Dog(Animal):
    """Dog class inheriting from Animal with fixed appetite of 7."""

    def __init__(self, name: str, is_hungry: bool = True) -> None:
        """Initialize the dog.

        Args:
            name (str): The name of the dog.
            is_hungry (bool): Whether the dog is hungry. Defaults to True.
        """
        super().__init__(name, 7, is_hungry)

    def bring_slippers(self) -> None:
        """Simulate bringing slippers."""
        print("The slippers delivered!")


def feed_animals(animals_list: list[Animal]) -> int:
    """Feed a list of animals and return total food points consumed.

    Args:
        animals_list (list[Animal]): List of animal instances to feed.

    Returns:
        int: Total food points eaten by all hungry animals.
    """
    total_food_points = 0
    for animal in animals_list:
        total_food_points += animal.feed()
    return total_food_points

