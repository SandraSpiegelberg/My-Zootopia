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
        print('Name:', animal['name'])
        info_dict['Name'] = animal['name']
      if 'diet' in animal['characteristics']:
        print('Diet:', animal['characteristics']['diet'])
        info_dict['Diet'] = animal['characteristics']['diet']
      if len(animal['locations']) > 0:
        print('First Location:', animal['locations'][0])
        info_dict['First Location'] = animal['locations'][0]
      if 'type' in animal['characteristics']:
        print('Type:', animal['characteristics']['type'])
        info_dict['Type'] = animal['characteristics']['type']
      animals_list.append(info_dict)
  print(animals_list)
  return animals_list


select_animal_information(animals_data)


