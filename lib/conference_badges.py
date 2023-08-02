def badge_maker(name):
    badge_name="Hello, my name is " + name + "."
    return badge_name

def batch_badge_creator(names):
    badge_list=list()
    for name in names:
        badge_name="Hello, my name is " + name + "."
        badge_list.append(badge_name)
    return badge_list

def assign_rooms(names):
    room_list=list();
    room_number=1
    for name in names:
        msg="Hello, "+name+"! You'll be assigned to room "+str(room_number)+"!";
        room_list.append(msg)
        room_number=room_number+1;

    return room_list

def printer(names):
    person_name=batch_badge_creator(names)
   # print(person_name);
    room_details= assign_rooms(names)
  #  print(room_details)
    for item in person_name:
        print(item);
    for lista in room_details:
        print(lista);
    
    return None
