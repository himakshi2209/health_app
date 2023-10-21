import mysql.connector as t
m=t.connect(host='localhost',user='root',passwd='ananya123')
mc=m.cursor()

mc.execute('CREATE database IF NOT EXISTS {}'.format('project'))
mc.execute('USE {}'.format('project'))

mc.execute('Create table IF NOT EXISTS {} (Item char(100), Measure char(100), Calories int)'.format('Beverages'))
mc.execute('INSERT INTO BEVERAGES(Item,Measure,Calories) VALUES("Cola","200 ml", 90 )')
mc.execute('INSERT INTO BEVERAGES(Item,Measure,Calories) VALUES("Beer","125 fl.oz",150)')
mc.execute('INSERT INTO BEVERAGES(Item,Measure,Calories) VALUES("Wine","3.5 fl.oz",85)')
mc.execute('INSERT INTO BEVERAGES(Item,Measure,Calories) VALUES("Tea","1 cup",70)')
mc.execute('INSERT INTO BEVERAGES(Item,Measure,Calories) VALUES("Coffee","1 cup",70)')
m.commit()


mc.execute('CREATE TABLE IF NOT EXISTS {} (Item char(100) PRIMARY KEY , Measure char(100), Calories int)'.format('CookedFoods'))
mc.execute('INSERT INTO CookedFoods(Item,Measure,Calories) VALUES("Biscuit(Sweet)","15 gms",70)')
mc.execute('INSERT INTO CookedFoods(Item,Measure,Calories) VALUES("Cake(Plain)","50 gms",135)')
mc.execute('INSERT INTO CookedFoods(Item,Measure,Calories) VALUES("Cake(Rich Chocolate)","50 gms",225)')
mc.execute('INSERT INTO CookedFoods(Item,Measure,Calories) VALUES("Dosa(Plain)","1 medium",135)')
mc.execute('INSERT INTO CookedFoods(Item,Measure,Calories) VALUES("Dosa(Masala)","1 medium",250)')
mc.execute('INSERT INTO CookedFoods(Item,Measure,Calories) VALUES("Pakoras","50 gms",175)')
mc.execute('INSERT INTO CookedFoods(Item,Measure,Calories) VALUES("Puri","1 large",85)')
mc.execute('INSERT INTO CookedFoods(Item,Measure,Calories) VALUES("Samosa","1 piece",140)')
mc.execute('INSERT INTO CookedFoods(Item,Measure,Calories) VALUES("Vada","1 small",70)')
mc.execute('INSERT INTO CookedFoods(Item,Measure,Calories) VALUES("Daal","1 large bowl",80)')
m.commit()


mc.execute('CREATE TABLE IF NOT EXISTS {} (Item char(100) PRIMARY KEY, Measure char(100), Calories int)'.format('Fruits'))
mc.execute('INSERT INTO Fruits(Item,Measure,Calories) VALUES("Apple","1 small",55)')
mc.execute('INSERT INTO Fruits(Item,Measure,Calories) VALUES("Banana","1/2 medium",55)')
mc.execute('INSERT INTO Fruits(Item,Measure,Calories) VALUES("Grapes","15 small",55)')
mc.execute('INSERT INTO Fruits(Item,Measure,Calories) VALUES("Mango","1/2 small",55)')
mc.execute('INSERT INTO Fruits(Item,Measure,Calories) VALUES("Musambi","1 medium",55)')
mc.execute('INSERT INTO Fruits(Item,Measure,Calories) VALUES("Orange","1 medium",55)')
m.commit()
           

mc.execute('CREATE TABLE IF NOT EXISTS {} (Item char(100) PRIMARY KEY, Measure char(100), Calories int)'.format('MainDishes'))
mc.execute('INSERT INTO MainDishes(Item,Measure,Calories) VALUES("Biriyani(Mutton)","1 cup",225)')
mc.execute('INSERT INTO MainDishes(Item,Measure,Calories) VALUES("Biriyani(Veg)","1 cup",200)')
mc.execute('INSERT INTO MainDishes(Item,Measure,Calories) VALUES("Curry(Chicken)","100 gms",225)')
mc.execute('INSERT INTO MainDishes(Item,Measure,Calories) VALUES("Curry(Veg)","100 gms",130)')
mc.execute('INSERT INTO MainDishes(Item,Measure,Calories) VALUES("Fried Fish","85 gms",140)')
mc.execute('INSERT INTO MainDishes(Item,Measure,Calories) VALUES("Veg Pulav","100 gms",130)')
m.commit()


mc.execute('CREATE TABLE IF NOT EXISTS {} (Item char(100) PRIMARY KEY, Measure char(100), Calories int)'.format('Cereals'))
mc.execute('INSERT INTO Cereals(Item,Measure,Calories) VALUES("Chapatti","1 medium",80)')
mc.execute('INSERT INTO Cereals(Item,Measure,Calories) VALUES("Cooked Cereal","1/2 cup",80)')
mc.execute('INSERT INTO Cereals(Item,Measure,Calories) VALUES("Rice Cooked","25 gms",80)')
m.commit()


mc.execute('CREATE TABLE IF NOT EXISTS {} (Item char(100) PRIMARY KEY, Measure char(100), Calories int)'.format('MilkProducts'))
mc.execute('INSERT INTO MilkProducts(Item,Measure,Calories) VALUES("Whole Milk","225 ml",150)')
mc.execute('INSERT INTO MilkProducts(Item,Measure,Calories) VALUES("Paneer","60 gms",150)')
mc.execute('INSERT INTO MilkProducts(Item,Measure,Calories) VALUES("Butter","1 tbsp",45)')
mc.execute('INSERT INTO MilkProducts(Item,Measure,Calories) VALUES("Ghee","1 tbsp",45)')
m.commit()


mc.execute('CREATE TABLE IF NOT EXISTS {} (Item char(100) PRIMARY KEY, Measure char(100), Calories int)'.format('Vegetables'))
mc.execute('INSERT INTO Vegetables(Item,Measure,Calories) VALUES("Potato","1 medium",80)')
mc.execute('INSERT INTO Vegetables(Item,Measure,Calories) VALUES("Mixed Vegetables","150 gms",80)')
m.commit()


mc.execute('CREATE TABLE IF NOT EXISTS {} (Item char(100) PRIMARY KEY, Measure char(100), Calories int)'.format('SweetDishes'))
mc.execute('INSERT INTO SweetDishes(Item,Measure,Calories) VALUES("Carrot Halwa","45 gms",165)')
mc.execute('INSERT INTO SweetDishes(Item,Measure,Calories) VALUES("Jalebi","20 gms",100)')
mc.execute('INSERT INTO SweetDishes(Item,Measure,Calories) VALUES("Kheer","100 gms",180)')
mc.execute('INSERT INTO SweetDishes(Item,Measure,Calories) VALUES("Rasgulla","50 gms",140)')
m.commit()


mc.execute('CREATE TABLE IF NOT EXISTS {} (Item char(100) PRIMARY KEY, Measure char(100), Calories int)'.format('Protein'))
mc.execute('INSERT INTO Protein(Item,Measure,Calories) VALUES("Fish","50 gms",55)')
mc.execute('INSERT INTO Protein(Item,Measure,Calories) VALUES("Mutton"," 1 oz",75)')
mc.execute('INSERT INTO Protein(Item,Measure,Calories) VALUES("Egg","1 piece",75)')
m.commit()
