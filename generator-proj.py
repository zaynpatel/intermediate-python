guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  val = None
  while True:
    if val is not None: 
      line_data = val.strip().split(",")
    else:
      line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
      line_data
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    val = yield name

temp_var = read_guestlist('guest_list.txt')

for temp in range(10):
  print(next(temp_var))
print(temp_var.send("Jane, 35"))
#for items in guests:
  #print(str(items))

twenty_one_plus = []
for guest in guests:
  if guests[guest] >= 21:
    twenty_one_plus.append(guest)
print(twenty_one_plus)

# tuple comp implementation of the above
#over_twenty_one = (guest for guest in guests if guests[guest] >= 21)
#print(list(over_twenty_one))

def table_one():
  for i in range(1,6):
    yield('Chicken', 'Table 1', 'Seat {}'.format(i))
def table_two():
  for u in range(1,6):
    yield('Beef', 'Table 2', 'Seat {}'.format(u))
def table_three():
  for z in range(1,6):
    yield('Fish', 'Table 3', 'Seat {}'.format(z))

def tables():
  yield from table_one()
  yield from table_two()
  yield from table_three()

combined_tables = tables()


def assign_tables(list_of_guests):
  for name in list_of_guests:
    yield (name, next(combined_tables))

guest_assignment = assign_tables(guests)
for person in guest_assignment:
  print(person)
