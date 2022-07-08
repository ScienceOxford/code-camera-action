from random import choice

characters = ['an apple', 'a cat', 'a dragon', 'a fairy', 'a firefighter', 'me', 'a monarch', 'a mushroom', 'a pizza', 'a robot', 'a scientist', 'a unicorn']
locations = ['a boat', 'a cave', 'a computer', 'a factory', 'the future', 'outer space', 'a parallel universe', 'the past', 'a science centre', 'a shop', 'a thunder storm', 'the woods']
styles = ['an adventurous', 'a confusing', 'a dramatic', 'an exciting', 'a fantastical', 'a funny', 'a happy', 'a mysterious', 'a predictable', 'a romantic', 'a scary', 'a strange']

print("This story is about " + choice(characters) + " in " + choice(locations) + ".")
print("It is " + choice(styles) + " story.")
