from guizero import App, Text, PushButton
from random import choice

app = App(title="Random Story Generator", height=200, width=1000)

characters = ['an apple', 'a cat', 'a dragon', 'a fairy', 'a firefighter', 'me', 'a monarch', 'a mushroom', 'a pizza', 'a robot', 'a scientist', 'a unicorn']
locations = ['a boat', 'a cave', 'a computer', 'a factory', 'the future', 'outer space', 'a parallel universe', 'the past', 'a science centre', 'a shop', 'a thunder storm', 'the woods']
styles = ['an adventurous', 'a confusing', 'a dramatic', 'an exciting', 'a fantastical', 'a funny', 'a happy', 'a mysterious', 'a predictable', 'a romantic', 'a scary', 'a strange']

story = ['a character', 'a location', 'a']

def roll():
    global story, message
    character = choice(characters)
    location = choice(locations)
    style = choice(styles)
    story = [character, location, style]
    print('rolled')
    message.value = "This story is about " + story[0] + " in " + story[1] + "." + "\n" + "It is " + story[2] + " story."
    return story

print("This story is about " + story[0] + " in " + story[1] + ".")
print("It is " + story[2] + " story.")

message = Text(app, text="This story is about " + story[0] + " in " + story[1] + "." + "\n" + "It is " + story[2] + " story.", size=24)
reroll = PushButton(app, text="Re-roll!", command=roll)
reroll.text_size = 24
reroll.bg = 'gold'

app.display()
