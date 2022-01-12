# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:04:30 2021

@author: Prashant Kumar
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("pima-indians-diabetes.csv")
#print(df.head())
data = df.drop(['class'], axis = 1)
#print(data.head())
#_______________Getting the Mean, median, mode, minimum, maximum and standard deviation of BMI
print("Mean of BMI is %1.2f"%(data['BMI'].mean()))
print("Mode of BMI is %1.2f"%(data['BMI'].mode()))
print("Median of BMI is %1.2f"%(data['BMI'].median()))
print("Maximum of BMI is %1.2f"%(data['BMI'].max()))
print("Minimum of BMI is %1.2f"%(data['BMI'].min()))


#_________________Code for the scatter plot between age and all the other attribute
attributesfr = ['pregs', 'plas', 'pres', 'skin','BMI', 'pedi']#ASSIGNING OUR ATTRIBUTES IN A LIST 
fig,axs=plt.subplots(2,3,figsize=(16,12))  #PLOTTING  SUBPLOTS FOR OUR REQUIRED ATTRIBUTE
a=0;b=0
for i in attributesfr: #LOOP IN ATTRIBUTES1 FOR OBTAINING EACH AND EVERY ATTRIBUTES FROM THE LIST
   
    axs[a][b].set_title(i.capitalize()+' vs Age')
    axs[a][b].scatter(data['Age'],data[i],color='blue') #USING SCATTER PLOT FROM PANDAS LIBRARY
    axs[a][b].set_xlabel('Age')
    axs[a][b].set_ylabel(i.capitalize())
    b+=1
    if b==3:
        a+=1;b=0
    
plt.show()



#_______________________The value of correlation coefficient
#Correlation coefficent
for i in attributesfr: 
     corr_age = np.corrcoef(data['Age'],data[i]) 
     print("correlation coefficient between Age and ",i,": %1.2f"%(corr_age[0,1]))

#_________________________The histogram for the attributes ‘preg’ and ‘skin’ 
df2 = pd.DataFrame({'preg': data['pregs'],'skin':data['skin']})
print(df2.columns)
plt2 = df2.hist(bins = 8)
print(plt2) 

df3 = df.groupby(['pregs','class'])
print(df3.first())

#___________________________The histogram of attribute ‘preg’ for each of the 2 classes individually
df['pregs'].hist(by=df['class'])
plt.show()

#___________________________The boxplot for all the attribute excluding ‘class’ 
bxplot = data.boxplot(attributesfr)
print(bxplot)
