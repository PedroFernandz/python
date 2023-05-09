#!/usr/bin/env python3

import subprocess
import sys
import getpass
import datetime

# Ask the user for the MySQL user
mysql_user = input("Please enter your MySQL user: ")

# Ask the user for the MySQL password
mysql_password = getpass.getpass("Please enter your MySQL password: ")

# Check if the MySQL user is valid
check_credentials_command = f"mysql --user={mysql_user} --password='{mysql_password}' --execute='SELECT 1;'"
result = subprocess.run(check_credentials_command, shell=True, stderr=subprocess.DEVNULL)

if result.returncode != 0:
    print("Invalid MySQL user or password. Please check your credentials. Exiting.")
    sys.exit(1)

# Get the list of databases
command = f"mysql --user={mysql_user} --password='{mysql_password}' --execute='SHOW DATABASES;' 2>/dev/null | grep -Ev 'Database|information_schema|performance_schema'"
databases_output = subprocess.getoutput(command)
databases = databases_output.split('\n')

# Verify if the connection was successful
if not databases:
    print("Error connecting to MySQL. Please check your username and password. Exiting.")
    sys.exit(1)

# Display the databases with an associated number
print("List of databases:")
db_map = {}
for i, db in enumerate(databases, start=1):
    print(f"{i} - {db}")
    db_map[i] = db

# Ask the user to select a database
selected_db_number = int(input("Please select the database you want to backup (enter the associated number): "))

# Verify if the selected number is valid
if selected_db_number not in db_map:
    print("Invalid number. Exiting.")
    sys.exit(1)

# Perform the backup of the selected database
selected_db = db_map[selected_db_number]
backup_file = f"{selected_db}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
mysqldump_command = f"mysqldump --user={mysql_user} --password='{mysql_password}' '{selected_db}' > '{backup_file}'"
result = subprocess.run(mysqldump_command, shell=True)

# Check if the backup was successful
if result.returncode == 0:
    print(f"Backup of database '{selected_db}' was successful. File: {backup_file}")
else:
    print(f"Error while backing up database '{selected_db}'.")
