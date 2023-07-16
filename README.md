# ImpledgeTest Kloudship Automation 

# Selenium Automation Script for Adding and Deleting Packages
This repository contains two Python scripts, `AddPackage.py` and `DeletePackage.py`, that automate the process of adding and deleting packages on the Kloudship website using Selenium.

## Prerequisites
To run the scripts, you need to have the following installed:
- Python 3
- webdriver library for Python
- ChromeDriver executable
- Python IDE (eg. Pycharm)

## Setup and Execution
1. Clone or download this repository to your local machine.
2. Install the required dependencies
3. Set the correct path to the ChromeDriver executable in both `AddPackage.py` and `DeletePackage.py` scripts. Update the `webdriver_service` variable with the correct path.
4. Locate the email and password input fields in both scripts and replace the existing placeholders with your login credentials for the Kloudship website.
5. Save the changes in the scripts.
6. Open a terminal or pycharm and navigate to the directory where the script files are located.

AddPackage.py - This script will automate the process of logging in, adding a new package, and logging out.
After the execution of the `AddPackage.py` script is complete

DeletePackage.py - This script will automate the process of logging in, deleting the previously added package(if the package is not exist then it throws an exception and take the screenshot), and logging out.
Once the execution of the `DeletePackage.py` script is complete, you can check the Kloudship website to verify that the package has been deleted successfully.



## Design Decisions and Approach
The scripts use the Selenium library, which provides a convenient API for automating web browsers, to interact with the Kloudship website. Here's an overview of the design decisions and approach taken in the scripts:

1. Import necessary modules and libraries: The scripts begin by importing the required modules, including Selenium, and setting up the ChromeDriver service.
2. Login: The scripts navigate to the Kloudship website and enter the login credentials (email and password) into the appropriate input fields. They then submit the login form to authenticate the user.
3. Add Package: The `AddPackage.py` script clicks on the "Packages" tab, locates the "+" button to add a new package, and enters the package details (name, length, width, and height) into the input fields. After saving the package, it logs out.
4. Delete Package: The `DeletePackage.py` script follows a similar approach as the "Add Package" script but instead of adding a package, it clicks on the delete icon for the previously added package(If it does not found created package it throws an exception and take screenshot). It then confirms the deletion and logs out.
5. Quit: After completing the actions, the scripts close the browser window and terminate the ChromeDriver service.

This approach provides a simple and effective way to automate the process of adding and deleting packages on the Kloudship website using Selenium webdriver.
