def create_table(database_name, table_name, username, password):
    """create_table Creates a database and table if not already existing

    The function creates a table to keep track of player scores for the game.


    Parameters
    ----------
    database_name : str
        The name of the database to create
    table_name : str
        The name of the table to create
    username : str
        Username to connect to database
    password : str
        Password to connect to database
    """

    from mysql import connector

    try:
        # Connect to database using provided login credentials
        connection = connector.connect(
            host="localhost", username=username, password=password
        )
        cursor = connection.cursor()
        # Query available databases
        cursor.execute("SHOW DATABASES")
        # Convert multiple tuple rows into single list of databases
        databases = [row[0] for row in cursor.fetchall()]
        # Check if required database is present
        # If not create the database
        if database_name not in databases:
            cursor.execute(f"CREATE DATABASE {database_name}")
        # Open the required database
        cursor.execute(f"USE {database_name}")
        # Query available tables
        cursor.execute("SHOW TABLES")
        # Convert multiple tuples into single list of tables
        tables = [row[0] for row in cursor.fetchall()]
        # Check if required table is present
        # If not create the table
        if table_name not in tables:
            cursor.execute(
                f"CREATE TABLE {table_name} (id int NOT NULL \
AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), score INT)"
            )
    except Exception as e:
        print(e)


def insertData(username, password, table_name, data, database_name):
    # Importing mysql connector
    from mysql import connector

    try:
        # Connecting databases of players
        connection = connector.connect(
            host="localhost",
            username=username,
            password=password,
            database=database_name,
        )
        # Establishing a cursor for the above connection
        cursor = connection.cursor()
        # Inserting data into the table using the above established cursor
        cursor.execute(
            f"insert into {table_name} (name, score) values('{data[0]}','{data[1]}')"
        )
        connection.commit()
        connection.close()
    except Exception as e:
        print(e)


def top_five_scores(username, password, table_name, database_name):
    # Importing sql connector
    from mysql import connector

    try:
        # Connecting to the database
        connection = connector.connect(
            host="localhost",
            username=username,
            password=password,
            database=database_name,
        )
        # Creating cursor object
        cursor = connection.cursor()
        # Query for top 5 scores
        cursor.execute(
            f"select name,score from {table_name} order by score desc limit 5"
        )
        return cursor.fetchall()
    except Exception as e:
        print(e)


def delete_scores(username, password, table_name, database_name):
    # Importing sql connector
    from mysql import connector

    try:
        # Connecting to the database
        connection = connector.connect(
            host="localhost",
            username=username,
            password=password,
            database=database_name,
        )
        # Creating cursor object
        cursor = connection.cursor()
        # Query to delete all scores
        cursor.execute(f"drop table {table_name}")
    except Exception as e:
        print(e)


def get_score(username, password, table_name, database_name):
    # Importing sql connector
    from mysql import connector

    try:
        # Connecting to the database
        connection = connector.connect(
            host="localhost",
            username=username,
            password=password,
            database=database_name,
        )
        # Creating cursor object
        cursor = connection.cursor()
        # Getting Score from table using username
        score = cursor.execute(
            f"SELECT score FROM {table_name} WHERE name={username}"
        )
        return score
    except Exception as e:
        print(e)


def greater_score_count(username, password, table_name, database_name, score):
    # Importing sql connector
    from mysql import connector

    try:
        # Connecting to the database
        connection = connector.connect(
            host="localhost",
            username=username,
            password=password,
            database=database_name,
        )
        # Creating cursor object
        cursor = connection.cursor()
        # Getting number of score greater than given score
        scoregreatercount = cursor.execute(
            f"SELECT COUNT(score) FROM {table_name} WHERE score>{score}"
        )
        return scoregreatercount
    except Exception as e:
        print(e)
