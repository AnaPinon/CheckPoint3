#Create a string, number, list, and boolean, each stored in their own variable.
name='Ana Maria'
age=52
hobbies=['leer','cocinar','senderismo']
hobby_leer=True

print (name)
print (age)
print (hobbies)
print("Es mi hobby leer", hobby_leer)

#Use an index to grab the first 3 letters in your string, store that in a variable. 
first_three_letters=name[:3]
print (first_three_letters)

#Use an index to grab the first element from your list.
first_hobby=hobbies[0]
print (first_hobby)

#Create a new number variable that adds 10 to your original number.
myage_masdiez=age+10
print(myage_masdiez)

#Use an index to get the last element in your list.
last_hobby=hobbies[-1]
print (last_hobby)

#Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list)

'''Get the first word from your string using indexes. 
Use the upper function to transform the letters into uppercase. 
Create a new string that takes the uppercase word and the rest of the original string.'''
first_word=name[:3]
first_word_mayuscula=first_word.upper()
new_name= first_word_mayuscula + name[3:]
print (new_name)

# Use string interpolation to print out a sentence that contains your number variable.
sentence= 'Hola, mi nombre es {0}, y tengo {1} años.'.format(name,age)
print(sentence)

#Print “hello world”.
print ("hello world")

'''Además necesito que me crees una cadena que contenga la palabra "Hola". 
Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione
 "Hola" en su cadena. 
Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".'''
indice_hola=sentence.find('Hola')
print(indice_hola)

sentence=sentence.replace('Hola','Adios')
print(sentence)


