import argparse

# 1. Skapa ett parser-objekt som är beredd på att ta emot argument från CLI
parser = argparse.ArgumentParser(description='A python script that accepts arguments from the terminal, and greets the user.')

# 2. Lägg till argument som vi vill kunna ta emot från CLI

# mandatory
parser.add_argument('--name', type=str, help='Your name', required=True)

# optional
parser.add_argument('--age', type=float, default=25, help='Your age')
parser.add_argument('--city', type=str, default=None, help='The city you live in')

# 3. Parsa argumenten från CLI, dvs processa argumenten och lägg in allt i variabeln args
args = parser.parse_args()

print(f'args.name har fått värdet {args.name}')
print(f'args.age har fått värdet {args.age}')
print(f'args.city har fått värdet {args.city}')


def greet(name, age=None, city='Unknown'):

    print(f'Hello {name}!')
    
    if age:                                 # detta kommer evalueras till False, om vi inte ändrar default-värdet av age
                                            # by default har age värdet None, och satsen evalueras därför till False här
        print(f'You are {age} years old.')

    print(f'You live in {city}')

greet(name=args.name, age=args.age, city=args.city)