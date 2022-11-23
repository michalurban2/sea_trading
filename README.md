# Sea trading

## Python OP
- class
- object self
- self = object
- method
    - default (self)
    - staticmethod ()
    - classmethod (cls)
- field/attributes
  - object field (self)
  - class field
- python features (magic methods)
    - `__str__` -> string 
    - `__len__` -> int (ilość elementów wewnątrz obiektu), każda klasa może mieć
    - `__repr__` -> string -> reprezentacja obiektu dla programisty 
    - `__formant__` -> string (pozwala dodawać formatter`y) x.format(), 
    - `__name__` -> string (nazwa klasy)
    - `__init__` -> zawraca None (x = x()) - setowanie pól obiektu DRUGI
    - `__new__` -> self/object (constructor) PIERWSZY
    - `__dict__` -> pola 
- constructor (metoda, która tworzy object '__new__')
- object descriptor/data object descriptor (getter/setter/setter)
- property - class data object descriptor property
- super() -> wywołuje metodę rodzica (MRO), wywołuje pierwszą, która znajdzie
- MRO - method resolution order (C3)

## OOP
1. Abstraction -> złożona logika w prosty sposób
2. Inheritence -> kopiowanie pól i metod
3. Polymorphish -> ta sama rzecz na wiele sposobów
4. Encaptulation (Hermetyzacja) - ograniczenie dostępu
  - private -> tylko tam gdzie zostało stworzone
  - protected -> w klasie i dzieciach
  - public -> wszedzie (wewnątrz i na zewnatrz klas)
  - read_only

## SOLID
1. Single responsibility principle -> każda klasa zajmuje się jedną rzeczą
2. Open/close principal -> otwarta na dziedziczenie i zamknięta modyfikacje
3. Liskov Substitution Principle -> dowolny objekt klasy bazowej może zostać zastąpiony
4. Interface segregation -> odseparować logikę od szczegółów implementacji 
5. Dependency inversion -> rodzic nie może istnieć bez dziecka

## Hierarchy
- Interface - requirements, no implementation detail (no in python)
- Abstract Class - requirements, partially implementation details
- Concrete Class - implementation detail

---

- metaclass -> tworzenie klasy
- class -> tworzenie obiektu
- object 


```python

class X:
    b = 'on class'
    
    def __init__(self):
        self.a = 'on instance'
        print(self.a)
        print(X.b)
        self.a = 're-bound'
        self.b = 'new on instance'
         
        print(self.b)
        print(X.b)
```
