import json

def load_data(file_path):
  """ Loads a JSON file

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
      if 'name' in animal:
          #print('Name:', animal['name'])
          info_dict['Name'] = animal['name']
      if 'diet' in animal['characteristics']:
          #print('Diet:', animal['characteristics']['diet'])
          info_dict['Diet'] = animal['characteristics']['diet']
      if len(animal['locations']) > 0:
          #print('First Location:', animal['locations'][0])
          info_dict['First Location'] = animal['locations'][0]
      if 'type' in animal['characteristics']:
          #print('Type:', animal['characteristics']['type'])
          info_dict['Type'] = animal['characteristics']['type']
      animals_list.append(info_dict)
  #print(animals_list)
  return animals_list

def create_str_of_info(list_of_dict):
  """
  create a string that include all the selected informations and line breaks
  :param list_of_dict: list of dictionaries with selected information
  :return:  string with whole selected information
  """
  animals_str = ''
  for animal in list_of_dict:
      for key, value in animal.items():
          animals_str += key + ': ' + value + '\n'
  return animals_str

list_infos = select_animal_info(animals_data)
str_infos = create_str_of_info(list_infos)

with open('animals_template.html', 'r') as animal_temp_html:
  animal_html_text = animal_temp_html.read()

new_html_txt = animal_html_text.replace('__REPLACE_ANIMALS_INFO__', str_infos)

with open('animals.html', 'w') as animals_html:
   animals_html.write(new_html_txt)





