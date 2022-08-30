animal_sounds = {
    'cow': 'moo',
    'chick': 'click-click',
    'pig': 'oink-oink',
    'sheep': 'baaa baaa',
    'duck': 'quack'
}


def print_lyrics(animal):
    sound = animal_sounds[animal]
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print(f"And on that farm he had a {animal}, Ee-igh, Ee-igh, Oh!")
    print(f"With a {sound}, {sound} here and a {sound}, {sound} there.")
    print(f"With a {sound}, there a {sound}, everywhere a {sound}, {sound}.")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh! \n")


print_lyrics('cow')
print_lyrics('chick')
print_lyrics('pig')
print_lyrics('sheep')
print_lyrics('duck')
