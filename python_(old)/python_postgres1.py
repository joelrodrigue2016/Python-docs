import psycopg2

conn = psycopg2.connect(database="postgres", user = "postgres", password = "Kingjames1611", host = "localhost", port = "5432")

print ("Opened database successfully")





###create table
cur = conn.cursor()
cur.execute('''CREATE TABLE courses(course_id serial primary key,
                course_name VARCHAR(255) NOT NULL,
                description VARCHAR(500),
                published_date date);''')


print ("Table created successfully")



cur = conn.cursor()

course_name =input("Course name: ")
description = input("Description: ")
published_date = input("Published date: ")

cur.execute(f"""INSERT INTO courses(course_name, description, published_date) \
      VALUES ('{course_name}','{description}','{published_date}')""")   ##2020-07-13

conn.commit()
print ("Records created successfully")



conn.close()
print("Connection closed, see you next time!")