def main():

    # Created a complex data structure
    about_me = {'full_name' : 'Sreehari Jiji',
                'student_id': '10316483',
                'pizza_toppings': ['BACON','PEPPORONI','SAUSAGE'] ,
                'movies': [{'title': 'rocky', 'genre': 'thriller'} ,
                {'title': 'rocky 2', 'genre': 'thriller'}]
                }

    # Step 3 - Added another movie to the data structure
    about_me['movies'].append({'title': 'shrek', 'genre': 'comedy'})
    
    # printing student name and id
    print_student_name_and_id(about_me)

    # printing and adding pizza toppings  
    add_pizza_toppings(about_me, ['Pineapple', 'Hot peppers'])
    print_pizza_toppings(about_me)

    
# Step 4 - Created Function that prints student name and ID	
def print_student_name_and_id (data_struct):

    full_name = data_struct['full_name']

    first_name = full_name.split(' ')[0]

    student_id = data_struct['student_id']

    print(f"My name is {full_name}, but you can call me Lord {first_name}.")

    print(f"My student ID is {student_id}.")

    return

    
    
# Step 5 - Created Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):

    about_me['pizza_toppings'].extend(toppings)

    about_me['pizza_toppings'] = sorted(map(str.lower, about_me['pizza_toppings']))

    return

# TODO: Step 6 - Created Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):

    print("My favourite pizza toppings are:")

    for topping in about_me['pizza_toppings']: print(f"- {topping}")

    return



# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()