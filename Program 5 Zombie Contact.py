# Program 5: Zombie Contact Tracing
# Owen O'Neil
# 11/21/24



# create list and dictionaries for all part to use
sick_person_list_global = []
contact_list_global = []
all_contacts = []
all_people = []
sick_and_contact = {}

def part_one():
    # For part 1 I decided to use an unordered array because it has an insertion efficiency of Big O(1) which is the fastest insertion and had a sort with a big O(n)
    # Because I am using a nested for loop inorder to create the all_contacts array, the big O of part 1 will be n^2
    # Once the global variables are created the rest of the parts will not have to go through creating the list each time, so they will just have to do a search
    # I will have to sacrifice efficiency for part one in order for the other parts to be more efficient
    # create the sick_person_list
    sick_person_list = []
    # create the contact_list
    contact_list = []
    # add the fist index to of a line the sick person list
    sick_person_list.append(people[0])
    # add it to the global list as well
    sick_person_list_global.append(people[0])
    contacts = people[1:]
    # sort the contacts using built in quick sort
    contacts.sort()
    # format the contacts correctly, so they are correct in the global lists
    formatted_contacts = ", ".join(contacts)
    # add the formatted contacts to the contacts list and the global contact list
    contact_list.append(formatted_contacts)
    contact_list_global.append(formatted_contacts)
    # for an index in the contact list split the list in that index by commas
    for contacts in contact_list_global:
        contact_individual = contacts.split(", ")
        # for a person in that list
        for contact in contact_individual:
            # makes sure there are no repeats
            # if it's not already in the contacts list
            if contact not in all_contacts:
                # add the person to the all_contacts and all_people list
                all_contacts.append(contact)
                all_people.append(contact)
    # for a sick person in the sick person list
    for sick in sick_person_list:
        # if that person is not already in the all_contacts list
        if sick not in all_contacts:
            # add that person to the list
            all_people.append(sick)
    # for and index in the number of indexes in sick_person_list
    for i in range(len(sick_person_list)):
        # print the sick person and their contacts formatted correctly
        print(f"  {sick_person_list[i]} had contact with {contact_list[i]}")


# create the patient_zero list
patient_zero = []
def part_two():
    # Again I decided to use and unordered array because sice the arrays are already created,
    # there is no need to go through making them again and with a searching big O(n), traversing through the array can be simple and efficient
    # creating another array will allow us to single out all the contacted individuals so that there are no repeats and iterating through the list will be easier for all parts following
    # insertion into patient_zero will be big O(n)
    # this will be the same as using the hash table method because I will stil have to iterate throught the dictionary which whill be big O(n)
    # for a sick person in the sick person list
    for sick_person in sick_person_list_global:
        # if the sick person is not in the all contacts list
        if sick_person not in all_contacts:
            # then add that person to the sick person to the patient zero list
            patient_zero.append(sick_person)
    # print the patient zero list formated correctly by joining the indexes and separating them with commas
    print(f"Patient Zeros: {", ".join(patient_zero)}")


# create the potential zombie list
potential_zombie = []
def part_three():
    # once again I am using the unordered array method because the arrays are already created after part one and will be easy to iterate through with a Big O(n)
    # I also chose this method because it is extremely simple to implement and all I would need to do is iterate through the already created lists O(n) and insert into the new list O(n)
    # Using this method and creating one more array will also make the part four much easier
    # This will have the same efficiency as most other data structures so this was method easier to implement
    # for a contact in the all contact list
    for contact in all_contacts:
        # if the contact is not in the sick person list
        if contact not in sick_person_list_global:
            # add that person to the potential zombie list
            potential_zombie.append(contact)
    # print the potential zombie list formated correctly by joining the indexes and separating them with commas
    print(f"Potential Zombies: {", ".join(potential_zombie)}")


# create the not zombie or patient zero list
not_zombie_or_p0 = []
def part_four():
    # part four is almost identical to part three so for the same reasons I used an unordered array
    # iterating through the array with the individual contacts and the potential zombie array makes this part extremely simple and easy to iterate thorugh
    # searching will take a big O(n) and inserting into the new list will be the same
    # the final efficiency is Big O(n)
    # for the contact in the all contacts list
    for contact in all_contacts:
        # if the person is not in the potential zombie and patient zero list
        if contact not in potential_zombie and contact not in patient_zero:
            # add that person to the not zombie ot patient zero list
            not_zombie_or_p0.append(contact)
    # print the not zombie or patient zero list formated correctly by joining the indexes and separating them with commas
    print(f"Neither Patient Zero nor Potential Zombie: {", ".join(not_zombie_or_p0)}")


# create the contact list
most_viral_people = []
def part_five():
    # Go through list and see who has the greatest amount of contacted people
    # For this problem, the best option is to use a hash table because once mapped the big O searching efficiency will be O(1)
    # Although we are using a hash table, we are still using a for loop to iterate through the table so the big O is really (n)
    # The final Big O of part five is (n)
    # I chose this method over an array because it is easier to give a sick person their corresponding contact length
    # create the empty hash table
    contact_count = {}
    # for an index the number of indexes in the sick person list
    for s in range(len(sick_person_list_global)):
        # the sick person is the index in the sick person list
        sick_person = sick_person_list_global[s]
        # the contacted person is the index in the contact list
        contacted_persons = contact_list_global[s].split(", ")
        # adding the sick_person corresponding contact length to its index in contact_count
        contact_count[sick_person] = len(contacted_persons)
    # allows us to search for the biggest value in the hash table(using the .value() method)
    max_contacts = max(contact_count.values())
    # Iterate through the contact_count dictionary to find the people with the maximum contact count
    # I used a website to learn how to use the .items() function to see what items are in the list
    # https: // www.w3schools.com / python / ref_dictionary_items.asp  #:~:text=The%20items()%20method%20returns,the%20dictionary%2C%20see%20example%20below.
    # the sick person is the key and the count is the value in the hash table
    for sick_person, count in contact_count.items():
        # if the count is the same as the max contacts, it will add every sick person that shares the max contact
        if count == max_contacts:
            # add the sick person to the most viral people list
            most_viral_people.append(sick_person)
    # print the most viral people list formated correctly by joining the indexes and separating them with commas
    print(f"Most Viral People: {", ".join(most_viral_people)}")


# creat the most contacted list
most_contacted = []
def part_six():
    # part six is very similar to how I would go about part five
    # Again, the best option is to use a hash table because once mapped the big O searching efficiency will be O(n)
    # This is better than other options because you are able to directly map the amount of times a person is listed in the already created contacts list
    # The final big O is (n^2) which isn't very efficient, but it is the best I could think of because
    # other methods like an unordered list would require an even worse big O efficiency
    # create the empty hash table
    contact_count_table = {}
    # for each index in the global contact list
    for contact in range(len(contact_list_global)):
        # split the list up so each person has an index
        line_of_contacted_people = contact_list_global[contact].split(", ")
        # for a person in the newly split list
        for individual in line_of_contacted_people:
            # if the person is already in the person is already in the list add one to their count in the table
            if individual in contact_count_table:
                contact_count_table[individual] += 1
            # if they are not already in the table then add them to the list and make their count value 1
            else:
                contact_count_table[individual] = 1

    # find the highest number of contacts in the table using the .value() method
    most_contacts = max(contact_count_table.values())
    # for the person and their corresponding count in the list (using the .item() method)
    for individual, count in contact_count_table.items():
        # if the persons contact count is the same as the max count in the table then add them to the most_contacted list
        if count == most_contacts:
            most_contacted.append(individual)
    # print the most contacted list formated correctly by joining the indexes and separating them with commas
    print(f"Most Contacted People: {", ".join(most_contacted)}")


#
def part_seven(p):
    # for part seven I decided to use a recursive statement using the hash table
    # I felt that using the hash table would be best because when the distance is found, the count can be directly mapped to its correcspondig person
    # the efficiency of this would be a big O(n)
    # other methods like linked list and arrays would make setting the counts to the person very hard and lengthy
    # for a person in all people
    # if person is in potential zombies return 0
    if p in potential_zombie:
        return 0
    else:
        # create the distance from a potential zombie
        distance_from_pz = []
        # for a person in a value(contacts for a sick person) the dictionary
        for c in sick_and_contact[p]:
            # add 1 to the subroutine called
            dist = 1 + part_seven(c)
            # add that number to the distance from potential zombie list
            distance_from_pz.append(dist)
        # return the max number in the distance from potential zombie list
        return max(distance_from_pz)


# create the spreader zombies
spreader_zombies = []
def part_eight():
    # for part eight I decided to use the hash table method
    # doing the hash table method makes it easy to know which sick person only has one contact and if that contact is a potential_zombie
    # since it is going through all the dictionary keys and values the big O will be (n)
    # I used this because I would get the same big O as if I used the array method and this way it is easier to impliment
    # for the keys and values in the dictionary
    for sick_person, contacted_persons in sick_and_contact.items():
        # if the length of the list in the value is 1
        if len(contacted_persons) == 1:
            # and the contacted person is in the potential zombie list
            if contacted_persons[0] in potential_zombie:
                # add the sick person/key to the spreader zombies list
                spreader_zombies.append(sick_person)
    # print the spreader zombies list formated correctly by joining the indexes and separating them with commas
    print(f"Spreader Zombies: {", ".join(spreader_zombies)}")

# create the regular zombie list
regular_zombie = []
def part_nine():
    # for part nine I decided to use the dictionary that was made in part one
    # this not only would be very simple to implement but also make it easier to search using a dictionary/hash table
    # because there are lists impeded in the dictionary's values, the search complexity will have to be big O(n)
    # I decided to use this instead of other data structures because I could utilize the any() method when searching through list
    # for the sick_person and contacts in the sick and contacted dictionary
    for sick_person, contact_persons in sick_and_contact.items():
        # I decided so use the any() method because it is slightly more efficient than an if statement because it stops searching once the condition is true
        # has potential zombies is equal to the contacts in the potential zombies list
        has_potential_zombie = any(contact in potential_zombie for contact in contact_persons)
        # has sick person is equal to the contacts in the sick person list
        has_sick_person = any(contact in sick_person_list_global for contact in contact_persons)
        # if has sick person and has potential zombies is true
        if has_sick_person and has_potential_zombie:
            # add sick person to the regular zombie list
            regular_zombie.append(sick_person)
    # print the regular zombie list formated correctly by joining the indexes and separating them with commas
    print(f"Regular Zombie: {", ".join(regular_zombie)}")


def part_ten():
    # I used the hash table created previously in part one, but it is not very efficient because it has a big O(n^2)
    # although its not very efficient it is necessary in order to go through the list in the contact_persons
    # if I were to use other data structures like the array method,
    # I would have to use even more for loops which would make this tack even less efficient
    # create the zombie predator list
    zombie_predator = []
    # for the sick person and contacts in the sick and contacts dictionary
    for sick_person, contact_persons in sick_and_contact.items():
        # for the contacts in the values for each item in the dictionary
        for contact in contact_persons:
            # if the contact is not in the sick person list
            if contact not in sick_person_list_global:
                # move to the next itme
                break
        else:
            # otherwise add the sick person to the zombie predator list
            zombie_predator.append(sick_person)
    # print the zombie predator list formated correctly by joining the indexes and separating them with commas
    print(f"Zombie Predators: {", ".join(zombie_predator)}")

# set the input file to a variable
input_file = ("dataset1.txt")
# open the input file
with (open(input_file, "r")) as f:
    # read each line in the input file
    lines = f.readlines()
    print("Contact Records:")
    # for a line in the input file
    for line in lines:
        # separate the people
        people = line.strip().split(",")
        # call part 1 subroutine
        part_one()
        # add the sick people and their corresponding contacts to the sick and contact dictionary
        sick_and_contact[people[0]] = people[1:]
    print()
    # call subroutine 2-6
    part_two()
    part_three()
    part_four()
    part_five()
    part_six()
    print()
    print("Maximum Distance from a Potential Zombie:")
    # create the maximum distance list
    max_distance = {}
    # for the person in the all people list
    for person in all_people:
        # seth the person to the number output by the part seven subroutine
        max_distance[person] = part_seven(person)
    # I used https://sparkbyexamples.com/python/sort-using-lambda-in-python/ to teach me how to sort this list form the key withe the greatest value to the key with the least value
    # key = lambda x: x[1] goes through each tuple and extracts the value to sort by, the x[1] represents the second element, which is the max distance
    # format correctly for the print statement
    sorted_distances = sorted(max_distance.items(), key=lambda x: x[1], reverse=True)
    # for each item in the sorted distance list, print the person and their distance
    for person, distance in sorted_distances:
        print(f"  {person}: {distance}")
    print()
    # call part 8-10(extra credit)
    part_eight()
    part_nine()
    part_ten()





