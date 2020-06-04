# --------------
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
class_1.extend(class_2)
new_class=class_1
print(new_class)
new_class.append("Peter Warden")
print(new_class)
new_class.remove("Carla Gentry")
print(new_class)


##step 2
courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}
total=sum(courses.values())
print(total)
percentage=total*100/500
print(percentage)


##Checking best performance
mathematics={"Goffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}
topper=max(mathematics,key=mathematics.get)
print(topper)


##Maths topper in class
x=topper.split(" ")
first_name=x[0]
last_name=x[1]
full_name=last_name+" "+first_name
certificate_name=full_name.upper()
print(certificate_name)
















