from example_32_enums import Person, TimeOfDay


class Cowboy(Person):
    def greet(self, time_of_day=None):
        if not time_of_day or not isinstance(time_of_day, TimeOfDay):
            return f'Howdy, {self.name}!'
        return f'Good {time_of_day}, {self.name}!'

    def __repr__(self):
        return f'Cowboy("{repr(self.name)}")'  # Cowboy("Name")


if __name__ == '__main__':
    cowboy = Cowboy('Woody')
    print(cowboy.greet())  # Howdy, Woody!
