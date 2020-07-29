'''
    Project name: Week 5 - SQL
    File name: pythonRepos.py
    Author: Patrick D
    DTG created: 28 2104 Z-4 July 2020
    DTG last modification: 28 2105 Z-4 July 2020
    Python Version: 3.7.4
    Description: Creating and editing databases with SQL
'''

# Importing requests
import requests

# Importing pymysql
import pymysql

# Declare API call variables
python_apicall = "https://api.github.com/search/repositories?q=language:python"
swift_apicall = "https://api.github.com/search/repositories?q=language:swift"
java_apicall = "https://api.github.com/search/repositories?q=language:java"

# Getting the response of each apicall
python_response = requests.get(python_apicall)
swift_response = requests.get(swift_apicall)
java_response = requests.get(java_apicall)

# Sets a variable to the  return of the JSON object of it's result
python_responseDict = python_response.json()
swift_responseDict = swift_response.json()
java_responseDict = java_response.json()

# Sets a variable to the total count of the repos
python_repos = python_responseDict['total_count']
swift_repos = swift_responseDict['total_count']
java_repos = java_responseDict['total_count']

# Print repos total count to verify successful api calls
print(f"Total Python repos: {python_repos}\nTotal Swift repos: {swift_repos}\nTotal Java repos: {java_repos}")

# Connect to local database c4v
connection = pymysql.connect('localhost', 'root', '', 'c4v')

# Create cursor object
cursor = connection.cursor()

# sql insert statement into assignment3 table
sql = "INSERT INTO assignment3 (PythonRepos, SwiftRepos, JavaRepos) VALUES (%s, %s, %s)"

# Execute sql statement passing the repos variables as arguements
cursor.execute(sql, (python_repos, swift_repos, java_repos))

# Commit insert change to database
connection.commit()

# Verify insertion
sql = "SELECT * FROM assignment3"

# Execute SELECT
cursor.execute(sql)

# Fetch the results followed by printing them
result = cursor.fetchall()
for row in result:
    print(row)

# Close connection
connection.close()