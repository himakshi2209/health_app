from tkinter import *
import time
from tkinter import messagebox as mb
import csv
from PIL import ImageTk
import PIL.Image
from datetime import date

#import mysql.connector
import sendimail
'''
myconnection=mysql.connector.connect(host="localhost", user="root", passwd="ananya123", database='project')
cursor=myconnection.cursor()'''
root=Tk()
root.title('REJUWEL - HEALTH APP')
root.geometry("2000x1000")

with open('checkocheck.txt','w') as filee:
    filee.write('a')
check=[0,0]
countttt=[0,0,0]
rrrr=[]

def raise_frame(frame):
    frame.tkraise()

#function for calorie counter
def cal():
    pass
'''
    ca = Frame(root)
    ca.place(x=0, y=0)
    
    loc = 'bgtry.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((1490, 850), PIL.Image.LANCZOS))
    label = Label(ca, image = photo)
    label.image = photo
    label.grid(row=0, column=0, rowspan=20, columnspan=20)

    l = Label(ca, text="Calorie Counter", padx=15, pady=5, bg="black", fg="white").grid(row=0, column=8, columnspan=5)
    inst = Label(ca, text=" Select all the food items consumed", bg='black', fg='white').grid(row=1, column=8, columnspan=5)

    check[0]+=1
    cursor.execute("show tables;")
    l = []
    l_all = ()
    r = 2
    co = 5
    no = 0
    for i in cursor:
        l.append(i)
    for i in l:
        for j in i:
            r+=1
            l=Label(ca, text=j.upper(), bg="black", fg='white').grid(row=r, column=co, columnspan=2, sticky='W')
            com="select * from " + str(j) + ";"
            cursor.execute(com)
            for x in cursor:
                no+=1
                lala=Label(ca, text=x[1], bg='gray88').grid(row=r+1, column=co+1, sticky='W')
                v='v' + str(no)
                v=IntVar()
                c=Checkbutton(ca, text=x[0].upper(), variable=v, bg='gray88')
                c.grid(row=r+1, column=co, sticky='W')
                r+=1
                l_all+=((v, j, x[0],r+1, co, x[1], x[2]),)
                if r > 14:
                    co+=3
                    r = 2

    def calculate():
        como=0
        l_alll=()
        for i in l_all:
            if i[0].get() == 1:
                clicked = "clicked" + str(como)
                clicked = StringVar()
                clicked.set("1")
                options = [1,2,3,4,5]
                drop=OptionMenu(ca, clicked,*options)
                drop.grid(row=i[3]-1, column=i[4]+2)
                l_alll+=((i[0], i[1], i[2], i[3], i[4],clicked, i[5], i[6]),)
                como+=1
        lasa=Label(ca, text="Select No. Of Servings for selected items", bg='black', fg='white').grid(row=1,column=8,columnspan=5)
        def donedoneadone():
            countttt[0]=1
            c3 = Frame(root)
            c3.place(x=0, y=0)
            
            loc='bgtry.jpg'
            image = PIL.Image.open(loc)
            photo = ImageTk.PhotoImage(image.resize((1490,850), PIL.Image.LANCZOS))
            label = Label(c3, image = photo)
            label.image = photo
            label.grid(row=0, column=0, rowspan=20, columnspan=20)
            
            l=Label(c3, text="Calorie Counter", padx=15, pady=5, bg="black", fg="white")
            l.grid(row=0, column=8, columnspan=2)
            calories=0

            file=open("caloriecounter.txt",'w')
            file.write("Food Items Consumed"+('   ---   ')+"Quantity"+('   ---   ')+"Servings"+('   ---   ')+"Calories per Serving"+'\n')
            ll=Label(c3, text="Food Items Consumed: ", padx=10, pady=5, bg="black", fg="white")
            ll.grid(row=2, column=7)
            ll=Label(c3, text="Quantity: ", padx=10, pady=5, bg="black", fg="white")
            ll.grid(row=2, column=8)
            ll=Label(c3, text="Servings: ", padx=10, pady=5, bg="black", fg="white")
            ll.grid(row=2, column=9)
            ll=Label(c3, text="Calories per serving: ", padx=10, pady=5, bg="black", fg="white")
            ll.grid(row=2, column=10)
            r=3
            c=7
            
            for i in l_alll:
                if i[0].get()==1:
                    if i[1]=="beverages":
                        com="select calories from "+i[1]+" where Item='"+i[2]+"';"
                        cursor.execute(com)
                        for x in cursor:
                            for j in x:
                                calories+=j*int(i[5].get())
                    else:
                        com="select calories from "+i[1]+" where Item='"+i[2]+"';"
                        cursor.execute(com)
                        for x in cursor:
                            for j in x:
                                calories+=j*int(i[5].get())
                    lala=Label(c3, text = i[2].upper(), fg="black", bg='gray88')
                    lala.grid(row=r, column=c)
                    lala=Label(c3, text = i[6].upper(), fg="black", bg='gray88')
                    lala.grid(row=r, column=c+1)
                    lala=Label(c3, text = i[5].get(), fg="black", bg='gray88')
                    lala.grid(row=r, column=c+2)
                    lala=Label(c3, text = i[7], fg="black", bg='gray88')
                    lala.grid(row=r, column=c+3)
                    file.write(i[2]+('   ---   ')+str(i[6])+('   ---   ')+str(i[5].get())+('   ---   ')+str(i[7])+'\n')           
                    r+=1
            file.write("Total No of Calories Consumed Today = "+str(calories)+'\n')
            file.close()
            labelfont = ('helvetica' , 16 )
            finale=Label(c3, text="Total no. of calories = "+str(calories), padx=10, pady=8, bg="black", fg="white")
            finale.config(font=labelfont)
            finale.grid(row=1, column=8, columnspan=2)
            back=Button(c3, text='<', height=1, width=2, padx=10, pady=10, command=homepg)
            back.place(x=0,y=0)
                
        done=Button(ca, text="Done", padx=10, pady=10, height=1, width=7, command=donedoneadone)
        done.grid(row=16, column=10)
        bbb=Button(ca, text="Back", height=1, width=7, padx=10, pady=10, command=cal)
        bbb.grid(row=16, column=12)

                    
    b=Button(ca, text="Ok", height=1, width=7, command=calculate, padx=10, pady=10)
    b.grid(row=16, column=10)
    back=Button(ca, text='<', height=1, width=2, padx=10, pady=10, command=homepg)
    back.place(x=0,y=0)'''

#function for dietplan    
def dietplan():
    dietplan = Frame(root)
    dietplan.place(x=0,y=0)

    loc = 'bg1.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((1450,850),PIL.Image.LANCZOS))
    label = Label(dietplan, image = photo)
    label.image = photo
    label.grid(row=0, column=0, rowspan=25, columnspan=17)

    back=Button(dietplan, text='<', height=1, width=3, padx=10, pady=10, command=homepg)
    back.place(x=0, y=0)

    labelfont = ('helvetica',20)
    l=Label(dietplan, text='Welcome to your Personal Diet Plan !', bg='gray94')
    l.config(font=labelfont)
    l.grid(row=6, column=12)

    def wdc():
        wd = Frame(root)
        wd.place(x=0, y=0)
        
        loc='bg1.jpg'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((1450,850), PIL.Image.LANCZOS))
        label = Label(wd, image = photo)
        label.image = photo
        label.grid(row=0, column=0, rowspan=25, columnspan=30)
        
        l1=Label(wd, text='Weekly Diet Chart', padx=10, bg='gray94')
        l1.grid(row=1, column=19)
        l2=Label(wd, text='Please Enter Your Age:', bg='gray94')
        l2.grid(row=3, column=18)
        mye=Entry(wd, width=10, borderwidth=2)
        mye.grid(row=3, column=19)
        def age():
            age=mye.get()
            if (mye.get()).isdigit()==False:
                text='Kindly enter age in valid format (digits)'
                loc=''
            else:
                m=int(mye.get())
                if 0<=m<=2:
                    loc='10.jpg'
                elif 2<m<=5:
                    loc='11.jpg'
                elif 5<m<=15:
                    loc='22.jpg'
                elif 15<m<=110:
                    loc='33.jpg'
                else:
                    loc=''
                if m>110:
                    text='Kindly enter valid age'
                else:
                    text=''
            if text=='':
                if loc!='':
                    image = PIL.Image.open(loc)
                    photo = ImageTk.PhotoImage(image.resize((700, 500), PIL.Image.LANCZOS))
                    label = Label(wd, image = photo)
                    label.image = photo
                    label.grid(row=4, column=12, rowspan=20, columnspan=25)
            else:
                labbel = Label(wd, text=text, bg='gray94')
                labbel.grid(row=4, column=19)
        b1 = Button(wd, text='Ok', command=age, padx=0, pady=2, bg='gray94')
        b1.grid(row=3, column=20)

        back = Button(wd, text='<', height=1, width=3, padx=10, pady=10, command=lambda:raise_frame(dietplan), bg='gray94')
        back.place(x=0,y=0)

    b = Button(dietplan, text="Weekly Diet Chart (age wise)", padx=10, pady=10, command=wdc, bg='gray94')
    b.grid(row=8, column=12)
    vv =[]
    xy = [0,0]
    xx = [0,0]
    defi = []
    tt = []
    finale = []
    protein = [['Kwashiorkor-edema', 'reddish pigmentation of hair and skin', 'fatty liver', 'retardation of growth in children', 'diarrhea, dermato- sis', 'decreased T-cell lympho- cytes'],
             ['meat', 'fish', 'poultry', 'egg yolk', 'cheese', 'yogurt', 'legumes'], 'protein']
    
    carbohydrate = [['Ketosis'],['whole-grain breads', 'cereals' ,'enriched grain products', 'potatoes','corn', 'legumes', 'fruits', 'vegetables'],'carbohydrate']
    
    fat = [['Eczema', 'low growth rate in infants', 'lowered resistance in infection', 'hair loss'],['meat', 'dairy products', 'egg yolk', 'nuts', 'butter', 'margarine', 'cream', 'salad oils'],'fat']
    
    vitamin_d = [['Rickets','epiphyseal enlargement', 'cranial bossing', 'bowed legs', 'persistently open anterior fontanelle'],['liver', 'fatty fish', 'sunlight'], 'vitamin_d']
    
    vitamin_a = [['Night blindness', 'dry eyes', 'poor bone growth', 'impaired resistance to infection', 'papillary hyperkeratosis of the skin'],
               ['liver', 'egg yolk', 'dark greens' ,'deep yellow vegetables', 'fruits'],'vitamin_a']
    
    vitamin_e = [['Hemolytic anemia in the prema- ture and newborn', 'hyporeflexia', 'spinocerebellar', 'retinal degeneration'],
               ['vegetable oils','liver', 'egg yolk', 'butter', 'green leafy vegetables', 'whole-grain breads', 'cereals', 'wheat germ'], 'vitamin_e']
    
    vitamin_k = [['Prolonged bleeding and prothrombin time', 'hemorrhagic manifestations'], ['vegetable oils', 'green leafy vegetables', 'pork', 'liver'],'vitamin_k']
    
    vitamin_c = [['Scurvy', 'pinpoint peripheral hemorrhages', 'bleeding gums', 'osmotic diarrhea'],['citrus fruits', 'papaya', 'cantaloupe', 'strawberries','potatoes', 'cabbage'],'vitamin_c']
    
    vitamin_b12 = [['Pernicious anemia', 'neurologic deterioration'], ['meat', 'fish', 'poultry', 'cheese', 'egg yolk', 'liver'],'vitamin_b12']
    
    folacin = [['Poor growth', 'megaloblastic anemia', 'impaired cellular immunity'],
             ['liver','green leafy vegetables', 'legumes', 'whole-grain breads', 'cereals','enriched grain products', 'legumes', 'oranges', 'cantaloupe', 'lean beef'],'folacin']
    
    vitamin_b6 = [['Microcytic anemia','convulsions','irritability'],['liver','meat', 'whole-grain breads', 'cereals', 'legumes', 'potatoes'], 'vitamin_b6']
    
    vitamin_b1 = [['Beriberi', 'neuritis', 'edema', 'cardiac failure'],[ 'lean pork', 'wheat germ','whole-grain','enriched breads', 'cereals', 'legumes', 'potatoes'], 'vitamin_b1']
    
    vitamin_b2 = [['Photophobia', 'cheilosis', 'glossitis', 'corneal vascularization', 'poor growth'],
                ['meat','dairy products', 'egg yolk','legumes','green vegetables', 'whole-grain breads', 'cereals'],'vitamin_b2']
    
    niacin = [['Pellegra: dermatitis', 'diarrhea', 'dementia'],['meat','poultry','fish', 'whole-grain breads', 'cereals','egg yolk'],'niacin']
    
    calcium = [['Rickets – abnormal development of bones'],['yogurt', 'cheese','grain products','collards', 'kale','mustard greens', 'turnip greens', 'tofu', 'sardines', 'salmon'],'calcium']
    
    iron = [['Hypochromic microcytic anemia', 'malabsorption','irritability', 'anorexia', 'pallor', 'lethargy'],
          ['meat','liver','legumes', 'whole-grain breads', 'cereals', 'enriched grain products','dark green vegetables'],'iron']
    
    zinc = [['Decreased wound healing', 'hypogonadism', 'mild anemia', 'decreased taste acuity', 'hair loss', 'diarrhea', 'growth failure', 'skin changes'],
          ['meat', 'liver', 'egg yolk', 'oysters and other seafood', 'whole-grain breads', 'cereals','legumes'],'zinc']
    
    fluoride = [['Increased dental caries'],['Fluoridated water'], 'fluoride']
    
    chromium = [['Glucose intolerance', 'impaired growth','peripheral neuropathy', 'negative nitrogen balance', 'decreased respiratory quotient'],
              ['meat', 'whole-grain breads', 'cereals','brewer’s yeast','corn oil'],'chromium']
    
    copper = [['Pallor', 'retarded growth', 'edema', 'anorexia'],['liver','kidney','poultry','shellfish', 'legumes','whole-grain breads', 'cereals'],'copper']
    
    iodine = [['Endemic goiter', 'depressed thyroid function','cretinism'],['seafood', 'iodized salt'], 'iodine']
    
    magnesium = [['Muscle tremors', 'convulsions','irritability','tetany', 'hyper-or hypoflexia'],['whole-grain breads', 'cereals','tofu','legumes', 'green vegetables'], 'magnesium']
    
    manganese = [['Impaired growth','skeletal abnormalities','neonatal ataxia'],['Whole-grain breads', 'cereals','legumes','fruits', 'leafy vegetables'],'manganese']
    
    phosphorous = [['Phosphate depletion effects renal,neuromuscular,skeletal systems,blood chemistry'],['cheese','egg yolk','meat','poultry','fish','whole-grain breads', 'cereals'], 'phosphorus']
    
    potassium = [['Muscle weakness','decreased intestinal tone and distension','cardiac arrhythmias','respiratory failure'],
               ['orange juice','bananas','dried fruits','yogurt','potatoes','meat','fish','poultry','soy products', 'vegetables'], 'potassium']
    
    selenium = [['Myalgia','muscle tenderness','cardiac myopathy','increased fragility of red blood cells', 'degeneration of pancreas'],
              ['Whole-grain breads', 'cereals','onions','meat', 'seafood'],'selenium']
    
    sodium = [['Nausea','cramps','vomiting','dizziness','apathy','exhaustion', 'possible respiratory failure'],['Sodium chloride (table salt)'],'sodium']
    
    pantothenic_acid = [['Fatigue','sleep disturbances','nausea','muscle cramps','impaired coordination', 'loss of antibody production'],
                      ['meat','fish','poultry','liver','egg yolk','yeast', 'whole-grain breads', 'cereals','legumes','vegetables'],'pantothenic_acid']
    
    biotin = [['Seborrheic dermatitis','glossitis','nausea','insomnia'],['liver', 'meat', 'egg yolk', 'yeast', 'bananas', 'most vegetables', 'strawberries', 'grapefruit', 'watermelon'],'biotin']
    
    nutrients = [protein,carbohydrate,fat,vitamin_d,vitamin_a, vitamin_e,vitamin_k,vitamin_c,vitamin_b12, folacin, vitamin_b6,vitamin_b1, vitamin_b2,niacin,calcium,iron,zinc,fluoride,chromium,copper,iodine,manganese,potassium,selenium,sodium,pantothenic_acid,biotin,phosphorous]

    finale = []
    def deficiency():
        xx[0] = xx[0]+1
        if xx[0] == 5:
            xx[0] = 1
            vv.clear()
            finale.clear()
            tt.clear()
            defi.clear()
     
        de = Frame(root)
        de.place(x=0, y=0)
        
        loc='bg1.jpg'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((1450,850), PIL.Image.LANCZOS))
        label = Label(de, image = photo)
        label.image = photo
        label.grid(row=0, column=0, rowspan=25, columnspan=15)
        
        back=Button(de, text='<', height=1, width=3, padx=10, pady=10, command=lambda:raise_frame(dietplan))
        back.place(x=0, y=0)

        labelfont = ('helvetica',20)
        l1 = Label(de, text='Deficiency Identifier', padx=10, bg='gray94')
        l1.config(font=labelfont)
        l1.grid(row=1, column=12, columnspan=2)
        l2 = Label(de, text='Please Select Symptoms Observed:', bg='gray94')
        l2.grid(row=2, column=12, columnspan=2)
        als = []
        for i in nutrients:
            for j in i[0]:
                if j.lower() not in als:
                    als.append(j)
        no = 0
        r = 3
        co = 12
        if xx[0] == 1:
            for i in als[:30]:
                if r>17:
                    r = 3
                    co = co + 1
                v = 'v' + str(no)
                v = IntVar()
                c = 'c' + str(no)
                c = Checkbutton(de, text=i, variable=v, bg='gray94')
                c.grid(row=r, column=co, sticky='W')
                vv.append([v,i])
                no+=1
                r+=1
                
        elif xx[0] == 2:
            for i in als[30:60]:
                if r>17:
                    r = 3
                    co = co + 1
                v = 'v' + str(no)
                v = IntVar()
                c = 'c' + str(no)
                c = Checkbutton(de, text=i, variable=v, bg='gray94')
                c.grid(row=r, column=co, sticky='W')
                vv.append([v,i])
                no+=1
                r+=1
                
        elif xx[0] == 3:
            for i in als[60:90]:
                if r>17:
                    r = 3
                    co=co+1
                v = 'v'+str(no)
                v = IntVar()
                c = 'c'+str(no)
                c = Checkbutton(de, text=i, variable=v,bg='gray94')
                c.grid(row=r, column=co,sticky='W')
                vv.append([v,i])
                no+=1
                r+=1
                
        elif xx[0] == 4:
            for i in als[90:]:
                if r>17:
                    r=3
                    co=co+1
                v = 'v'+str(no)
                v = IntVar()
                c = 'c'+str(no)
                c = Checkbutton(de, text=i, variable=v,bg='gray94')
                c.grid(row=r, column=co,sticky='W')
                vv.append([v,i])
                no+=1
                r+=1
                
        def new1():
            countttt[1]=1
            xy[0]+=1
            nww = Frame(root)
            nww.place(x=0, y=0)
            
            loc='bg1.jpg'
            image = PIL.Image.open(loc)
            photo = ImageTk.PhotoImage(image.resize((1450,850), PIL.Image.LANCZOS))
            label = Label(nww, image = photo)
            label.image = photo
            label.grid(row=0, column=0, rowspan=25, columnspan=15)

            back=Button(nww, text='<', height=1, width=3, padx=10, pady=10, command=lambda:raise_frame(dietplan))
            back.place(x=0, y=0)

            labelfont = ('helvetica',20)
            l1=Label(nww, text='Deficiency Identifier', padx=10, bg='gray94')
            l1.config(font=labelfont)
            l1.grid(row=1, column=11)
            lab=Label(nww, text='Deficiencies Identifies are:', bg='gray94')
            lab.config(font=labelfont)
            lab.grid(row=2, column=11)
            
            rooo = 4
            cooo = 6
            
            if xy[0]>=1:
                for i in vv:
                    if i[0].get() == 1:
                        tt.append(i[1])
                for i in nutrients:
                    for j in tt:
                        if j in i[0]:
                            defi.append(i[2])
                finale=[]
                while True:
                    for i in defi:
                        finale.append([i,defi.count(i)])
                        for j in range(defi.count(i)):
                            defi.remove(i)
                    if defi==[]:
                        break

            lala = Label(nww, text='Low probability', bg='gray94')
            lala.grid(row=rooo, column=10)
            lala = Label(nww, text='Medium probability', bg='gray94')
            lala.grid(row=rooo, column=11)
            lala = Label(nww, text='High probability', bg='gray94')
            lala.grid(row=rooo, column=12)
            rooo+=1
            r1 = rooo
            r2 = rooo
            r3 = rooo
            c1 = 5
            c2 = 6
            c3 = 7
            file=open('deficiency.txt','w')
            file.write('Deficiency'+(' '*(15-len('deficiency')))+'Probability'+'\n')

            for i in finale:
                if 1<=i[1]<2:
                    lala = Label(nww, text=i[0], bg='gray94')
                    lala.grid(row=r1, column=c1+5)
                    r1+=1
                    if r1>18:
                        lala = Label(nww, text='Low probability', bg='gray94')
                        lala.grid(row=rooo-1, column=6)
                        r1 = rooo
                        c1=4
                    file.write(i[0]+(' '*(15-len(i[0])))+'Low'+'\n')
                elif 2<=i[1]<=5:
                    lala = Label(nww, text=i[0], bg='gray94')
                    lala.grid(row=r2, column=c2+5)
                    r2+=1
                    if r2>18:
                        lala = Label(nww, text='Medium probability', bg='gray94')
                        lala.grid(row=rooo-1, column=7)
                        r2 = rooo
                        c2 = 9
                    file.write(i[0]+(' '*(15-len(i[0])))+'Medium'+'\n')
                elif i[1]>5:
                    lala = Label(nww, text=i[0], bg='gray94')
                    lala.grid(row=r3, column=c3+5)
                    r3+=1
                    if r3>18:
                        lala = Label(nww, text='High probability', bg='gray94')
                        lala.grid(row=rooo-1, column=8)
                        r3 = rooo
                        cl = 8
                    file.write(i[0]+(' '*(15-len(i[0])))+'High'+'\n')
            file.close()

            def redo():
                xx[0] == 0
                deficiency()
            bb = Button(nww, text="Test Again", command=redo)
            bb.grid(row=19, column=11)
    
        if xx[0]<4:
            buttons = Button(de, text="Next", command=deficiency)
            buttons.grid(row=r, column=12, columnspan=2)
        else:
            buttons = Button(de, text="Done", command=new1)
            buttons.grid(row=r, column=12, columnspan=2)
        if xx[0]>4:
            new1()

    b1 = Button(dietplan, text="Deficiency Identifier", padx=10, pady=10, bg='gray94', command=deficiency)
    b1.grid(row=10, column=12)

    def specialfood():
        nw1 = Frame(root)
        nw1.place(x=0,y=0)
        
        loc='bg1.jpg'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((1450,850), PIL.Image.LANCZOS))
        label = Label(nw1, image = photo)
        label.image = photo
        label.grid(row=0, column=0, rowspan=25, columnspan=15)
        back=Button(nw1, text='<', height=1, width=3, padx=10, pady=10, command=lambda:raise_frame(dietplan))
        back.place(x=0, y=0)

        labelfont = ('helvetica',20)
        l1 = Label(nw1, text='Foods You Need To Consume More', padx=10, bg='gray94')
        l1.config(font=labelfont)
        l1.grid(row=1, column=9, columnspan=3)
        def display_fin():
            countttt[2]=1
            nww1 = Frame(root)
            nww1.place(x=0,y=0)
            
            loc='bg1.jpg'
            image = PIL.Image.open(loc)
            photo = ImageTk.PhotoImage(image.resize((1450,850), PIL.Image.LANCZOS))
            label = Label(nww1, image = photo) 
            label.image = photo
            label.grid(row=0, column=0, rowspan=25, columnspan=15)
            
            back=Button(nww1, text='<', height=1, width=3, padx=10, pady=10, command=lambda:raise_frame(dietplan))
            back.place(x=0, y=0)
            
            tess=[]
            for i in nutrients:
                for j in defi:
                    if i[2] == j and tess.count(i[1]) == 0:
                        tess.append(i[1])
            r = 3
            c = 8
            crackpot = []
            file=open('foodconsume.txt','w')
            file.write('Foods You Need To Consume More - '+'\n')

            labelfont = ('Helvetica', 20)
            l1 = Label(nww1, text='Foods You Need To Consume More', bg='gray94')
            l1.config(font = labelfont)
            l1.grid(row=2, column=8, columnspan=3)
            for i in tess:
                for j in i:
                    if crackpot.count(j) == 0:
                        crackpot.append(j)
            for i in crackpot:
                lala = Label(nww1, text=i, bg='gray94')
                lala.grid(row=r+2, column=c+1)
                r+=1
                if r>15:
                    r = 3
                    c+=1
                file.write(i+'\n')
            file.close()
            
        if defi == []:
            l2 = Label(nw1, text='Please Select Deficiencies Present:', bg='gray94')
            l2.grid(row=2, column=9, columnspan=3)
            r = 4
            co = 6
            vv = []
            no = 0
            for i in nutrients:
                v = 'v' + str(no)
                v = IntVar()
                c = Checkbutton(nw1, text=i[2], variable=v, bg='gray94')
                c.grid(row=r, column=co+3, sticky='W')
                vv.append([v, i[2]])
                r+=1
                if r>13:
                    r = 4
                    co+=1
                no+=1
            def done():
                for i in vv:
                    if i[0].get() == 1:
                        defi.append(i[1])
                display_fin()
            b3 = Button(nw1, text="Done", padx=10, pady=0, command=done)
            b3.grid(row=14, column=10)
        else:
            display_fin()

    b2=Button(dietplan, text="Food Guide", padx=10, pady=10, bg='gray94', command=specialfood)
    b2.grid(row=12, column=12)

#function for workout
def workout():
    def monday1():
        mon1 = Frame(root)
        mon1.place(x=0,y=0,width=2000,height=1000)
        
        loc = 'Monday1.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=mon1)
        label = Label(mon1, image = photo)
        label.image = photo
        label.grid(row=0, column=15, rowspan=20, columnspan=5)
        
        lb1 = Label(mon1,text='MONDAY:CHEST AND TRICEPS').grid(row=0,column=0)
        lb2 = Label(mon1,text='Warm up:').grid(row=1,column=0)
        list1 = [['Small circles forward/backward arms out','10 each'],['Large circles forward/backward arms out','10 each'],
               ['Dynamic chest stretch(arms straight out,swing from front to back)','30 sec'],['Door frame stretches','10 each']]
        r=2;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(mon1,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        blank=Label(mon1,text='.').grid(row=6,column=0,sticky=W)

        lb11=Label(mon1,text='Exercises:').grid(row=7,column=0)
        list2=[['Push-ups on Knees','2 sets of 8'],['Seated dips','2 sets of 6'],['Elevated push-ups(hands on elevated surface)','2 sets of 6'],
               ['Close push-ups(hands 6 inches apart, on knees)','2 sets of 5'],
                   ['Wide push-ups with 5 seconds down/1 second hold/5 seconds up(on knees)','2 sets of 5']]

        r=8;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(mon1,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        blank=Label(mon1,text='.').grid(row=13,column=0,sticky=W)

        lb22=Label(mon1,text='Cool Down:').grid(row=16,column=0)
        list3=[['Arm crosses','2 sets of 10 sec./arm'],
                   ['Door frame stretches','30 sec'],['Behind the head bent elbow stretch','2 sets of 10 sec./arm']]
        r=18;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(mon1,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(mon1,text='<',height=1,width=2,padx=10,pady=10,command=beginner)
        back.place(x=0,y=0)

    def tuesday1():
        tue1=Frame(root)
        tue1.place(x=0,y=0,width=2000,height=1000)
        
        loc='Tuesday1.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=tue1)
        label = Label(tue1, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=20, columnspan=5)
        
        lb1=Label(tue1,text='TUESDAY:LOWER BODY').grid(row=0,column=0,sticky=E)
        lb2=Label(tue1,text='Warm up:').grid(row=1,column=0)

        list1=[['Knee hugs','3/leg for 3 sec. each'],['Leg cradles','3/leg for 3 sec. each'],
               ['Quad stretch','3/leg for 3 sec. each'],['Hamstring kicks','10/leg'],['Butterfly stretch','20 sec']]
        r=2;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(tue1,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1       

        blank=Label(tue1,text='.').grid(row=7,column=0,sticky=W)   
        lb13=Label(tue1,text='Exercises:').grid(row=8,column=0)
        list2=[['Bodyweight Squat','2 sets of 8'],['Elevated calf raises','2 sets of 12'],['Split squats','2 sets of 6/leg'],
               ['One-legged elevated calf raise','2 sets of 8/leg'],
                   ['Bear squats','2 sets of 8'],['Squat jumps','2 sets of 5']]
        r=9;c=0
        for i in range(6):
            for j in range(2):
                lb=Label(tue1,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(tue1,text='.').grid(row=15,column=0,sticky=W)
        lb24=Label(tue1,text='Cool Down:').grid(row=16,column=0)
        list3=[['Toe touches on floor(legs spread','2 sets of 20 sec./leg'],
                   ['Butterfly stretches','2 sets of 20 sec'],['Knee hugs(on floor)','2 sets of 15 sec./leg'],
               ['Calf Streches','2 sets of 10 sec./leg']]

        r=17;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(tue1,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(tue1,text='<',height=1,width=2,padx=10,pady=10,command=beginner)
        back.place(x=0,y=0)

    def thursday1():
        thu1=Frame(root)
        thu1.place(x=0,y=0,width=2000,height=1000)
        
        loc='Thursday1.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=thu1)
        label = Label(thu1, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=20, columnspan=5)
        
        lb1=Label(thu1,text='THURSDAY:BACK').grid(row=0,column=0)
        lb2=Label(thu1,text='Warm up:').grid(row=1,column=0)
        
        list1=[['Side bends','10/side'],['Trunk Rotations(alternating directions)','10'],
               ['Supine bridge','10'],['Shoulder blade squeeze','8'],['Trunk twists','6/side']]
        r=2;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(thu1,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1       

        blank=Label(thu1,text='.').grid(row=7,column=0,sticky=W)

        lb13=Label(thu1,text='Exercises:').grid(row=8,column=0)
        list2=[['Australian pull-ups/bodyweight rows(upper back)','2 sets of 5'],['Supermans','2 sets of 8'],
               ['Australian pull-up(mid back)','2 sets of 5'],['Scapula push-ups','2 sets of 8'],
                   ['3 position towel rows','2 sets of 3/position']]
        r=9;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(thu1,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(thu1,text='.').grid(row=14,column=0,sticky=W)
        lb24=Label(thu1,text='Cool Down:').grid(row=15,column=0)
        list3=[['Entended leg stretch','2 sets of 10 sec./leg'],['Cat stretch','10'],
               ['Trunk twist & hold','3 sets of 5 sec./leg'],['Shoulder blade squeeze','8']]
        r=18;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(thu1,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(thu1,text='<',height=1,width=2,padx=10,pady=10,command=beginner)
        back.place(x=0,y=0)

    def friday1():
        fri1=Frame(root)
        fri1.place(x=0,y=0,width=2000,height=1000)
        
        lb1=Label(fri1,text='FRIDAY:CORE').grid(row=0,column=0)
        lb2=Label(fri1,text='Warm up:').grid(row=1,column=0)
        
        loc='Friday1.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=fri1)
        label = Label(fri1, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=20, columnspan=5)
        
        list1=[['Standing arch','15 sec'],['Side bends','10/side'],['Cobra','15 sec']]
        r=2;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(fri1,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1       

        blank=Label(fri1,text='.').grid(row=5,column=0,sticky=W)   
        lb9=Label(fri1,text='Exercises:').grid(row=6,column=0)
        lb10=Label(fri1,text='To be done in 3 rounds (no rest between exercises; one minute rest between rounds)').grid(row=7,column=0)
        list2=[['Flutter kicks','10 seconds'],['V-ups','10 seconds'],['Planks','15 seconds'],['Hip-dip','10 sec./side'],
                   ['Crunchy Frogs','15 seconds']]
        r=8;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(fri1,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(fri1,text='.').grid(row=13,column=0,sticky=W)
        lb21=Label(fri1,text='Cool Down:').grid(row=14,column=0)
        list3=[['Cobra stretch','20 seconds'],
                   ['Supine stretch','20 sec'],['Standing arch','20 sec']]
        r=18;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(fri1,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(fri1,text='<',height=1,width=2,padx=10,pady=10,command=beginner)
        back.place(x=0,y=0)

    def saturday1():
        sat1=Frame(root)
        sat1.place(x=0,y=0,width=2000,height=1000)
        
        loc='Saturday1.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=sat1)
        label = Label(sat1, image = photo)
        label.image = photo
        label.grid(row=0, column=12, rowspan=20, columnspan=5)
        
        lb1=Label(sat1,text='SATURDAY:SHOULDER AND BICEP').grid(row=0,column=0,sticky=E)
        lb2=Label(sat1,text='Warm up:').grid(row=1,column=0)
        list1=[['Forearm stretch','2 sets of 3 sec./arm'],['Arm crosses','2 sets of 10 sec./arm'],
               ['Shoulder stretches on wall','5/arm'],['Behind the head bent elbow stretch','2 sets of 10 sec./arm']]
        r=2;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(sat1,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1       

        blank=Label(sat1,text='.').grid(row=7,column=0,sticky=W)
        lb11=Label(sat1,text='Exercises:').grid(row=8,column=0)
        list2=[['Elevated Pike push-ups (upper body raised)','2 sets of 5'],['Australian chin-ups','2 sets of 5'],
               ['Sidelying bodyweight bicep curls','2 sets of 4/arm'],
               ['Crab walk (forward and backward)','2 sets 20 sec.'],['Assisted chin-ups','2 sets of 4']]
        r=9;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(sat1,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(sat1,text='.').grid(row=14,column=0,sticky=W)
        lb24=Label(sat1,text='Cool Down:').grid(row=15,column=0)
        list3=[['Forearm stretch','2 sets of 3 sec./arm'],['Arm crosses','2 sets of 10 sec./arm'],
               ['Shoulder stretches on wall','5/arm'],['Behind the head bent elbow stretch','2 sets of 10 sec./arm']]
        r=18;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(sat1,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(sat1,text='<',height=1,width=2,padx=10,pady=10,command=beginner)
        back.place(x=0,y=0)

        
    def beginner():
        beg=Frame(root)
        beg.place(x=0,y=0,width=2000,height=1000)
        
        loc='wpf.jpg'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((1490,850),PIL.Image.LANCZOS), master=beg)
        label = Label(beg, image = photo)
        label.image = photo
        label.grid(row=0, column=0, rowspan=20, columnspan=20)
        lb1=Label(beg,text='Welcome to your workout if you have just started exercising.',bg='goldenrod1').grid(row=1,column=3)
        lb3=Label(beg,text='**************',bg='goldenrod1').grid(row=2,column=3)
        mon=Button(beg,text='Monday',height=1,width=10,padx=10,pady=10,command=monday1).grid(row=3,column=3)
        tue=Button(beg,text='Tuesday',height=1,width=10,padx=10,pady=10,command=tuesday1).grid(row=4,column=3)
        wed=Label(beg,text='Wednesday: please relax today:)',bg='goldenrod1').grid(row=5,column=3)
        thu=Button(beg,text='Thursday',height=1,width=10,padx=10,pady=10,command=thursday1).grid(row=6,column=3)
        fri=Button(beg,text='Friday',height=1,width=10,padx=10,pady=10,command=friday1).grid(row=7,column=3)
        sat=Button(beg,text='Saturday',height=1,width=10,padx=10,pady=10,command=saturday1).grid(row=8,column=3)
        sun=Label(beg,text='Sunday: please relax today:)',bg='goldenrod1').grid(row=9,column=3)
        blank=Label(beg,text='********************',bg='goldenrod1',height=1,width=10,padx=10,pady=10).grid(row=10,column=3)
        back=Button(beg,text='<',height=1,width=2,padx=10,pady=10,command=lambda:raise_frame(workout))
        back.place(x=0,y=0)
        

    def monday2():
        mon2=Frame(root)
        mon2.place(x=0,y=0,width=2000,height=1000)
        
        loc='Monday2.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=mon2)
        label = Label(mon2, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=20, columnspan=5)
        
        lb1=Label(mon2,text='MONDAY:CHEST AND TRICEPS').grid(row=0,column=0)
        lb2=Label(mon2,text='Warm up:').grid(row=1,column=0)
        list1=[['Small circles forward/backward arms out','10 each'],['Large circles forward/backward arms out','10 each'],
               ['Dynamic chest stretch(arms straight out,swing from front to back quickly)','30 sec'],
               ['Door frame stretches','10 each']]
        r=2;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(mon2,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1       

        blank=Label(mon2,text='.').grid(row=6,column=0,sticky=W)
        lb11=Label(mon2,text='Exercises:').grid(row=7,column=0)
        list2=[['Regular Push-ups','2 sets of 10'],['Seated dips','2 sets of 8'],['Shuffle push-ups','2 sets of 4/side'],
               ['Close push-ups(hands 6 inches apart, on knees)','2 sets of 5'],
                ['Wide push-ups with 5 seconds down/1 second hold/5 seconds up(on knees)','2 sets of 8']]
        r=8;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(mon2,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        blank=Label(mon2,text='.').grid(row=13,column=0,sticky=W)
        lb22=Label(mon2,text='Cool Down:').grid(row=14,column=0)
        list3=[['Arm crosses','2 sets of 10 sec./arm'],
                   ['Door frame stretches','30 sec'],['Behind the head bent elbow stretch','2 sets of 10 sec./arm']]
        r=18;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(mon2,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(mon2,text='<',height=1,width=2,padx=10,pady=10,command=intermediate)
        back.place(x=0,y=0)

    def tuesday2():
        tue2=Frame(root)
        tue2.place(x=0,y=0,width=2000,height=1000)
        
        loc='Tuesday2.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=tue2)
        label = Label(tue2, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=22, columnspan=5)
        
        lb1=Label(tue2,text='TUESDAY:LOWER BODY').grid(row=0,column=0,sticky=E)
        lb2=Label(tue2,text='Warm up:').grid(row=1,column=0)
        list1=[['Knee hugs','3/leg for 3 sec. each'],['Leg cradles','3/leg for 3 sec. each'],
               ['Quad stretch','3/leg for 3 sec. each'],['Hamstring kicks','10/leg'],['Butterfly stretch','20 sec']]
        r=2;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(tue2,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1       

        blank=Label(tue2,text='.').grid(row=7,column=0,sticky=W)
        lb13=Label(tue2,text='Exercises:').grid(row=8,column=0)
        list2=[['Bodyweight Squat','2 sets of 12'],['Elevated calf raises','2 sets of 15'],
               ['Split squats','2 sets of 8/leg'],['One-legged elevated calf raise','2 sets of 10/leg'],
               ['Bear squats','2 sets of 12'],['Squat jumps','2 sets of 8']]
        r=9;c=0
        for i in range(6):
            for j in range(2):
                lb=Label(tue2,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(tue2,text='.').grid(row=15,column=0,sticky=W)
        lb24=Label(tue2,text='Cool Down:').grid(row=16,column=0)
        list3=[['Toe touches on floor(legs spread)','2 sets of 20 sec./leg'],['Butterfly stretches','2 sets of 20 sec'],
               ['Knee hugs(on floor)','2 sets of 15 sec./leg'],['Calf Streches','2 sets of 10 sec./leg']]
        r=18;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(tue2,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(tue2,text='<',height=1,width=2,padx=10,pady=10,command=intermediate)
        back.place(x=0,y=0)

    def thursday2():
        thu2=Frame(root)
        thu2.place(x=0,y=0,width=2000,height=1000)
        
        loc='Thursday2.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=thu2)
        label = Label(thu2, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=22, columnspan=5)
        
        lb1=Label(thu2,text='THURSDAY:BACK').grid(row=0,column=0)
        lb2=Label(thu2,text='Warm up:').grid(row=1,column=0)
        list1=[['Side bends','10/side'],['Trunk Rotations(alternating directions)','10'],
               ['Supine bridge','10'],['Shoulder blade squeeze','8'],['Trunk twists','6/side']]
        r=2;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(thu2,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(thu2,text='.').grid(row=7,column=0,sticky=W)
        lb13=Label(thu2,text='Exercises:').grid(row=8,column=0)
        list2=[['Australian pull-ups/bodyweight rows (upper back)','2 sets of 7'],['Supermans','2 sets of 10'],
               ['Australian pull-ups(mid back)','2 sets of 7'],['Scapula push-ups','2 sets of 10'],
               ['3 position towel rows','2 sets of 5/position']]
        r=9;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(thu2,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(thu2,text='.').grid(row=14,column=0,sticky=W)
        lb24=Label(thu2,text='Cool Down:').grid(row=15,column=0)
        list3=[['Entended leg stretch','2 sets of 10 sec./leg'],['Cat stretch','10'],
               ['Trunk twist & hold','3 sets of 5 sec./leg'],['Sitting twist & hold','3 sets of 5 sec./leg'],
               ['Shoulder blade squeeze','8']]
        r=18;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(thu2,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(thu2,text='<',height=1,width=2,padx=10,pady=10,command=intermediate)
        back.place(x=0,y=0)

    def friday2():
        fri2=Frame(root)
        fri2.place(x=0,y=0,width=2000,height=1000)
        
        loc='Friday2.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=fri2)
        label = Label(fri2, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=22, columnspan=5)
        
        lb1=Label(fri2,text='FRIDAY:CORE').grid(row=0,column=0)
        lb2=Label(fri2,text='Warm up:').grid(row=1,column=0)
        list1=[['Standing arch','15 sec'],['Side bends','10/side'],['Cobra','15 sec']]
        r=2;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(fri2,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        blank=Label(fri2,text='.').grid(row=5,column=0,sticky=W)
        lb9=Label(fri2,text='Exercises:').grid(row=6,column=0)
        lb10=Label(fri2,text='To be done in 3 rounds (no rest between exercises; one minute rest between rounds)').grid(row=7,column=0)
        list2=[['Flutter kicks','15 seconds'],['V-ups','15 seconds'],['Planks','20 seconds'],
               ['Hip dip','15 sec./side'],['Crunchy Frogs','20 seconds']]
        r=9;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(fri2,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        blank=Label(fri2,text='.').grid(row=14,column=0,sticky=W)
        lb21=Label(fri2,text='Cool Down:').grid(row=15,column=0)
        list3=[['Cobra stretch','20 sec'],['Supine stretch','20 sec'],['Standing arch','20 sec']]
        r=18;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(fri2,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(fri2,text='<',height=1,width=2,padx=10,pady=10,command=intermediate)
        back.place(x=0,y=0)

    def saturday2():
        sat2=Frame(root)
        sat2.place(x=0,y=0,width=2000,height=1000)
        
        loc='Saturday2.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=sat2)
        label = Label(sat2, image = photo)
        label.image = photo
        label.grid(row=0, column=12, rowspan=20, columnspan=5)
        
        lb1=Label(sat2,text='SATURDAY:SHOULDER AND BICEP').grid(row=0,column=1)
        lb2=Label(sat2,text='Warm up:').grid(row=1,column=0)
        list1=[['Forearm stretch','2 sets of 3 sec./arm'],['Arm crosses','2 sets of 10 sec./arm'],
               ['Shoulder stretches on wall','5/arm'],['Behind the head bent elbow stretch','2 sets of 10 sec./arm']]
        r=2;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(sat2,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(sat2,text='.').grid(row=7,column=0,sticky=W)   
        lb11=Label(sat2,text='Exercises:').grid(row=8,column=0)
        list2=[['Pike push-ups','2 sets of 8'],['Australian chin-ups','2 sets of 8'],
               ['Sidelying bodyweight bicep curls','2 sets of 6/arm'],['Crab walk','2 sets of 30 sec.'],
               ['Assisted chin-ups','2 sets of 6']]
        r=9;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(sat2,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(sat2,text='.').grid(row=14,column=0,sticky=W)
        lb24=Label(sat2,text='Cool Down:').grid(row=15,column=0)
        list3=[['Forearm stretch','2 sets of 3 sec./arm'],['Arm crosses','2 sets of 10 sec./arm'],
               ['Shoulder stretches on wall','5/arm'],['Behind the head bent elbow stretch','2 sets of 10 sec./arm']]
        r=18;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(sat2,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(sat2,text='<',height=1,width=2,padx=10,pady=10,command=intermediate)
        back.place(x=0,y=0)

    def intermediate():
        inte=Frame(root)
        inte.place(x=0,y=0,width=2000,height=1000)
        
        loc='wpf.jpg'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((1490,850),PIL.Image.LANCZOS), master=inte)
        label = Label(inte, image = photo)
        label.image = photo
        label.grid(row=0, column=0, rowspan=20, columnspan=20)
        
        lb1=Label(inte,text='Welcome to your workout if you have just started exercising.',bg='goldenrod1').grid(row=1,column=3)
        lb3=Label(inte,text='**************',bg='goldenrod1').grid(row=2,column=3)
        mon=Button(inte,text='Monday',height=1,width=10,padx=10,pady=10,command=monday2).grid(row=3,column=3)
        tue=Button(inte,text='Tuesday',height=1,width=10,padx=10,pady=10,command=tuesday2).grid(row=4,column=3)
        wed=Label(inte,text='Wednesday: please relax today:)',bg='goldenrod1').grid(row=5,column=3)
        thu=Button(inte,text='Thursday',height=1,width=10,padx=10,pady=10,command=thursday2).grid(row=6,column=3)
        fri=Button(inte,text='Friday',height=1,width=10,padx=10,pady=10,command=friday2).grid(row=7,column=3)
        sat=Button(inte,text='Saturday',height=1,width=10,padx=10,pady=10,command=saturday2).grid(row=8,column=3)
        sun=Label(inte,text='Sunday: please relax today:)',bg='goldenrod1').grid(row=9,column=3)
        blank=Label(inte,text='********************',bg='goldenrod1').grid(row=10,column=3)
        back=Button(inte,text='<',height=1,width=2,padx=10,pady=10,command=lambda:raise_frame(workout))
        back.place(x=0,y=0)

    def monday3():
        mon3=Frame(root)
        mon3.place(x=0,y=0,width=2000,height=1000)
        
        loc='Monday3.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=mon3)
        label = Label(mon3, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=20, columnspan=5)
        
        lb1=Label(mon3,text='MONDAY:CHEST AND TRICEPS').grid(row=0,column=0)
        lb2=Label(mon3,text='Warm up:').grid(row=1,column=0)
        list1=[['Small circles forward/backward arms out','10 each'],['Large circles forward/backward arms out','10 each'],
               ['Dynamic chest stretch(arms straight out,swing from front to back quickly)','10'],
               ['Door frame stretches','30 sec']]
        r=2;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(mon3,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(mon3,text='.').grid(row=6,column=0,sticky=W)

        lb11=Label(mon3,text='Exercises:').grid(row=7,column=0)
        list2=[['Push-up with one-second pause','2 sets of 8'],['Dips','2 sets of 6'],
               ['Wide push ups with 5 seconds down/1 second hold/5 seconds up (knees off ground)','2 sets of 5'],
               ['Close push-ups(hands 6 inches apart, knees off ground)','2 sets of 8'],
               ['Extended range of motion (EROM) push-ups','2 sets of 7']]
        r=8;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(mon3,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(mon3,text='.').grid(row=13,column=0,sticky=W)
        lb22=Label(mon3,text='Cool Down:').grid(row=14,column=0)
        list3=[['Arm crosses','2 sets of 10 sec./arm'],['Door frame stretches','30 sec'],
               ['Behind the head bent elbow stretch','2 sets of 10 sec./arm']]
        r=18;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(mon3,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(mon3,text='<',height=1,width=2,padx=10,pady=10,command=advanced)
        back.place(x=0,y=0)

    def tuesday3():
        tue3=Frame(root)
        tue3.place(x=0,y=0,width=2000,height=1000)
        
        loc='Tuesday3.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=tue3)
        label = Label(tue3, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=22, columnspan=5)
        
        lb1=Label(tue3,text='TUESDAY:LOWER BODY').grid(row=0,column=0)
        lb2=Label(tue3,text='Warm up:').grid(row=1,column=0)
        list1=[['Knee hugs','3/leg for 3 sec. each'],['Leg cradles','3/leg for 3 sec. each'],
               ['Quad stretch','3/leg for 3 sec. each'],['Hamstring kicks','10/leg'],['Butterfly stretch','20 sec']]
        r=2;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(tue3,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1 

        blank=Label(tue3,text='.').grid(row=7,column=0,sticky=W)
        lb13=Label(tue3,text='Exercises:').grid(row=8,column=0)
        list2=[['Bodyweight Squat with one second hold','2 sets of 12'],
               ['Elevated calf raises with standard,toes in toes out','2 sets of 8 each'],
               ['Bulgarian split squats','2 sets of 10/leg'],
               ['One-legged elevated calf raise with 2 sec. hold','2 sets of 10/leg'],
               ['Bodyweight squat with pulse & pivot','2 sets of 4 per pivot(16 total each set)'],
               ['Wall sit','2 sets of 1 minute']]
        r=9;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(tue3,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(tue3,text='.').grid(row=14,column=0,sticky=W)
        lb24=Label(tue3,text='Cool Down:').grid(row=15,column=0)
        list3=[['Toe touches on floor(legs spread)','2 sets of 20 sec./leg'],['Butterfly stretches','2 sets of 20 sec'],
               ['Knee hugs(on floor)','2 sets of 15 sec./leg'],['Calf Streches','2 sets of 10 sec./leg']]
        r=16;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(tue3,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(tue3,text='<',height=1,width=2,padx=10,pady=10,command=advanced)
        back.place(x=0,y=0)

    def thursday3():
        thu3=Frame(root)
        thu3.place(x=0,y=0,width=2000,height=1000)
        
        loc='Thursday3.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=thu3)
        label = Label(thu3, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=22, columnspan=5)
        
        lb1=Label(thu3,text='THURSDAY:BACK').grid(row=0,column=0)
        lb2=Label(thu3,text='Warm up:').grid(row=1,column=0)
        list1=[['Side bends','10/side'],['Trunk Rotations(alternating directions)','10'],
               ['Supine bridge','10'],['Shoulder blade squeeze','8'],['Trunk twists','6/side']]
        r=2;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(thu3,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1 

        blank=Label(thu3,text='.').grid(row=7,column=0,sticky=W)
        lb13=Label(thu3,text='Exercises:').grid(row=8,column=0)
        list2=[['Australian pull-ups w/ 1-sec. hold','2 sets of 7'],['Supermans with i sec.hold','2 sets of 10'],
               ['Australian pull-ups w/ one sec. hold (mid back)','2 sets of 7'],['Reverse dolphin kicks','2 sets of 10'],
               ['Wide grip pull-ups','2 sets to failure']]
        r=9;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(thu3,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1

        blank=Label(thu3,text='.').grid(row=14,column=0,sticky=W)
        lb24=Label(thu3,text='Cool Down:').grid(row=15,column=0)
        list3=[['Entended leg stretch','2 sets of 10 sec./leg'],['Cat stretch','10'],
               ['Trunk twist & hold','3 sets of 5 sec./leg'],['Sitting twist & hold','3 sets of 5 sec./leg'],
               ['Shoulder blade squeeze','8']]
        r=18;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(thu3,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(thu3,text='<',height=1,width=2,padx=10,pady=10,command=advanced)
        back.place(x=0,y=0)
        
    def friday3():
        fri3=Frame(root)
        fri3.place(x=0,y=0,width=2000,height=1000)
        
        loc='Friday3.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=fri3)
        label = Label(fri3, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=22, columnspan=5)
        
        lb1=Label(fri3,text='FRIDAY:CORE').grid(row=0,column=0)
        lb2=Label(fri3,text='Warm up:').grid(row=1,column=0)
        list1=[['Standing arch','15 sec'],['Side bends','10/side'],['Cobra','15 sec']]
        r=2;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(fri3,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1 

        blank=Label(fri3,text='.').grid(row=5,column=0,sticky=W)
        lb9=Label(fri3,text='Exercises:').grid(row=6,column=0)
        lb10=Label(fri3,text='To be done in 3 rounds (no rest between exercises; one minute rest between rounds)').grid(row=7,column=0)
        list2=[['Mountain climbers','25 seconds'],['Alternating V-ups','25 seconds'],
               ['Planks with forward/backward lean','25 seconds'],
               ['Russian Twist','20/side'],['Crunchy Frogs','25 seconds']]
        r=8;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(fri3,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0:
                    c=1
                else :
                    c=0
            r+=1

        blank=Label(fri3,text='.').grid(row=13,column=0,sticky=W)
        lb21=Label(fri3,text='Cool Down:').grid(row=14,column=0)
        list3=[['Cobra stretch','20 seconds'],['Supine stretch','20 sec'],['Standing arch','20 sec']]
        r=18;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(fri3,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(fri3,text='<',height=1,width=2,padx=10,pady=10,command=advanced)
        back.place(x=0,y=0)

    def saturday3():
        sat3=Frame(root)
        sat3.place(x=0,y=0,width=2000,height=1000)
        
        loc='Saturday3.png'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((600,700),PIL.Image.LANCZOS), master=sat3)
        label = Label(sat3, image = photo)
        label.image = photo
        label.grid(row=0, column=10, rowspan=22, columnspan=5)
        
        lb1=Label(sat3,text='SATURDAY:SHOULDER AND BICEP').grid(row=0,column=1)
        lb2=Label(sat3,text='Warm up:').grid(row=1,column=0)
        list1=[['Standing arch','15 sec'],['Side bends','10/side'],['Cobra','15 sec']]
        r=2;c=0
        for i in range(3):
            for j in range(2):
                lb=Label(sat3,text=list1[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1 
        blank=Label(sat3,text='.').grid(row=7,column=0,sticky=W)
        lb11=Label(sat3,text='Exercises:').grid(row=8,column=0)
        list2=[['Elevated Pike push-ups','2 sets of 8'],['Australian chin-ups','2 sets of 10'],
               ['Sidelying bodyweight bicep curls','2 sets of 8/arm'],['Helicopter exercise','2 sets of 8/side'],
               ['Assisted chin-ups','2 sets to failure']]
        r=9;c=0
        for i in range(5):
            for j in range(2):
                lb=Label(sat3,text=list2[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        blank=Label(sat3,text='.').grid(row=14,column=0,sticky=W)
        lb24=Label(sat3,text='Cool Down:').grid(row=15,column=0)
        list3=[['Forearm stretch','2 sets of 3 sec./arm'],['Arm crosses','2 sets of 10 sec./arm'],
               ['Shoulder stretches on wall','5/arm'],['Behind the head bent elbow stretch','2 sets of 10 sec./arm']]
        r=18;c=0
        for i in range(4):
            for j in range(2):
                lb=Label(sat3,text=list3[i][j]).grid(row=r,column=c,sticky=W)
                if c == 0: c=1
                else :c=0
            r+=1
        back=Button(sat3,text='<',height=1,width=2,padx=10,pady=10,command=advanced)
        back.place(x=0,y=0)

    def advanced():
        adva=Frame(root)
        adva.place(x=0,y=0,width=2000,height=1000)
        
        loc='wpf.jpg'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((1490,850),PIL.Image.LANCZOS), master=adva)
        label = Label(adva, image = photo)
        label.image = photo
        label.grid(row=0, column=0, rowspan=20, columnspan=20)
        
        lb1=Label(adva,text='Welcome to your workout if you exercise regularly.',bg='goldenrod1').grid(row=1,column=3)
        lb3=Label(adva,text='**************',bg='goldenrod1').grid(row=2,column=3)
        mon=Button(adva,text='Monday',height=1,width=10,padx=10,pady=10,command=monday3).grid(row=3,column=3)
        tue=Button(adva,text='Tuesday',height=1,width=10,padx=10,pady=10,command=tuesday3).grid(row=4,column=3)
        wed=Label(adva,text='Wednesday: please relax today:)',bg='goldenrod1').grid(row=5,column=3)
        thu=Button(adva,text='Thursday',height=1,width=10,padx=10,pady=10,command=thursday3).grid(row=6,column=3)
        fri=Button(adva,text='Friday',height=1,width=10,padx=10,pady=10,command=friday3).grid(row=7,column=3)
        sat=Button(adva,text='Saturday',height=1,width=10,padx=10,pady=10,command=saturday3).grid(row=8,column=3)
        sun=Label(adva,text='Sunday: please relax today:)',bg='goldenrod1').grid(row=9,column=3)
        blank=Label(adva,text='********************',bg='goldenrod1').grid(row=10,column=3)
        back=Button(adva,text='<',height=1,width=2,padx=10,pady=10,command=lambda:raise_frame(workout))
        back.place(x=0,y=0)

    workout=Frame(root)
    workout.place(x=0,y=0,width=2000,height=1000)
        
    loc='wpf.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((1490,850),PIL.Image.LANCZOS))
    label = Label(workout, image = photo)
    label.image = photo
    label.grid(row=0, column=0, rowspan=20, columnspan=20)

    l1=Label(workout,text='Hello this is to help you with your weekly workouts!!',bg='goldenrod1').grid(row=0,column=2,columnspan=4)
    l2=Label(workout,text='Choose your level of physical strength to exercise:',bg='goldenrod1').grid(row=1,column=2,columnspan=4)
    begi=Button(workout,text='Beginner',height=1,width=10,padx=10,pady=10,command=beginner).grid(row=2,column=4)
    inter=Button(workout,text='Intermediate',height=1,width=10,padx=10,pady=10,command=intermediate).grid(row=3,column=4)
    adv=Button(workout,text='Advanced',height=1,width=10,padx=10,pady=10,command=advanced).grid(row=4,column=4)
    l3=Label(workout,text='Each day will contain some warm up and cool down exercise also.',bg='goldenrod1').grid(row=5,column=2,columnspan=5)
    back=Button(workout,text='<',height=1,width=2,padx=10,pady=10,command=homepg)
    back.place(x=0,y=0)

#function for bmi
global bmm
def bmii():
    bm=Frame(root)
    bm.place(x=0,y=0)
    global height,bmi,weight
    loc='bmibg1.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((1500,800),PIL.Image.LANCZOS))
    label = Label(bm, image = photo)
    label.image = photo
    label.grid(row=0, column=0, rowspan=16 , columnspan=29)

    loc='bmi-chart.png'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((650,450),PIL.Image.LANCZOS))
    label = Label(bm, image = photo)
    label.image = photo
    label.grid(row=0, column=7, rowspan=25 , columnspan=19)

    #labelfont = ('Trattatello', 40)
    labelfont = ('Tsukushi A Round Gothic', 40)
    widget = Label(bm, text='BMI CALCULATOR')
    widget.config(bg='turquoise',fg='black') 
    widget.config(font=labelfont)           
    #widget.config(height=2, width=30)       
    widget.place(x=550,y=3)

    w=Label(bm, text='Weight in kg: ',height=2,width=20,bg='coral')
    w.grid(row=4,column=3,padx=10,pady=10)
    weigh=Entry(bm,width=10)
    weigh.grid(row=4,column=5,padx=10,pady=10)

    h=Label(bm, text='Height in metres: ',height=2,width=20,bg='coral')
    h.grid(row=5,column=3,padx=10,pady=10)
    heigh=Entry(bm,width=10)
    heigh.grid(row=5,column=5,padx=10,pady=10)

    def com():
        be=Entry(bm)
        be.grid(row=9, column=5,padx=10,pady=10)
        be.delete(0,END)
        ce=Entry(bm)
        ce.grid(row=10, column=5,padx=10,pady=10)
        ce.delete(0,END)
        height =float(heigh.get())
        weight =float(weigh.get())
        bmi=round(weight/ (height**2),2)
        st=""
        if ( bmi < 16):
            st="severely underweight"

        elif ( bmi >= 16 and bmi < 18.5):
            st="underweight"

        elif ( bmi >= 18.5 and bmi < 25):
            st="Healthy"
        
        elif ( bmi >= 25 and bmi < 30):
            st="overweight"

        elif ( bmi >=30):
            st="severely overweight"

        b=Label(bm, text='Your Bmi is :  ',height=2,width=20,bg='coral')
        b.grid(row=9,column=3)
        be.insert(0,str(bmi))
        comment=Label(bm, text="Category",height=2,width=20,bg='coral')
        comment.grid(row=10,column=3)
        ce.insert(0,st)
        if bmi<=10 or bmi>=48:
            def countdown(count):
                if count > 0:
                    root.after(1000, countdown, count-1)
                elif count == 0:
                    label.destroy()
            label = Label(bm,text="Enter Valid Height and Weight", anchor=CENTER, font=('Calibri', 10))
            label.grid(row=6,column=5,padx=10,pady=10)
            countdown(5)
            label.pack_forget()

    bsubb=Button(bm,text="Submit",height=1,width=10,padx=10,pady=10, command=com,bg='coral')
    bsubb.grid(row=7,column=4)
    back=Button(bm,text='<',height=1,width=2,padx=10,pady=10,command=homepg)
    back.place(x=0,y=0)

#function for home page screen buttons
def homepg():
    hp=Frame(root)
    hp.place(x=0, y=0, width=2000,height=1000)
    
    loc='final.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((1490,850),PIL.Image.LANCZOS), master=hp)
    label = Label(hp, image = photo)
    label.image = photo
    label.place(x=0,y=0)

    Label(hp,text='',bg='white smoke',height=5,width=200)
    
    labelfont = ('Trattatello',48)
    w = Label(hp,text='REJUWEL',bg='white smoke',fg='dark turquoise')
    w.config(font = labelfont)
    w.place(x=620,y=0)
    
    b4 = Button(hp,text="My Profile",height=2,width=20,padx=10,pady=10,command=profilemy)#,bg='powder blue')
    b4.place(x=160,y=160)
    b5 = Button(hp,text="Calorie counter",height=2,width=20,padx=10,pady=10,command=cal)#,bg='plum3')
    b5.place(x=160,y=260)
    b6 = Button(hp,text='BMI calculator',height=2,width=20,padx=10,pady=10,command=bmii)#,bg='powder blue')
    b6.place(x=160,y=360)
    b7 = Button(hp,text='Diet Chart',height=2,width=20,padx=10,pady=10,command=dietplan)#,bg='plum3')
    b7.place(x=160,y=460)
    b8 = Button(hp,text='Workout Plan',height=2,width=20,padx=10,pady=10,command=workout)#,bg='powder blue')
    b8.place(x=160,y=560)
    b9 = Button(hp,text='Sign out',height=2,width=20,padx=10,pady=10,command=main)#,bg='RosyBrown1')
    b9.place(x=160,y=660)
    
    loc='logo.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((120,80),PIL.Image.LANCZOS), master=hp)
    label = Label(hp, image = photo)
    label.image = photo
    label.place(x=0,y=0)

    l=[1,2,3,4,5,6]
    def update_clock():
        now=time.strftime("%H:%M:%S")
        hp.after(4000, update_clock)
    def update_pic():
        num=l[0]
        loc=''
        loc+= str(num)
        loc+='.jpg'
        image = PIL.Image.open(loc)
        photo = ImageTk.PhotoImage(image.resize((750, 500),PIL.Image.LANCZOS))
        label = Label(hp, image = photo)
        label.image = photo
        label.place(x=530,y=180)
        l.append(l.pop(0))
        hp.after(3000,update_pic)
    update_clock()
    update_pic()
    def pic_right():
       num=l[0]
       loc=''
       loc+= str(num)
       loc+='.jpg'
       image = PIL.Image.open(loc)
       photo = ImageTk.PhotoImage(image.resize((750, 500),PIL.Image.LANCZOS))
       label = Label(hp, image = photo)
       label.image = photo
       label.place(x=530,y=180)
    def pic_left():
       num=l[0]
       l.insert(0,l.pop())
       loc=''
       loc+= str(num)
       loc+='.jpg'
       image = PIL.Image.open(loc)
       photo = ImageTk.PhotoImage(image.resize((750, 500),PIL.Image.LANCZOS))
       label = Label(hp, image = photo)
       label.image = photo
       label.place(x=530,y=180)
       
    '''image = PIL.Image.open(r"logo.jpg")
    photo=ImageTk.PhotoImage(image.resize((20, 10),PIL.Image.LANCZOS))
    b4=Button(hp, text = '', image = photo, compound = LEFT, command=pic_left) 
    b4.grid(row=4, column=1, sticky="E")
    image1 = PIL.Image.open(r"logo.jpg")
    photo1=ImageTk.PhotoImage(image1.resize((20, 10),PIL.Image.LANCZOS))
    b5=Button(hp, text = '', image = photo1, compound = RIGHT, command=pic_right) 
    b5.grid(row=4, column=3, sticky="W")'''

#function for signing in
username=StringVar()
password=StringVar()
def find():
    try:
        ausername=username.get()
        apassword=password.get()
        search=0
        with open('login.csv','r',newline='') as csvfile:
            reader=csv.reader(csvfile)
            while True:
                for row in reader:     
                    if ausername==row[0] and apassword== row[4]:
                        search=1    
                        homepg()
                        break
                if search == 0:
                    if(ausername=='' or apassword==''):
                        mb.showerror('Error!',' Enter details to sign in')
                        username.set('')
                        password.set('')
                    
                    else:
                        mb.showerror('Error','Incorrect Details Entered')
                        break
                else:
                    break
    except FileNotFoundError:
        mb.showinfo('Error','Sign Up First')

def reset():
    username.set('')
    password.set('')

def helping():
    mb.showinfo('Sign In','Enter your username and password')

def signin():
    insign=Frame(root)
    insign.place(x=0,y=0,width=2000,height=1000)

    loc='final.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((1490,850),PIL.Image.LANCZOS),master=insign)
    label = Label(insign, image = photo)
    label.image = photo
    label.grid(row=0, column=0, rowspan=20, columnspan=20)

    loc='logo.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((300,200),PIL.Image.LANCZOS), master=insign)
    label = Label(insign, image = photo)
    label.image = photo
    label.place(x=560,y=275)

    lblUsername=Label(insign,text='Username:',fg='black',bg='white smoke').place(x=580,y=500)
    entryusername=Entry(insign,textvariable=username,width=10).place(x=680,y=500)

    lblPassword=Label(insign,text='Password:',fg='black',bg='white smoke').place(x=580,y=550)
    entryPassword=Entry(insign,textvariable=password,width=10,show='*').place(x=680,y=550)

    reset()

    find_button=Button(insign,text='Submit',height=1,width=10,padx=10,pady=10,command=find).place(x=670,y=600)
    reset_button=Button(insign,text='Clear',height=1,width=10,padx=10,pady=10,command=reset).place(x=350,y=600)
    help_button=Button(insign,text='Help',height=1,width=10,padx=10,pady=10,command=helping).place(x=1000,y=600)

    back=Button(insign,text='<',height=1,width=3,padx=10,pady=10,command=main)
    back.place(x=0,y=0)

#function for profile
def profilemy():
    profile=Tk()
    profile.title('REJUWEL - PROFILE')
    profile.geometry("464x646")
    
    loc='bgpro.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((464,646),PIL.Image.LANCZOS),master=profile)
    label = Label(profile, image = photo)
    label.image = photo
    label.grid(row=0, column=0, rowspan=20, columnspan=20)

    def destroy():
        profile.destroy()

    l1=Label(profile,text='My Profile',height=1,width=10,bg='light sea green',fg='white')
    l1.place(x=200,y=170)

    back=Button(profile,text='<',height=1,width=3,padx=10,pady=10,command=destroy)
    back.place(x=0,y=0)
    
    def dest():
        profile.destroy()
        
    ausername=username.get()
    apassword=password.get()
    with open('login.csv','r',newline='') as csvfile:
        reader=csv.reader(csvfile)
        flag=0
        while flag==0:
            for row in reader:     
                if ausername==row[0] and apassword== row[4]:
                    ll=[]
                    for i in range(10):
                        ll.append(row[i])
                    lun=ll[0]
                    lfn=ll[1]
                    lln=ll[2]
                    la=ll[5]
                    lw=ll[6]
                    lh=ll[7]
                    lg=ll[8]
                    lb=ll[9]
                    
                    Label(profile,text='Username:',height=1,width=10,bg='sienna1',fg='white').place(x=105,y=220)
                    Label(profile,text=lun,height=1,width=25,bg='gold',fg='RoyalBlue1').place(x=210,y=220)
                    
                    Label(profile,text='First name:',height=1,width=10,bg='sienna1',fg='white').place(x=105,y=255)
                    Label(profile,text=lfn,height=1,width=25,bg='gold',fg='RoyalBlue1').place(x=210,y=255)
                    
                    Label(profile,text='Last name:',height=1,width=10,bg='sienna1',fg='white').place(x=105,y=290)
                    Label(profile,text=lln,height=1,width=25,bg='gold',fg='RoyalBlue1').place(x=210,y=290)

                    Label(profile,text='Email Id:',height=1,width=10,bg='sienna1',fg='white').place(x=105,y=325)
                    Label(profile,text=ll[3],height=1,width=25,bg='gold',fg='RoyalBlue1').place(x=210,y=325)

                    Label(profile,text='Age (in years):',height=1,width=10,bg='sienna1',fg='white').place(x=105,y=360)
                    Label(profile,text=la,height=1,width=25,bg='gold',fg='RoyalBlue1').place(x=210,y=360)
                    
                    Label(profile,text='Weight (in kg):',height=1,width=10,bg='sienna1',fg='white').place(x=105,y=395)
                    Label(profile,text=lw,height=1,width=25,bg='gold',fg='RoyalBlue1').place(x=210,y=395)
                    
                    Label(profile,text='Height (in cm):',height=1,width=10,bg='sienna1',fg='white').place(x=105,y=430)
                    Label(profile,text=lh,height=1,width=25,bg='gold',fg='RoyalBlue1').place(x=210,y=430)
                    
                    Label(profile,text='Gender:',height=1,width=10,bg='sienna1',fg='white').place(x=105,y=465)
                    if lg == '1':
                        Label(profile,text="Male",height=1,width=25,bg='gold',fg='RoyalBlue1').place(x=210,y=465)

                    else:
                        Label(profile,text="Female",height=1,width=25,bg='gold',fg='RoyalBlue1').place(x=210,y=465)
                        
                    Label(profile,text='BMI:',height=1,width=10,bg='sienna1',fg='white').place(x=105,y=500)
                    Label(profile,text=lb,height=1,width=25,bg='gold',fg='RoyalBlue1').place(x=210,y=500)
                    
                    flag=1
                    break
                break
    def savereport():
        if countttt[0]==0 or countttt[1]==0 or countttt[2]==0:
            mb.showinfo('Invalid','Go to Calorie Counter, Deficiency Identifier and Special Foods To Consume First')
            dest()
            
        else:           
            filename='Report_'+username.get()+str(date.today())+'.txt'
            rrrr.append(filename)
            
            with open(filename, "w") as file:
                with open("login.csv",'r') as csvfile:
                    c_reader=csv.reader(csvfile)
                    cccc=[]
                    auser=username.get()
                    apass=password.get()
                    for i in c_reader:
                        if i[0]==auser and i[4]==apass:
                            cccc=i.copy()
                file.write('\n'+'Username : '+cccc[0])
                file.write('\n'+'Firstname : '+cccc[1])
                file.write('\n'+'Surname : '+cccc[2])
                file.write('\n'+'Email Address : '+cccc[3])
                file.write('\n'+'Age (in yrs) : '+cccc[5])
                file.write('\n'+'Weight (in kg) : '+cccc[6])
                file.write('\n'+'Height (in cm) : '+cccc[7])
                if cccc[8]==2:
                    file.write('\n'+'Gender : '+'Female')
                else:
                    file.write('\n'+'Gender : '+'Female') 
                file.write('\n'+'BMI : '+cccc[9])
                file.write('\n'+'\n')
                
                with open("caloriecounter.txt",'r') as file1:
                    content=''
                    for line in file1:
                        data = line.strip()
                        content+=data.ljust(300, ' ')
                        content+='\n'
                    file.write(content)
                file.write('\n'+'\n')
                with open("deficiency.txt",'r') as file1:
                    content=file1.read()
                    file.write(content)
                file.write('\n'+'\n')
                with open("foodconsume.txt",'r') as file1:
                    content=file1.read()
                    file.write(content)    
                file.write('\n'+'\n')
                
            
            with open('checkocheck.txt','a') as filee:
                filee.write('b')
            mb.showinfo('Report Saved','You can now send Report')
            
    def sendreport():
        with open('checkocheck.txt','r') as filee:
            aaaa=filee.read()
        if aaaa=='a':
            mb.showinfo('Invalid','Save Report First')
        else:
            with open("login.csv",'r') as csvfile:
                c_reader=csv.reader(csvfile)
                cccc=[]
                auser=username.get()
                apass=password.get()
                for i in c_reader:
                    if i[0]==auser and i[4]==apass:
                        cccc=i.copy()
            name=username.get()
            amailid=cccc[3]
            filename='Report_'+username.get()+str(date.today())+'.txt'
            sendimail.sending(name,amailid,filename)
            mb.showinfo('Report Sent Successfully','Please check your mail id for Daily Health Report')
    b=Button(profile, text="Save Report", height=2, width=10, bg='linen', command=savereport).place(x=135, y=550)
    b2=Button(profile, text="Send Report", height=2, width=10, bg='linen', command=sendreport).place(x=265, y=550)
                   
#function for signing up
username=StringVar()
firstname=StringVar()
surname=StringVar()
password=StringVar()
confirm_password=StringVar()
gender_choice=IntVar()
age=StringVar()
weight=StringVar()
height=StringVar()
mailid=StringVar()
global bmi
def store_value():
    ausername=username.get()
    global afirstname
    afirstname=firstname.get()
    asurname=surname.get()
    apassword=password.get()
    aconfirm_password=confirm_password.get()
    aage=age.get()
    aweight=weight.get()
    aheight=height.get()
    global amailid
    amailid=mailid.get()
    agender_choice=gender_choice.get()
    if(ausername=='' or afirstname=='' or asurname=='' or amailid=='' or apassword=='' or aconfirm_password=='' or aage=='' or aweight=='' or aheight==''):
        mb.showerror('Error!',' Missing Details')
        username.set('')
        firstname.set('')
        surname.set('')
        password.set('')
        confirm_password.set('')
        age.set('')
        weight.set('')
        height.set('')
        mailid.set('')
    elif(apassword!=aconfirm_password):
        mb.showerror('Error','Password does not match')
    elif(agender_choice!=2 and agender_choice!=1):
        mb.showerror('Error!', 'Gender must be selected')
        username.set('')
        firstname.set('')
        surname.set('')
        password.set('')
        confirm_password.set('')
        age.set('')
        weight.set('')
        height.set('')
        mailid.set('')
    else:
        result= mb.askquestion('Submit','You are about to enter the following data\n'+ausername+'\n'+afirstname+'\n'+asurname+'\n'+amailid+'\n'+apassword+'\n'+aage+'\n'+aweight+'\n'+aheight)
        if(result=='yes'):
            bmi=round(int(aweight)/ ((float(aheight)/100)**2),2)
            with open('login.csv','a',newline='') as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow([ausername,afirstname,asurname,amailid,apassword,aage,aweight,aheight,agender_choice,bmi])
       
            homepg()
        else:
            username.set('')
            firstname.set('')
            surname.set('')
            password.set('')
            confirm_password.set('')
            age.set('')
            weight.set('')
            height.set('')
            mailid.set('')
def clear_info():
    username.set('')
    firstname.set('')
    surname.set('')
    password.set('')
    confirm_password.set('')
    age.set('')
    weight.set('')
    height.set('')
    mailid.set('')

def helping():
    mb.showinfo('Information','Enter all your personal information to login')
    
def signup():
    upsign=Frame(root)
    upsign.place(x=0,y=0,width=2000,height=1000)

    loc='final.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((1490,850),PIL.Image.LANCZOS),master=upsign )
    label = Label(upsign, image = photo)
    label.image = photo
    label.grid(row=0, column=0, rowspan=20, columnspan=20)

    loc='logo.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((300,200),PIL.Image.LANCZOS), master=root)
    label = Label(root, image = photo)
    label.image = photo
    label.place(x=560,y=275)

    lblUsername=Label(upsign,text='Username: ',fg='black',bg='white smoke').place(x=250,y=500)
    entryusername=Entry(upsign,textvariable=username,width=10).place(x=350,y=500)

    lblFirstName=Label(upsign,text='First Name: ',fg='black',bg='white smoke').place(x=250,y=550)
    entryfirstName=Entry(upsign,textvariable=firstname,width=10).place(x=350,y=550)

    lblLastName=Label(upsign,text='Last Name: ',fg='black',bg='white smoke').place(x=250,y=600)
    entryLastName=Entry(upsign,textvariable=surname,width=10).place(x=350,y=600)

    lblemail=Label(upsign,text='Email Id (valid): ',fg='black',bg='white smoke').place(x=480,y=500)
    entryemail=Entry(upsign,textvariable=mailid,width=30).place(x=610,y=500)
    
    lblage=Label(upsign,text='Age(in years): ',fg='black',bg='white smoke').place(x=250,y=650)
    entryage=Entry(upsign,textvariable=age,width=10).place(x=350,y=650)

    lblPassword=Label(upsign,text='Password: ',fg='black',bg='white smoke').place(x=940,y=500)
    entryPassword=Entry(upsign,textvariable=password,width=10,show='*').place(x=1100,y=500)

    lblConfirmPassword=Label(upsign,text='Confirm Password: ',fg='black',bg='white smoke').place(x=940,y=550)
    entryConfirmPassword=Entry(upsign,textvariable=confirm_password,width=10,show='*').place(x=1100,y=550)

    lblweight=Label(upsign,text='Weight(in kg): ',fg='black',bg='white smoke').place(x=940,y=600)
    entryweight=Entry(upsign,textvariable=weight,width=10).place(x=1100,y=600)

    lblheight=Label(upsign,text='Height(in cms): ',fg='black',bg='white smoke').place(x=940,y=650)
    entryheight=Entry(upsign,textvariable=height,width=10).place(x=1100,y=650)

    lblGender=Label(upsign,text='Gender',fg='black',bg='white smoke').place(x=670,y=540)
    radiobutton1=Radiobutton(upsign,text='Male',fg='black',bg='white smoke',variable=gender_choice,value=1).place(x=670,y=580)
    radiobutton2=Radiobutton(upsign,text='Female',fg='black',bg='white smoke',variable=gender_choice,value=2).place(x=670,y=630)

    clear_info()
    
    submit_button=Button(upsign,text='Submit',height=1,width=10,padx=10,pady=10,command=store_value).place(x=670,y=700)
    clear_button=Button(upsign,text='Clear',height=1,width=10,padx=10,pady=10,command=clear_info).place(x=350,y=700)
    help_button=Button(upsign,text='Help',height=1,width=10,padx=10,pady=10,command=helping).place(x=1000,y=700)

    back=Button(upsign,text='<',height=1,width=3,padx=10,pady=10,command=main)
    back.place(x=0,y=0)

#function for main window
def main():
    mainwindow=Frame(root)
    mainwindow.place(x=0,y=0,width=2000,height=1000)

    #commands for putting logo
    loc='final.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((1490,850),PIL.Image.LANCZOS), master=mainwindow)
    label1 = Label(mainwindow, image = photo)
    label1.image = photo
    label1.place(x=0,y=0)

    loc='logo.jpg'
    image = PIL.Image.open(loc)
    photo = ImageTk.PhotoImage(image.resize((300,200),PIL.Image.LANCZOS), master=mainwindow)
    label = Label(mainwindow, image = photo)
    label.image = photo
    label.place(x=560,y=275)

    #buttons for sign in and sign up
    b1=Button(mainwindow,text="Sign in",height=1,width=10,padx=10,pady=10,command=signin)
    b1.place(x=655,y=500)
    b2=Button(mainwindow,text="Sign up",height=1,width=10,padx=10,pady=10,command=signup)
    b2.place(x=655,y=550)

main()

root.mainloop()
