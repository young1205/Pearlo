import numpy as np
import matplotlib as plt
import pylab as pl
from matplotlib.patches import Circle, Rectangle, Polygon, Arrow, FancyArrow

print 'Hello welcome to Perlo'
depts = raw_input('For the first step enter the departments involved in hiring seperated by spaces. \n For example: HR Engineering Marketing : ')

deptlist = depts.split()
print 'The departments you entered are: '  
print deptlist

firstcontact = raw_input('Which department screens the applicant pool? ')

for jix in range(0, len(deptlist)):
    if firstcontact == deptlist[jix]:
        fcid = jix


ysize = 4.0/len(deptlist) 
################ FIRST PLOT

fig = pl.figure(figsize=(15, 6), facecolor='w')
ax = pl.axes((0, 0, 1, 1), xticks=[], yticks=[], frameon=False)
ax.set_xlim(0, 9)
ax.set_ylim(0, 6)

bbox_args = dict(boxstyle="round", fc="0.8")
arrow_args = dict(arrowstyle="->")

for jix in range(0, len(deptlist)):       
    pl.text(1.0, ysize*jix+1.0 ,str(deptlist[jix]), ha='center', va='center', fontsize=14)
    ax.add_patch(Rectangle((0.2, ysize*jix+0.2), 6.6 , 0.01, fc='#88CCFF'))

ax.add_patch(Rectangle((0.2, ysize*(len(deptlist))+0.2), 6.6 , 0.01, fc='#88CCFF'))

ax.add_patch(Rectangle((2.6, ysize*fcid+0.7), 0.8, 0.6, fc='#88CCFF'))
pl.text(3.0, ysize*fcid+1.0 ,'First Screen', ha='center', va='center', fontsize=14)  

#FancyArrow(2.3, 4.6, 0.35, 0, width=0.25, head_width=0.5, head_length=0.2),
pl.show()

step2 = raw_input('What is the next step? ')
