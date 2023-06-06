

import tkinter as tk
import itertools
"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map2.txt')
fr=f.read()
frs=fr.split('\n')
print(frs)


maze=[]


for k in range(0,11):
    for (i,j) in itertools.zip_longest(frs[k],range(len(frs[k]))):
        if i=='0':
            maze.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#0000bb'))
        if i=='1':
            maze.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#00ff00'))
        if i=='2':




            maze.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#013220'))
        if i=='3':
            maze.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#90ee90'))
        if i=='4':
            maze.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#964b00'))
        if i=='5':
            maze.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#005249'))
        if i=='6':
            maze.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#808080'))
        else:
            pass


w.mainloop()
