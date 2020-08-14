def reminder():
    import time
    print("Script Me!!!")
    time.sleep(1)


def safeget(dct, *keys):
    for key in keys:
      dct = dct[key]
    return dct


def wait(seconds):
  import time
  time.sleep(seconds)


def clear():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def yes_no(prompt):
    on = True
    clear()
    while on:
        user = input(prompt).lower()
        if user == 'yes':
            clear()
            return True
        if user == 'no':
            clear()
            return False
        else:
            print("I don't recognize that input, please try again")
            wait(1)
            clear()


def save_to_json(name, data):
    import json
    filename = name + '.json'
    with open(filename, 'w+') as f:
        json.dump(data, f, indent=4)
        f.close()


def load_json(name):
    import json
    with open(str(name) + str('.json'), 'r') as f:
      data = json.load(f)
      f.close()
      return data


def is_prime(x):
  for i in range(2, (x/2)+1):
    if x%i==0:
      return False
  return True


def is_same(x, y):
  if x == y:
    return True
  return False

def nested_set_all(outer, x):
  for inner in outer:
    for i in outer[inner]:
      (outer[inner])[i] = x
  return outer

