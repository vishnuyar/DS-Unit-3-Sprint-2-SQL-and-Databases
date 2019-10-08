import sqlite3

#Creating a connection to the rpg database
conn = sqlite3.connect('rpg_db.sqlite3')
#creating a cursor for rpg database connection
curs = conn.cursor()
#Query for number of characters in the game
query = 'SELECT COUNT(name) FROM charactercreator_character;'
#Executing the query
answer = curs.execute(query)
for row in answer:
    print(f'They are a total of {row[0]} characters in the game')
no_of_characters = row[0]
#Different classes of character by table name
character_class = ['mage','thief','cleric','fighter']
for subclass in character_class:
    query = f'SELECT COUNT(character_ptr_id) FROM charactercreator_{subclass}'
    answer = curs.execute(query)
    for row in answer:
        print(f'They are {row[0]} characters of the class {subclass}')

#Total items in the armoury
query = 'SELECT COUNT(name) FROM armory_item;'
answer = curs.execute(query)
for row in answer:
    print(f'They are a total of {row[0]} items in the armoury')
no_of_items = row[0]
#Number of weapons in the items
query = f'SELECT COUNT(item_ptr_id) FROM armory_weapon;'
answer = curs.execute(query)
for row in answer:
    print(f'They are a total of {row[0]} weapons in the items')
no_of_weapons = row[0]
#Number of non weapons in the items
print(f'They are a total of {(no_of_items-no_of_weapons)} weapons in the items')

#No of items for Top 20 chararcters by name
query = 'select count(item_id) AS no_of_items,name\
        from charactercreator_character_inventory,charactercreator_character\
        where charactercreator_character.character_id = charactercreator_character_inventory.character_id\
        GROUP BY charactercreator_character_inventory.character_id ORDER BY name ASC LIMIT 20;'
answer = curs.execute(query).fetchall()
print('The Number of items of the top 20 characters by name are')
for row in answer:
    print(f'No. of Items:{row[0]}, Name:{row[1]}')

#No of weapons for Top 20 chararcters by name
query = 'select count(armory_weapon.item_ptr_id) AS no_of_items,name\
        from charactercreator_character_inventory,charactercreator_character,armory_weapon\
        where charactercreator_character.character_id = charactercreator_character_inventory.character_id\
        AND charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id\
        GROUP BY charactercreator_character_inventory.character_id ORDER BY name ASC LIMIT 20;'
answer = curs.execute(query).fetchall()
print('The number of weapons of the top 20 characters by name are')
for row in answer:
    print(f'No. of Items:{row[0]}, Name:{row[1]}')

#Total Number of items held by characters
query = 'select count(id) from charactercreator_character_inventory'
answer = curs.execute(query)
for row in answer:
    total_no_of_items = row[0]
#Average number of items for each character
print(f'The average number of items per character is {total_no_of_items/no_of_characters:0.2f}')
#closing the cursor and connection
curs.close()
conn.close()