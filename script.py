def main():

    # Created a complex data structure
    about_me = {'full_name' : 'Sreehari Jiji',
                'student_id': '10316483',
                'pizza_toppings': ['BACON','PEPPORONI','SAUSAGE'] ,
                'movies': [{'title': 'the perks of being a wallflower', 'genre': 'romance'} ,
                {'title': 'django unchained', 'genre': 'action'}]
                }

    # Step 3 - Added another movie to the data structure
    about_me['movies'].append({'title': 'shrek 2', 'genre': 'comedy'})
    
    # printing student name and id
    print_student_name_and_id(about_me)

    # CAPITAL pizza toppings
    CAPITAL_print_pizza_toppings(about_me)

    # printing added pizza toppings  
    add_pizza_toppings(about_me, ['Pineapple', 'Hot peppers'])
    print_pizza_toppings(about_me)

    # printing movie titles and genres
    print_movie_genres(about_me)
    print_movie_titles(about_me['movies'])

    
# Step 4 - Created Function that prints student name and ID	
def print_student_name_and_id (about_me):

    full_name = about_me['full_name']

    first_name = full_name.split(' ')[0]

    student_id = about_me['student_id']

    print(f"My name is {full_name}, but you can call me Lord {first_name}.")

    print(f"My student ID is {student_id}.\n")

    return

# CAPITAL pizza toppings
def CAPITAL_print_pizza_toppings(about_me):

    print("My favourite pizza toppings are:")

    for topping in about_me['pizza_toppings']: print(f"- {topping}")
    print()

    return

    
    
# Step 5 - Created Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):

    about_me['pizza_toppings'].extend(toppings)

    about_me['pizza_toppings'] = sorted(map(str.lower, about_me['pizza_toppings']))

    return


#Step 6 - Created Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):

    print("My favourite pizza toppings are:")

    for topping in about_me['pizza_toppings']: 
        print(f"- {topping}")
    print()
    return



#Step 7 - Created Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):

    genres = [movies['genre'] for movies in about_me['movies']]

    commas = ', '.join(genres)

    commas = commas.rsplit(', ', 1)

    bonus = ' and '.join(commas)

    print(f"I like to watch {bonus} movies.\n")

    return 


# Step 8 - Created Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):

    titles = [movie['title'].title() for movie in movie_list]

    commas = ', '.join(titles)

    commas = commas.rsplit(', ', 1)

    bonus = ' and '.join(commas)

    print(f"Some of my favourite movies are {bonus}!\n")

    return

    
if __name__ == '__main__':
    main()