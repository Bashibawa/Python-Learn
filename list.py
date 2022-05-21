from email import message


bicycles= ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[0].title())
print(bicycles[0].upper())
print(bicycles[-1])
message= "My first bicycle was a "+ bicycles[0].title() + "."
print(message)
friends= ['peter', 'uti', 'isaiah', 'rekpene', 'abigail', 'matthew', 'testimony']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[-3])
print(friends[-2])
print(friends[-1])
message= "Hello dear " + friends[0].title() + " how's your day going?"
print(message)
message_1= "Hello dear " + friends[1].title() + " how's your day going?"
print(message_1)
message= "Hello dear " + friends[2].title() + " how's your day going?"
print(message)
message= "Hello dear " + friends[-4].title() + " how's your day going?"
print(message)
message= "Hello dear " + friends[4].title() + " how's your day going?"
print(message)
message_2= "Hello dear " + friends[-2].title() + " how's your day going?"
message_3= "Hello dear " + friends[-1].title() + " how's your day going?"
print(message_2, "\n" + message_3)
vehicles= ['Toyota', 'Honda', 'Ford', 'Mercedes', 'Lexus']
message= "I would like to own a " + vehicles[0] + " Car"
print(message)
message_1= "I would like to own a " + vehicles[1] + " Car"
message_2= "I would like to own a " + vehicles[2] + " Car"
message_3= "I would like to own a " + vehicles[3] + " Car"
message_4= "I would like to own a " + vehicles[4] + " Car"
print(message_1, "\n" + message_2, "\n" + message_3, "\n" + message_4)
motorcycles= ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0]= 'ducati'
print(motorcycles)
motorcycles= ['honda', 'yamaha', 'suzuki', 'jincheng']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[2]
print(motorcycles)
motorcycles= ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle= motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owned= motorcycles.pop()
print ("The last motocycle I owned ws a " + last_owned.title() + ".")
first_owned= motorcycles.pop(0)
print ("The first motocycle I owned ws a " + first_owned.title() + ".")
