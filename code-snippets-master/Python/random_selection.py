# Got this from Will: it's Toni's first program and they use it to select restaurants when they can't think of one. 
#!/usr/bin/env python
import random
restaurant_list = ['Dominos Pizza', 'Mysore', 'Restaurant Thailande', 'Lemeac', 'Chez Leveque', 'Sushi', 'Italian', 'Poutineville']
restaurant_item = random.choice(restaurant_list)
print ("Randomly selected item from list is " + restaurant_item)
