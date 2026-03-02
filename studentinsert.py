import psycopg2

connection = None
try:
    connection = psycopg2.connect(
        user="dbadmin",
        password="bhagavathi1",
        host="my-test-postgres-db.ch4kq2860gzt.eu-north-1.rds.amazonaws.com",
        port="5432",
        database="test"
    )
    cursor = connection.cursor()

    # Define student-specific SQL
    insert_query = """INSERT INTO student (studentId, studentname, age, grade) 
                      VALUES (%d, %s, %d, %d)"""
    record_to_insert = (1, 'Bob Johnson', 18, 3.8)

    cursor.execute(insert_query, record_to_insert)
    connection.commit()
    
    print("Student record inserted successfully")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()