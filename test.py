import re
import numpy as np
import pandas as pd

print("Please enter your schema :")
body = str(input())
RelNames = re.split(r',\s*(?![^()]*\))', body)
cars = []
attn = []
names =[]
for j in RelNames:
    cars.append(j)
for element in cars:
    names.append(re.sub(" *\\(.*", "", element))
    attn.append((element[element.find("(") + 1:element.find(")")]).split(','))
print("Relation Tables from your schema are:"+"\n")
for i in range(len(names)):
    print(str(i+1) + " " + "->" +" " + str(names[i]) + "\n" + "with columns" + " "+ str(attn[i]) +"\n")

print("Give your primary key like id->actor,hour for both of tables")
print("For " +":" +" "+ str(names[0]))
primary1=str(input())
print("\n" + "For " +":" +" "+ str(names[1]))
primary2 = str(input())

names[0] = [[101, 'Alex', 10], [102, 'Bob', 12], [103, 'Clarke', 13], [101, 'Alex', 7] ,[102, 'Bob', 12],  [103, 'Clarke', 13] ,  [104, 'Mary', 13]]

names[1] = [[101,"Village" , "Rentis"],[102,"Athinaion","Ampelokipoi"],[101,"Athinaion","Ampelokipoi"]]
#names[0] = [[101, 'Alex', 12], [102, 'Alex', 14], [103, 'Clarke', 13]]
count=0
count1=0

prdepen = re.split("->", primary1)
prdepen0 = prdepen[0].split(',')
prdepen1 = prdepen[1].split(',')
df1 = pd.DataFrame(names[0], columns=['id', 'actor', 'hour'])
for i in range(len(prdepen0)):
    gk = df1.groupby([prdepen0[i]])
for group_name, df_group in gk:
    for row_indec, row in df_group.iterrows():
        for j in range(len(prdepen1)):
           if row[prdepen1[j]] != df_group.iloc[0][prdepen1[j]]:
               count = count+1
if count >= 1:
        print("Not valid primary key"+"\n")


prdepenb = re.split("->", primary2)
prdepen0b = prdepenb[0].split(',')
prdepen1b = prdepenb[1].split(',')
df2 = pd.DataFrame(names[1], columns=['movid', 'name','region'])
for i in range(len(prdepen0b)):
    gk = df2.groupby([prdepen0b[i]])
for group_name, df_group in gk:
    for row_indec, row in df_group.iterrows():
        for j in range(len(prdepen1b)):
           if row[prdepen1b[j]] != df_group.iloc[0][prdepen1b[j]]:
               count1 = count1+1
if count1 >= 1:
        print("Not valid primary key"+"\n")



print( "Type  2.Foreign key 3.Other Functional Depedency")

depend = str(input())

#---------------------------------FOREIGN KEY-------------------------------------------
if depend == "2":
    countf=0;
    print(" Type your foreign key:")
    foreign = str(input())
    foreigntable=[]
    print(" It references to where:")
    refer = str(input())
    refertable=[]
    #result =  df2.movid.isin(df1.id)
    #df2['match'] = np.where(df2.movid == df1.id, 'True', 'False')

    for row_indec, row in df2.iterrows():
        foreigntable.append(row[foreign])

    for row_indec, row in df1.iterrows():
        refertable.append(row[refer])

    for i in range(len(foreigntable)):
        if foreigntable[i] in refertable:
            countf = countf + 1

    if countf==len(foreigntable):
        print("Valid Foreign key ")
    else:
        print("Not Valid Foreign key ")


#-------------------------OTHER FUNCTIONAL DEPEDENCIES--------------------------------
elif depend == "3":
    print("Give the Functional Depedency you want")
    #Movies(id, actor, hour), Cinema(movid, name)
    prdk = str(input())
    prd = re.split("->", prdk)
    prd1 = prd[0].split(',')

    prd2 = prd[1].split(',')

    print("Type Table 1.Movies Table 2.Cinema")
    answer = str(input())
    countd1=0
    countd2=0
    if answer == "1":

      df1 = pd.DataFrame(names[0], columns=['id','actor','hour'])
      for i in range(len(prd1)):
         gk = df1.groupby([prd1[i]])
         for group_name, df_group in gk:
            for row_indec, row in df_group.iterrows():
               for j in range(len(prd2)):
                 if row[prd2[j]] != df_group.iloc[0][prd2[j]]:
                    countd1 = countd1 + 1
      if countd1 >= 1:
        print("Not valid" + "\n")

    if answer == "2":

       df2 = pd.DataFrame(names[1], columns=['movid','name','region'])
       for i in range(len(prd1)):
          gk = df2.groupby([prd1[i]])
          for group_name, df_group in gk:
            for row_indec, row in df_group.iterrows():
                for j in range(len(prd2)):
                    if row[prd2[j]] != df_group.iloc[0][prd2[j]]:
                          countd2= countd2 + 1
       if countd2 >= 1:
            print("Not valid" + "\n")




















