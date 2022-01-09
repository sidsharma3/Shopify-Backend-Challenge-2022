## Shopify Backend Challenge 2022

Hello! In this repository is my submission to the Shopify Backend Intern Challenge for Summer 2022.

This repository contains the code for a Flask web application which allows users to create, edit and delete inventory items and also view all the inventory items in a list as well! Additionally this application also features the ability to download all of the product data as a csv file.

It is important to note that in order to start this application Python 3 must be installed. This can be done by following the steps in this link: https://www.python.org/downloads/

## Start the Application

To start the application first clone the repository to a working directory using git. Once the project is cloned, navigate to the directory which includes the requirements.txt file.


After this open a terminal or command prompt window in your current directory and run the command below.

```
pip install -r requirements.txt
```

Once the previous command is completed, in the same terminal or command prompt window run the command below. 

```
python main.py
```
This command will launch the Flask web application on localhost:5000, the homepage will look like the image below.

<img width="1204" alt="HomepageNoItems" src="https://user-images.githubusercontent.com/46334482/148676830-9f93a7e4-8905-4c2e-b33b-b7c8aed98e8d.png">

This is the homepage with inventory items:

<img width="1272" alt="HomepageWithItems" src="https://user-images.githubusercontent.com/46334482/148676856-281d9f48-9465-4761-9dcb-ae0cc18ba2f2.png">

This is the Add/Edit Inventory Items page:

<img width="1193" alt="AddAndEditPage" src="https://user-images.githubusercontent.com/46334482/148676870-6e3e9989-33ed-4e99-9b6f-de125d07b45b.png">


Please note that if Python 3 and Python 2 are both installed in your computer you may need to run the following commands instead:

```
pip3 install -r requirements.txt
```

```
python3 main.py
```
