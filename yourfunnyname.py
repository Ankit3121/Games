import sys
import random

first = ('Fatela', 'Chhakka', 'Chaman', "Randibaaz",
"John", 'Gandu', 'Anurag', "Mia",
'johnny', 'Ankit', 'Amit', 'Ronny', 'Dinesh',
'Bhadwa', 'Ava', 'Madarchod', 'Yogesh', 'Ravindra', 'Bahinchod',
'Batman', 'Laden', 'Lodu', 'Dickman', 'Bhasad',
'Vagina', 'kaala', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
'Lemongrass', 'Lil Debil', 'Bhosadiwale', 'chacha',
'Mergatroid', '"Mr Peabody"', 'Oil­Can', 'Hawasi', 'Old Scratch',
'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
'Pushmeet','Rock Candy', 'Schlomo', 'Ratan', 'Pubg',
"Sid 'The Squirts'", 'timma', 'Slaps', 'Snakes', 'Snoobs',
'Meri ex', 'America', 'Tony', 'choduram', 'Kinky',
'chuttad', 'Asshole', 'Tera baap', 'Munni',
"Badnam", 'bhookha')

last = ('Condom', 'Tiktoker', 'Chutiya', 'Bhadwa',
'Bhosadiwala', 'Madarchod', 'Dickshit', 'Khalifa',
'Sins', 'Mohapatra', 'Mohanty', 'Hota', 'Ronny',
'Addams', 'Pyaare', 'Booby', 'Bahinchod', 'Chutmarike',
'Bin Superman', 'Chaiwala', 'and sons', 'Bhosad', 'sharma',
'Kingfisher', 'Tandoori', "Bakra", 'McFadden', 'Moonshine', 'Nettles',
'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Nasim',
'Pradhan', 'Iyer', 'Chhodi', 'Captain', 'stark',
'choduram', 'Ghasita', 'Laal', 'Asshole', 'Tera Baap',
'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
'Badnam', 'Munni', 'Bhosadiwale', 'chacha', 'hawasi',
'Sher')

while True:
    first_name = random.choice(first)
    last_name = random.choice(last)

    print("\n\n")
    print("{} {}".format(first_name,last_name), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
    if try_again.lower() == "n":
        break
input("\nPress Enter to exit.")