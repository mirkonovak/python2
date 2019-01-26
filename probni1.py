magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

for value in range(1,5):
    print(value)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

numbers = list(range(1,1000001))
print(sum(numbers))

