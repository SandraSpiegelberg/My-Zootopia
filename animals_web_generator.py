import json

def load_data(file_path):
  """ 
  Loads a JSON file
    :param file_path: Path to the JSON file
    :return: loaded JSON file
  """
  with open(file_path, "r") as handle:
    return json.load(handle)

# list of dictionaries every dictionary stands for an animal
animals_data = load_data('animals_data.json')

def select_animal_info(data):
  """
  selects the information {Name, Diet, first location, Type}
  if one of these fields doesn't exist, then it doesn't exist as well in the dictionary
    :param data: loaded data
    :return:  list of dictionaries with selected information
  """
  animals_list = []
  for animal in data:
      info_dict = {}
      #select Name of the animals
      if 'name' in animal:
          info_dict['Name'] = animal['name']
      #select Diet of the animals
      if 'diet' in animal['characteristics']:
          info_dict['Diet'] = animal['characteristics']['diet']
      #select First Location of the animals
      if len(animal['locations']) > 0:
          info_dict['First Location'] = animal['locations'][0]
      #select Type of the animals
      if 'type' in animal['characteristics']:
          info_dict['Type'] = animal['characteristics']['type']
      animals_list.append(info_dict)
  return animals_list

def create_str_of_info(list_of_dict):
  """
  create a string that includes html list items, all the selected informations and line breaks
    :param list_of_dict: list of dictionaries with selected information
    :return:  string with whole selected information
  """
  animals_str = ''
  for animal in list_of_dict:
      #create list items for the html page
      animals_str += '<li class="cards__item">'
      for key, value in animal.items():
          animals_str += key + ': ' + value + '<br/>\n'
      animals_str += '</li>'
  return animals_str

list_infos = select_animal_info(animals_data)
str_infos = create_str_of_info(list_infos)

def write_html_file():
  """
  write the reading animals_template.html and the selected informations in the animals.html file 
    :params: None
    :return: None
  """
  with open('animals_template.html', 'r') as animal_temp_html:
    animal_html_text = animal_temp_html.read()

  new_html_txt = animal_html_text.replace('__REPLACE_ANIMALS_INFO__', str_infos)

  with open('animals.html', 'w') as animals_html:
    animals_html.write(new_html_txt)

if __name__ == '__main__':
   write_html_file()



