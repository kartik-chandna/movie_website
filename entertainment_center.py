# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media

import fresh_tomatoes

# create object of Movie class 
toy_story = media.Movie("Toy Story" , "Toys comes to life" , "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg" , "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar" , "A marine on an alien planet" , "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg" ,"https://www.youtube.com/watch?v=cRdxXPV9GNQ")

escape_plan = media.Movie("Escape Plane" , "Person who escapes prison" ,"https://upload.wikimedia.org/wikipedia/en/5/5d/Escapeplanfilmposter.jpg" ,"https://www.youtube.com/watch?v=Gmt89TXjYBI")

internship = media.Movie("The Internship" , "2 boys doing internship at google" , "https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg" , "https://www.youtube.com/watch?v=cdnoqCViqUo")

# list of objects of Movie class is stored in variable - movies
movies = [toy_story, avatar, escape_plan , internship]

# shows the HTML page
fresh_tomatoes.open_movies_page(movies) 


