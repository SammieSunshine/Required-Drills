# Required-Drills
Drills Revisions needed to be made in order to progress to Live Project


Database and SQL Course: Page 254
Python Course: Pages 185, 207, 266(PASSED), 270, 351, 355, 360, 364
Project Management Course: Page 149

 
Database and SQL Course: Page 254
ZOO DATABASE ASSIGNMENT 5
Compose a SELECT statement that accomplishes the following:
Retrieve all names within the species_name column using the alias "Species Name:" from the species table and their corresponding nutrition_type under the alias "Nutrition Type:" from the nutrition table.

Original Feedback: 
Hint: This query will need to have a table join and it should be nutrition_type AS [Nutrition Type] not nutrition_id AS [Nutrition Type]


Python Course Drills: 
 
Assignment 185
ASSIGNMENT
For this assignment, you will need to write a script that creates a database and adds new data into that database.
REQUIREMENTS:
Your script will need to use Python 3 and the sqlite3 module.
Your database will require 2 fields: an auto-increment primary integer field and a field with the data type "string".
Your script will need to read from the supplied list of file names at the bottom of this page and determine only the files from the list which end with a “.txt” file extension.
Next, your script should add those file names from the list ending with “.txt” file extension within your database.
Finally, your script should legibly print the qualifying text files to the console.
Add comments throughout your Python explaining your code. Adding comments to your code is a good practice, and is expected in the industry. It will help you understand what your code is doing and will also make it easier when you need reference back to previous projects.
SETUP INSTRUCTIONS:
The following is the list of file names to use for this assignment:

Once you have completed this assignment, upload your code to your Github account and submit your link in the space below.

Original Feedback:
Thanks for the submission. This is very close, although it's not inserting the files into the table correctly. In order to run an SQL statement in Python, you have to use "cur" and "cur.execute". Take a look at the statement you did in the beginning, where you created a table:

cur.execute('CREATE TABLE IF NOT EXISTS table_Files(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    fname TEXT)')

Notice that it uses "cur.execute", and then inside of the parentheses and then inside the quotes, it runs an SQL statement. You're going to want to do something similar to run an INSERT statement to insert the files into the table.

Also, it would be ideal to display the contents of the table after you insert into them, so the user knows the files were inserted correctly. Again, you can do this by using a "cur.execute" to run an SQL SELECT statement.


Assignment 207 
POLYMORPHISM ASSIGNMENT
Create two classes that inherit from another class.
1. Each child should have at least two of their own attributes.
2. The parent class should have at least one method (function).
3. Both child classes should utilize polymorphism on the parent class method.
4. Add comments throughout your Python explaining your code.
Upload your code to GitHub and submit your link below.

Original Feedback:
Thanks for the submission. This is very, very close, although there's a couple of things that need to be adjusted to get it working properly.

For one, in the "if" statement in the "getcharinfo" method of "CharInfo", it's trying to compare "c_tollGold" to "self.c_tollGold". But "self.c_tollGold" doesn't exist, it should be "self.tollGold". So it should compare them like this in the "if" statement:

c_tollGold == self.tollGold

Also, "self.c_nameEntry" doesn't exist, so you could either add a variable to the "CharInfo" class named "c_nameEntry", or you could remove that part from your "if" statement.

Lastly, because you're reading user input into "c_tollGold" without converting to an int, it's saving it as a string. Which means that when it compares "c_tollGold" to "tollGold", it always says they're not equal, since it's trying to compare a string to an int. The workaround would be to make the original "tollGold" variable in the "CharInfo" class a string instead of an int. Like this:

tollGold = "5000"

Go ahead and adjust those things, and give it a few tests with different inputs into the console to make sure all paths are accounted for and work properly. If you have any questions or need help, feel free to email us.


Assignment 270
FILE TRANSFER ASSIGNMENT PART THREE
Users are now asking for a user interface to make using the script easier and more versatile.
Desired features of the UI:
Allow the user to browse and choose a specific folder that will contain the files to be checked daily.
Allow the user to browse and choose a specific folder that will receive the copied files.
Allow the user to manually initiate the 'file check' process that is performed by the script.
Add comments throughout your Python explaining your code.
You have been asked to create this UI.
Once you have completed this assignment, upload your code to Github and submit the link in the space below.
 
Assignment 351 
ESSAY
Write an essay on what you learned in the Django tutorial series and how you can apply what you learned as a developer.
 
Assignment 355
DJANGO CHALLENGE PART TWO
The next couple of steps are meant to challenge you now that we’ve set up the basics for a Django project. This may require some research from the student and should not take more than a couple hours.
5. Create a superuser within your manage.py file so you can log in as an admin.
6. Create a new app within your project called classApp.
cd Classes
django-admin startapp classApp
 
7. Create a class “djangoClasses” within your models.py file. It should have the following attributes and include a Model manager:
Title (string value)
Course Number (integer value)
Instructor Name (string value)
Duration (float value)
8. Add your model to the admin.py file and register it.
9. Create three objects from the djangoClasses class and assign their attribute values.
10. Add the classApp name to the Main Project settings.py file.
11. Make a migration and migrate it for the three objects you created.
12. Make sure you see your objects as part of the admin page. Also make sure that you can add, modify, and delete courses to the database.
13. Make sure to add comments throughout your code to help you better understand and explain what the code is doing.
After you complete this assignment, be sure to deactivate your virtual environment. To do this, navigate back to the venv folder of your project in the PyCharm terminal and simply type deactivate.
Upload your completed code to your GitHub, including the migration files and database. The database file can be found within the Classes folder that contains the manage.py file.
Submit a link to your GitHub below.

Assignment 360
DJANGO CHECKBOOK CHALLENGE PART FIVE
This is the final step of the challenge. Up until now, you’ve got your application to the point that you can create an account and add a transaction for the account. Now comes the last step of calculating balances and displaying the information. These steps will be similar to the Products Page and the Present Product templates within the Django video series. You’ll need to pull content from the database and pass it into the templates as content, then display that content. You will also need to do some backend calculations to set the current balance of the account. This step includes the following:
1. Modifying the url patterns so the Balance Sheet can be displayed using a pk (primary key).
2. Modifying the Balance Sheet views function to take a pk and find that account.
3. Modifying the index views function and template so that it displays a form which contains a drop down of account names for the user to choose from.
(Hint: Is there anything you have already created that links to an account name?)
4. Within the Balance Sheet views function, pulling all the transactions associated with the given account from the database, calculating the current balance of the account, and returning all the information as a dictionary object.
5. Modifying the Balance Sheet views function and template to use the dictionary object for displaying all of the account information and transaction information for the given account.
6. Updating the transaction views function so that upon adding a new transaction, the user is redirected to the balance sheet.
Complete these actions:
1. In your Checkbook app directory, open the urls.py file
2. Modify the balance url patterns path so the Balance Sheet can be displayed using a pk. This will account for passing a primary key to our balance sheet, which will be related to each account:
3. We then need to modify the Balance Sheet views function to take a pk and find that account. To accomplish this, you first need to update the import statements within views.py
4. Open views.py and update/add the following import statements:

5. In the views.py file update the balance function with the following code:

The index functions and templates need to be modified so that it displays a form which contains a drop down of account names for the user to choose from. On the AddTransaction page you’ll notice that there is a drop down of account names. This is because the Transaction Form has an account field which is a foreign key to the account it applies to. We’re going to use this to generate the drop down on index.html.
6. Update the home function in the views.py to pass in the Transaction form like so:

7. From templates open index.html and add a form under the heading ‘Manage your existing account!’ with the following code and then save the file:

8. Return to views.py and update the home function with the code below then save the file:

9. Create a working Balance Sheet. To do so, in the balance function in views.py, add this code under account:

10. Then in BalanceSheet.html delete all of the table rows except for the first 2. Update the second row with the following code:

11. In the same BalanaceSheet.html file at the top of the page update the following code with the below:

12. Back in the views.py file update the transaction views function so that upon adding a new transaction, the user is redirected to the balance sheet. Remove the following line of code under form.save():

And replace it with:

CONGRATULATIONS! You have built a functional Django app!
13. Upload your code to GitHub and submit it here:
 
Assignment 364
FINAL ESSAY
1. What did you learn from this course?
2. How will you use Python as a developer?
3. How will you use Django?
4. What do you intend to do with the skills gained on this course?
Submit your essay below:
 
 
 
Project Management Course:
Assignment Page 149
TBD once approved to view course.



 

