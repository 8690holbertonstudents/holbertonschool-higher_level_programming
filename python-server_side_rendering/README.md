<h3>Python - Server-Side Rendering</h3>

<h5>0. Creating a Simple Templating Program</h5>

In this task, you will create a Python function that generates personalized invitation files from a template with placeholders and a list of objects. Each output file should be named sequentially, starting from 1. You will also implement specific error handling for various edge cases.

Objective
Understand how to use string templating in Python.
Implement file operations for reading templates and writing output files.
Handle various edge cases and errors gracefully.
Instructions
Create the Template:

Use the provided template with placeholders for name, event_title, event_date, and event_location.
Define the Data:

Use the provided list of objects as your data source.
Write the Templating Function:

Define a function named generate_invitations that takes two parameters: template and attendees.
Check Input Types:

Verify that template is a string and attendees is a list of dictionaries.
If template is not a string or attendees is not a list of dictionaries, log an error message and terminate the function.
Handle Empty Inputs:

Check if the template is empty and log an error message if it is.
Check if the attendees list is empty and log an error message if it is.
Process Each Attendee:

Iterate over the list of attendees and replace the placeholders in the template with the corresponding values from each attendee’s dictionary.
If a value is missing, replace it with “N/A”.
Generate Output Files:

Write the processed template to output files named output_X.txt, where X is the index of the attendee starting from 1.
Specific Error Handling Behaviors:
Empty Template: If the template is empty, log an error message, “Template is empty, no output files generated.” and terminate without creating any files.
Empty List of Objects: If the list of objects is empty, log a message, “No data provided, no output files generated.” and terminate without creating any files.
Missing Data in Object: If an object is missing data for any of the placeholders, replace the missing data with the text “N/A” in the output file. For example, if event_date is missing, it should appear as “event_date: N/A” in the output.
Invalid Input Types: If the input template is not a string or the list is not a list of dictionaries, log an error message indicating the type of invalid input and terminate the function.

<h5>1. Creating a Basic HTML Template in Flask</h5>

In this task, you will build a basic Flask application that serves a web page using a Jinja template. You will create a simple HTML template that includes various elements like headings, paragraphs, and lists, and learn how to render it as a web page using Flask. Additionally, you will learn to create reusable templates for headers and footers to promote code reusability and consistency across multiple pages.

Objective
Set up a Flask environment and create a basic Flask application.
Design HTML templates using Jinja for dynamic content rendering.
Implement reusable components in templates to maintain consistent layout across pages.
Instructions
Set Up Your Flask Environment:

Ensure Python is installed on your system.
Install Flask using pip: sh pip install Flask
Create a Basic Flask Application:

In your project directory, create a Python file named task_01_jinja.py.
Write a basic Flask application with a route that renders an HTML template.


<h5>2. Creating a Dynamic Template with Loops and Conditions in Flask</h5>

In this task, you will enhance your Flask application by integrating dynamic content into your HTML templates using Jinja’s loop and conditional constructs. You will read a list of items from a JSON file and display them dynamically on a web page.

Objective
Use Jinja’s loop and conditional constructs to dynamically render content in HTML templates.
Read and parse JSON data in Python.
Integrate dynamic content into your Flask application.
Instructions
Prepare Your Flask Application:

Continue using the Flask application you created in the previous exercises.
Ensure you have a basic understanding of Jinja’s templating syntax.
Create a Dynamic Template:

In your templates folder, create a new HTML template named items.html with “Items List” for the title.
This template should include a loop to iterate over a list of items and display each item.
Items must be displayed as an unordered list.
Add a conditional statement to display a message “No items found” if the list is empty.
Define the Data for the Template:

In your project directory, create a file named items.json.
Populate items.json with a list of items. Example: json { "items": ["Python Book", "Flask Mug", "Jinja Sticker"] }
Experiment with different lists, including an empty list, to see how your template responds.
Add a Route in Flask:

Create a new route /items in your Flask application to render the items.html template with the list of items.
Use Python’s json module to read the data from items.json.
Pass the list of items to the template for rendering.


<h5>3. Displaying Data from JSON or CSV Files in Flask</h5>

In this task, you will build a feature in your Flask application to read and display product data from two different data formats: JSON and CSV. You will create a single HTML template that can display data from either file type, depending on a query parameter provided in the URL. You will add functionality to your Flask application to filter product data based on an optional id query parameter. Additionally, you will handle edge cases such as invalid source parameter values or when the specified id is not found in the data.

Objective
Read and parse data from JSON and CSV files.
Use query parameters in Flask to determine data sources and filter criteria.
Implement error handling for invalid inputs and missing data.
Render dynamic data in HTML templates using Jinja.
Instructions
Prepare Data Files:

Create a JSON file (products.json) containing a list of products, each with an id, name, category, and price. Example JSON content: json [ {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99}, {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99} ]
Create a CSV file (products.csv) with similar data, using columns for id, name, category, and price. Example CSV content: id,name,category,price 1,Laptop,Electronics,799.99 2,Coffee Mug,Home Goods,15.99
Create a Dynamic Template:

In your templates folder, create an HTML template product_display.html for displaying the product data.
Design the template to display the data in a table format with headings for Name, Category, and Price.
Modify Flask Application:

In task_03_files.py, create a route in your Flask application that accepts a source query parameter (values json or csv) and an optional id.
Depending on the source parameter, read and parse data from the corresponding file.
Implement logic to filter data by the specified id if provided. If id is not provided, display all products.
Pass the parsed data to the product_display.html template for rendering.
Implement File Reading Logic:

Write functions to read and parse data from both JSON and CSV files.
Ensure the data is converted into a format that can be easily displayed by the template.
Handle Edge Cases:

If source is neither json nor csv, return a “Wrong source” error message in the template.
If id is provided but not found in the file, display a “Product not found” error message in the template.
Modify the product_display.html template to handle and display error messages if necessary.



<h5>4. Extending Dynamic Data Display to Include SQLite in Flask</h5>

Building on the previous exercise, you will now add the functionality to fetch and display data from a SQLite database in your Flask application. The application should allow users to choose between JSON, CSV, and SQL (SQLite database) as data sources using the source query parameter.

Objective
Set up and interact with a SQLite database in a Flask application.
Extend existing functionality to handle multiple data sources.
Implement error handling for database-related issues.
Instructions
Database Setup:
SQLite Database File:
Name your SQLite database file products.db.
Table Structure:

Create a Products table with columns: id (primary key), name, price, category.
Example Data:

Insert the following data into the Products table:
id: 1, name: “Laptop”, price: 799.99, category: “Electronics”
id: 2, name: “Coffee Mug”, price: 15.99, category: “Home Goods”
