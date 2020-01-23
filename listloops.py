#for i in range(10):
    #print(i)

#import random

#for i in range(6):
    #print(random.randint(1,50))

#for i in range(9,-1,-1):
    #print(i)

movie_list = [
    'Man On Fire',
    'flight',
    'deja vu',
    'unstoppable'
]

movie_list.insert(3,'shooter')
movie_list.append('scream')

#for film in movie_list:
    #print(film)

def film_search ():
    if movie_list[3] == "shooter":
        print("this is correct")
    else:
        print("It is not")
film_search()