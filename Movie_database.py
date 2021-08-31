import sqlite3

#Connect to database
conn = sqlite3.connect("movies.db")

#Create a cursor
c = conn.cursor()

#Create a Table 
c.execute(""" CREATE TABLE movies(
        movie_name text,
        actor_name text,
        actress_name text,
        year_of_release text,
        director_name text
    )""")

#Insert values into table
fav_movies = [('Shershaah', 'Sidharth Malhotra', 'Kiara Advani', '2021', 'Vishnuvardhan'),
               ('Passengers', 'Chris Pratt', 'Jennifer Lawrence', '2016', 'Morten Tyldum'),
               ('3 Idiots', 'Aamir Khan', 'Kareena Kapoor', '2009', 'Rajkumar Hirani'),
               ('Devdas', 'Shah Rukh Khan', 'Aishwarya Rai', '2002', 'Sanjay Leela Bhansali'),
               ('Ek Villain', 'Sidharth Malhotra', 'Shraddha Kapoor', '2014', 'Mohit Suri'),]

c.executemany("INSERT INTO movies VALUES(?,?,?,?,?)", fav_movies)

#Query the database
#Query all rows from the Movies table
print("----------First Query----------")
c.execute("SELECT * FROM movies")
results = c.fetchall()
for result in results:
    print(result[0] + "," + result[1] + "," + result[2] + "," + result[3] + "," + result[4])


#Query movies based on the actor name
print("----------Second Query----------")
c.execute("SELECT * FROM movies WHERE actor_name = 'Sidharth Malhotra'")
results = c.fetchall()
for result in results:
    print(result[0] + "," + result[1] + "," + result[2] + "," + result[3] + "," + result[4])


#Commit the command
conn.commit()

#Close the connection
conn.close()