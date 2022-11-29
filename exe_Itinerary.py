class Itinerary:

    @classmethod
    def from_location(cls, *locations):
        return cls(locations)  # iterable tuple

    def __init__(self, locations):
        self._locations = list(locations)

    def __str__(self):
        return '\n'.join(location.name for location in self._locations)

    @property
    def locations(self):
        return tuple(self._locations)

    @property
    def origin(self):
        return self._locations[0]  # zwraca pierwszy element

    @property
    def destination(self):
        return self._locations[-1]

    def add(self, location):
        self._locations.append(location)

    def remove(self, name):
        self._locations = [location for location in self._locations if location.name != name]
        # location.name obiekt klasy Location -> tam przyjmuje parametr name

    def truncate_at(self, name):
        # Np. przyjmujemy Łódź i po łodzi wszytko kasujemy
        stop = 0

        for idx, location in enumerate(self._locations): # wyciąga index
            if location.name == name:
                stop = idx + 1
                break

            self._locations = self._locations[:stop]
