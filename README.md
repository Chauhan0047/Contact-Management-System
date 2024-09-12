
# Contact Management System

## Overview

This is a simple contact management system implemented in Python. It allows users to add, update, delete, search, view, and count contacts. The contacts are stored in a JSON file named `contacts.json` to persist data across program runs.

## Features

- **Add Contact**: Add a new contact with a name, email, and phone number.
- **Update Contact**: Update the email and/or phone number of an existing contact.
- **Delete Contact**: Remove a contact from the system.
- **Search Contact**: Search for a contact by name and display their details.
- **View All Contacts**: View a list of all contacts in the system.
- **Count Contacts**: Display the number of contacts currently stored.

## File Structure

- `contacts.json`: JSON file that stores contact information.
- `app.py`: Python script containing the contact management system code.

## Requirements

- Python 3.x
- No additional libraries are required other than Python's standard libraries (`json`, `os`).

## Usage

1. **Running the Program**

   To start the contact management system, run the following command in your terminal:
   python app.py

   
Available Options:

Once the program is running, you will be presented with a menu of options:

Add contact: Add a new contact to the system.
Update contact: Update the details of an existing contact.
Delete contact: Remove a contact from the system.
Search contact: Find and display the details of a contact by name.
View all contacts: List all contacts in the system.
Count contacts: Show the total number of contacts.
Exit: Exit the program.

File Persistence:
Loading Contacts: Contacts are loaded from contacts.json when the program starts.
Saving Contacts: Contacts are saved to contacts.json after each modification (add, update, delete).
Troubleshooting
File Not Found Error: Ensure that contacts.json is in the same directory as app.py. The file will be created automatically if it does not exist.
Invalid Input: Ensure that you enter valid choices (1-7) and follow prompts for entering contact details.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
[Himanshu ]

Feel free to modify the README as needed for your specific use case or to include additional details about the project.

### Explanation of the README Content

1. **Overview**: Provides a brief description of what the application does.
2. **Features**: Lists the functionalities of the application.
3. **File Structure**: Explains the files used in the project.
4. **Requirements**: Specifies the requirements for running the code.
5. **Usage**: Includes instructions on how to run the program and interact with it.
6. **Example Usage**: Provides sample inputs and interactions.
7. **File Persistence**: Describes how the program handles data storage.
8. **Troubleshooting**: Offers solutions to common issues.
9. **License**: Mentions the licensing information.
10. **Author**: Provides author details.

This README file should help users understand how to use the contact management system
