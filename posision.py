class Position:
    def __init__(self, latitute, longitute):
        if not (-90 <= latitute <= 90):
            raise ValueError(f'Latitute {latitute} out of range')

        if not (-180 <= latitute <= 180):
            raise ValueError(f'longitute {longitute} out of range')

        self._latitute = latitute
        self._longitude = longitute

    @property
    def latitude(self):
        return self._latitute

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemishere(self):
        return 'N' if self.latitude >= 0 else 'S'

    @property
    def longitude_hemishere(self):
        return 'E' if self.latitude >= 0 else 'W'

    def __repr__(self):
        return f'{type(self).__name__} (latitude={self._longitude}, longitude={self._longitude}'

    def __str__(self):
        return f'{abs(self.latitude)}° {self.latitude_hemishere}, {abs(self.longitude)}° {self.latitude_hemishere}'

    def __format__(self, format_spec):
        print(format_spec)
        component_format_spec = '2.f'

        prefix, dot, suffix = format_spec.partition('.')

        if dot:
            component_format_spec = f'.{suffix}f'

        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return f'{latitude}° {self.latitude_hemishere}, {longitude}° {self.longitude_hemishere}'


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


waw = EarthPosition(52.1, 21)
print(waw)
print(repr(waw))
print(f'{waw:.3f}')