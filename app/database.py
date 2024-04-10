import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("table created")
    except Error as e:
        print(e)

# ================================ PELIGROSO ===========================
def drop_table(table_name, database_file):
    conn = create_connection(database_file)
    cursor = conn.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    conn.commit()
    print(f"Table {table_name} is dead")
    conn.close()

def drop_all_tables(database_file):
    conn = create_connection(database_file)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    for table in tables:
        if table[0] != 'sqlite_sequence':
            cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")

    conn.commit()
    print(f"All Tables are dead")
    conn.close()

def create_tables(database_file):
    
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        user_id TEXT PRIMARY KEY,
                                        email TEXT NOT NULL UNIQUE,
                                        password TEXT NOT NULL,
                                        created_at TIMESTAMP NOT NULL,
                                        last_login TIMESTAMP
                                    ); """

    sql_create_accounts_table = """CREATE TABLE IF NOT EXISTS accounts (
                                      account_id TEXT PRIMARY KEY,
                                      user_id TEXT NOT NULL,
                                      account_type TEXT NOT NULL,
                                      account_name TEXT NOT NULL,
                                      balance REAL NOT NULL,
                                      created_at TIMESTAMP NOT NULL,
                                      last_updated TIMESTAMP,
                                      FOREIGN KEY (user_id) REFERENCES users (user_id)
                                   );"""

    sql_create_transactions_table = """CREATE TABLE IF NOT EXISTS transactions (
                                          transaction_id TEXT PRIMARY KEY,
                                          account_id TEXT NOT NULL,
                                          user_id TEXT NOT NULL,
                                          transaction_type TEXT NOT NULL,
                                          amount REAL NOT NULL,
                                          category_id TEXT NOT NULL,
                                          transaction_date DATE NOT NULL,
                                          description TEXT,
                                          created_at TIMESTAMP NOT NULL,
                                          FOREIGN KEY (account_id) REFERENCES accounts (account_id),
                                          FOREIGN KEY (user_id) REFERENCES users (user_id),
                                          FOREIGN KEY (category_id) REFERENCES categories (category_id)
                                       );"""

    sql_create_categories_table = """CREATE TABLE IF NOT EXISTS categories (
                                        category_id TEXT PRIMARY KEY,
                                        category_name TEXT NOT NULL,
                                        category_type TEXT NOT NULL,
                                        global BOOLEAN NOT NULL,
                                        user_id TEXT,
                                        FOREIGN KEY (user_id) REFERENCES users (user_id)
                                     );"""

    sql_create_budgets_table = """CREATE TABLE IF NOT EXISTS budgets (
                                     budget_id TEXT PRIMARY KEY,
                                     user_id TEXT NOT NULL,
                                     category_id TEXT NOT NULL,
                                     amount REAL NOT NULL,
                                     start_date DATE NOT NULL,
                                     end_date DATE NOT NULL,
                                     FOREIGN KEY (user_id) REFERENCES users (user_id),
                                     FOREIGN KEY (category_id) REFERENCES categories (category_id)
                                  );"""

    sql_create_savings_goals_table = """CREATE TABLE IF NOT EXISTS savings_goals (
                                           goal_id TEXT PRIMARY KEY,
                                           user_id TEXT NOT NULL,
                                           goal_name TEXT NOT NULL,
                                           target_amount REAL NOT NULL,
                                           current_amount REAL NOT NULL DEFAULT 0,
                                           target_date DATE,
                                           created_at TIMESTAMP NOT NULL,
                                           FOREIGN KEY (user_id) REFERENCES users (user_id)
                                        );"""


    # create a database connection
    conn = create_connection(database_file)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_accounts_table)
        create_table(conn, sql_create_transactions_table)
        create_table(conn, sql_create_categories_table)
        create_table(conn, sql_create_budgets_table)
        create_table(conn, sql_create_savings_goals_table)
        conn.commit()
        conn.close()
    else:
        print("Error! cannot create the database connection.")

def main():
    database_file = "data/personal_finance_data.db"
    drop_all_tables(database_file)
    create_tables(database_file)

if __name__ == '__main__':
    main()
