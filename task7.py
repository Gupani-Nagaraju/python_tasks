#custom Context manager
class ResourceManager:
    def __enter__(self):
        print("Enterd into the Resource")
        return self

    def __exit__(self, exc_type,exc_val,traceback):
        print("Resource Released")

        if exc_type:
            print(f"The exception is {exc_val}")

        return False

# Custom Iterator
class NumberIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


# Context Manager Demo
print("Context Manager Demo")

with ResourceManager():
    print("Working with the resource...")


print("\nIterator Demo")

# Iterator Demo
numbers = NumberIterator(5)

for number in numbers:
    print(number)