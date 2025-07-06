# My Zootopia
## About 

This is a Python project in which a list is created on an HTML page using freely available animal data via an API from `https://api-ninjas.com/api/animals`. The user can select which animals should be listed on the page. By entering the name of the animals and the skin type.

## Installation

To install this project, clone the repository and install the dependencies in requirements.txt using `pip install` or `pip3 install`.
Additional you need to sing in at `https://api-ninjas.com/` for a free API key.
Also you have to create a file for enviroment variables `.env` to save there your free API key.

## Usage

To use this project, run the following command - `python animals_web_generator.py`. 
At the moment you can search for animals via user input which are listed on the `animals.html` page with some properties. If they are available in the animal database of `api-ninjas.com`. If there is an incorrect entry or the animal does not exist in the database, an error message is displayed on the HTML page.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:
-   create a new branch to experiment with the code and possibly also open an issue in case of additional content or wishes
-   if you find something interesting and want to share it, create a pull request
-   in case of bugs or problems, open an issue and describe the bug/problem and mark it with labels
