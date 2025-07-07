""" animals_web_generator.py
This script generates an HTML file displaying information about animals.
It reads data from a JSON file, allows the user to filter animals by skin type,
and creates an HTML file with the selected information.
"""


import json
from data_fetcher import fetch_data


def load_data(file_path):
    """ Loads a JSON file
        :param file_path: Path to the JSON file
        :return: loaded JSON file
    """
    with open(file_path, "r", encoding='utf-8') as handle:
        return json.load(handle)


def select_animal_info(data):
    """ Selects the information {Name, Diet, first location, Type}
    if one of these fields doesn't exist, then it doesn't exist as well in the dictionary
        :param data: loaded data
        :return:  list of dictionaries with selected information
    """
    animals_list = []
    for animal in data:
        info_dict = {}
        # select Name of the animals
        if 'name' in animal:
            info_dict['Name'] = animal['name']
        # select Diet of the animals
        if 'diet' in animal['characteristics']:
            info_dict['Diet'] = animal['characteristics']['diet']
        # select First Location of the animals
        if len(animal['locations']) > 0:
            info_dict['First Location'] = animal['locations'][0]
        # select Type of the animals
        if 'type' in animal['characteristics']:
            info_dict['Type'] = animal['characteristics']['type']
        # selecte Skin_Type of the animals
        if 'skin_type' in animal['characteristics']:
            info_dict['Skin_Type'] = animal['characteristics']['skin_type']
        animals_list.append(info_dict)  
    return animals_list


def user_input_skin_type(list_of_dict):
    """ Create a new list of dictionaries with only the animals 
    that have a skin_type previously entered by the user
    first a list of all skin_types will be created to show this in the user input 
    after the user entered a skin_type, the function will check of an correct entry
    in case of an incorrect entry, the user will be informed and 
    the entire list of all animals will be returned
    in case of an correct entry, the animals with the right skin_type will be added to the new list
        :param list_of_dict: list of dictionaries with selected information
        :return: list of dictionaries with only the animals that have the entered skin_type
    """
    new_list_of_dict = []
    list_skin_types = []
    for animal in list_of_dict:
        if 'Skin_Type' in animal:
            # list of all skin_types
            if list_skin_types.count(animal['Skin_Type']) < 1:
                list_skin_types.append(animal['Skin_Type'])

    user_skin_type = input(
        f'Enter a Skin_Type from these List {list_skin_types}: ')
    # case of an incorrect entry
    if user_skin_type not in list_skin_types:
        print(
            f'{user_skin_type} was not in the presented list, please enter a Skin_Type again: ')
        new_list_of_dict = list_of_dict
    # case of an correct entry
    else:
        for animals in list_of_dict:
            if 'Skin_Type' in animals:
                if animals['Skin_Type'] == user_skin_type:
                    new_list_of_dict.append(animals)
    return new_list_of_dict


def serialize_animal(animal_dict):
    """ Create a string that includes html list items, 
    the selected informations of one animal and line breaks
        :param animal_dict: dictionary with selected information of one animal
        :return:  string with selected information of one animal
    """
    # create html list items for the html page
    animals_str = '<li class="cards__item"> \n <div class="card__title">'
    for key, value in animal_dict.items():
        if key == 'Name':
            animals_str += value + '</div> \n <div class="card__text">\n <ul>'
        else:
            animals_str += '<li><strong>' + key + ':</strong> ' + value + '</li>\n'
    animals_str += '</ul>\n</div>\n</li>\n'
    return animals_str


def create_str_of_info(list_of_dict):
    """ Create a string of all selected information from every animal 
    use the serialize_animal function
        :param list_of_dict: list of dictionaries with selected information
        :return:  string with whole selected information
    """
    animals_str = ''
    for animal in list_of_dict:
        animals_str += serialize_animal(animal)
    return animals_str


def write_html_file(str_selecte_infos):
    """ Write the reading animals_template.html & the selected informations in the animals.html file 
        :params: None
        :return: None
    """
    with open('animals_template.html', 'r', encoding='utf-8') as animal_temp_html:
        animal_html_text = animal_temp_html.read()

    new_html_txt = animal_html_text.replace(
        '__REPLACE_ANIMALS_INFO__', str_selecte_infos)

    with open('animals.html', 'w', encoding='utf-8') as animals_html:
        animals_html.write(new_html_txt)


def main():
    """ Main function to run the script
        :params: None
        :return: None
    """
    animal_name = input('Enter the name of the animal: ')
    # get animal data from the API
    # list of dictionaries every dictionary stands for an animal
    data = fetch_data(animal_name)
    #animals_data = load_data('animals_data.json') 
    if not data:
        str_html_info = f'<h2>The animal {animal_name} does not exist.</h2>'
        write_html_file(str_html_info)
    else:
        list_infos = select_animal_info(data) # old version animal_data
        list_selected_skin_type = user_input_skin_type(list_infos)
        str_infos = create_str_of_info(list_selected_skin_type)
        write_html_file(str_infos)
    print('Website was successfully generated to the file animals.html.')


if __name__ == '__main__':
    main()
