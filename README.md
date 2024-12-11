This implementation includes several improvements and different approaches compared to the original code:

1. I use a `Contact` class with `@dataclass` decorator for cleaner and more structured contact representation.
2. The `ContactManager` class encapsulates all the functionality related to managing contacts.
3. I use type hints throughout the code for better readability and potential static type checking.
4. Error handling is improved, especially when loading the JSON file and getting user input.
5. The `save_contacts` method now writes JSON with indentation for better readability.
6. I've added a demonstration section at the end to show how the program works without requiring user input.


This implementation provides a more object-oriented approach to the Contact Management System, 
making it easier to maintain and extend in the future. It also demonstrates some more advanced 
Python features while retaining the original program's core functionality.
