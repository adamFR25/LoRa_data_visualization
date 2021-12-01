from tkinter import *
from tkinter import ttk
from tkhtmlview import *
import time
import sys
import lorthon
import json
import threading
from matplotlib import pyplot as plt
from matplotlib.image import imread
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import pandas as pd
from PIL import Image, ImageDraw


root = Tk()
root.protocol(quit)
root.title('PKPT UNDIKA')
root.geometry("900x400")

def quit():
    root.quit()

options = [
    "Node 1",
    "Node 2",
    "Node 3",
]


# Monitor DATA
monitor = tk.scrolledtext.ScrolledText(root, width=50, height=20)
monitor.config(state = DISABLED)
monitor.pack(side = RIGHT, fill = BOTH, expand = True)


# combo box (node)
drop = ttk.Combobox(root, 
                            values=[
                                    "Node 1", 
                                    "Node 2",
                                    "Node 3",
                                    "View All",])
drop.current(0)              
drop.pack(padx=10)

root.bind("1", lambda e : drop.current(0))
root.bind("2", lambda e : drop.current(1))
root.bind("3", lambda e : drop.current(2))
root.bind("4", lambda e : drop.current(3))
drop.pack(padx = 10)
#---drop.grid(row = 0,column = 0,columnspan = 1)

        
# check Button 
var = IntVar()
autoscroll = tk.Checkbutton(root, text= "Auto Scroll", variable = var)
autoscroll.select()
autoscroll.pack(padx = 10)

root.bind("a", lambda e : cb_stats(var.get()))

def cb_stats (x):
    if  x == 1:
        autoscroll.deselect()
    
    else:
        autoscroll.select()



link = "https://youtube.com"
link1 = "https://google.com"
link2 = "https://dota2.com" 


def callback(event):
        index = event.widget.index("@%s,%s" % (event.x, event.y))
        tag_indices = list(event.widget.tag_ranges('tag'))

        for start, end in zip(tag_indices[0::2], tag_indices[1::2]):
            if event.widget.compare(start, '<=', index) and event.widget.compare(index, '<', end):                
                if drop.get() == "Node 1":
                    #webbrowser.open_new_tab(event.widget.get(start, end))
                    getnode = event.widget.get(start, end)
                    putnode = getnode.split(",")
                    plt.style.use('seaborn')

                    img = imread('map1.png')
                    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Node 1',
                                        markerfacecolor='r', markersize=10),
									Line2D([0], [0], marker='o', color='w', label='Node 2',
											markerfacecolor='g', markersize=10),
									Line2D([0], [0], marker='o', color='w', label='Node 3',
											markerfacecolor='y', markersize=10),]

					
                    fig, ax = plt.subplots()
                    ax.legend(handles=legend_elements, loc='upper left')

                    y = float(putnode[0])
                    x = float(putnode[1])
                    
                    #----rumah sukri-------
                    plt.imshow(img,zorder = 0,extent= [112.7221, 112.7354,-7.4556,-7.4453])
                    plt.ylim(-7.4556,-7.4453,)
                    plt.xlim(112.7221,112.7354)
                    plt.scatter(x,y, c='red')
                    
                    #----rumah adam--------
                    #plt.imshow(img,zorder = 0,extent= [112.67548, 112.68313,-7.44400,-7.43970])
                    #plt.ylim(-7.44400,-7.43970,)
                    #plt.xlim(112.67548,112.68313)
                    #plt.scatter(x,y, c='red')
                
                    plt.show()
                
                if drop.get() == "Node 2":
                    #webbrowser.open_new_tab(event.widget.get(start, end))
                    getnode = event.widget.get(start, end)
                    putnode = getnode.split(",")
                    plt.style.use('seaborn')

                    img = imread('map1.png')
                    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Node 1',
                                        markerfacecolor='r', markersize=10),
									Line2D([0], [0], marker='o', color='w', label='Node 2',
											markerfacecolor='g', markersize=10),
									Line2D([0], [0], marker='o', color='w', label='Node 3',
											markerfacecolor='y', markersize=10),]

					
                    fig, ax = plt.subplots()
                    ax.legend(handles=legend_elements, loc='upper left')

                    y = float(putnode[0])
                    x = float(putnode[1])
                    
                    #----rumah sukri-------
                    plt.imshow(img,zorder = 0,extent= [112.7221, 112.7354,-7.4556,-7.4453])
                    plt.ylim(-7.4556,-7.4453,)
                    plt.xlim(112.7221,112.7354)
                    plt.scatter(x,y, c='green')
                    
                    #----rumah adam--------
                    #plt.imshow(img,zorder = 0,extent= [112.67548, 112.68313,-7.44400,-7.43970])
                    #plt.ylim(-7.44400,-7.43970,)
                    #plt.xlim(112.67548,112.68313)
                    #plt.scatter(x,y, c='green')
                
                    plt.show()

                if drop.get() == "Node 3":
                    #webbrowser.open_new_tab(event.widget.get(start, end))
                    getnode = event.widget.get(start, end)
                    putnode = getnode.split(",")
                    plt.style.use('seaborn')

                    img = imread('map1.png')
                    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Node 1',
                                        markerfacecolor='r', markersize=10),
									Line2D([0], [0], marker='o', color='w', label='Node 2',
											markerfacecolor='g', markersize=10),
									Line2D([0], [0], marker='o', color='w', label='Node 3',
											markerfacecolor='y', markersize=10),]

					
                    fig, ax = plt.subplots()
                    ax.legend(handles=legend_elements, loc='upper left')

                    y = float(putnode[0])
                    x = float(putnode[1])
                    
                    #------rumah sukri-----
                    plt.imshow(img,zorder = 0,extent= [112.7221, 112.7354,-7.4556,-7.4453])
                    plt.ylim(-7.4556,-7.4453,)
                    plt.xlim(112.7221,112.7354)
                    plt.scatter(x,y, c='yellow')
                    
                    #----rumah adam--------
                    #plt.imshow(img,zorder = 0,extent= [112.67548, 112.68313,-7.44400,-7.43970])
                    #plt.ylim(-7.44400,-7.43970,)
                    #plt.xlim(112.67548,112.68313)
                    #plt.scatter(x,y, c='yellow')
                    
                
                    plt.show()
                    
                if drop.get() == "View All":
                    #webbrowser.open_new_tab(event.widget.get(start, end))
                    putnode1 = ''
                    putnode2 = ''
                    putnode3 = ''
                    if app.paket1 != '':
                        putnode1 = app.paket1[4:].split(",")
                        putx1 = putnode1[1]
                    if app.paket2 != '':
                        putnode2 = app.paket2[4:].split(",")
                        putx2 = putnode2[1]
                    if app.paket3 != '':
                        putnode3 = app.paket3[4:].split(",")
                        putx3 = putnode3[1]
                    
                    
                    
                    
                    
                    
                    plt.style.use('seaborn')

                    img = imread('map1.png')
                    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Node 1',
                                        markerfacecolor='r', markersize=10),
									Line2D([0], [0], marker='o', color='w', label='Node 2',
											markerfacecolor='g', markersize=10),
									Line2D([0], [0], marker='o', color='w', label='Node 3',
											markerfacecolor='y', markersize=10),]

					
                    fig, ax = plt.subplots()
                    ax.legend(handles=legend_elements, loc='upper left')
                    
                    y1 = ''
                    x1 = ''
                    y2 = ''
                    x2 = ''
                    y3 = ''
                    x3 = ''
                    
                    #----rumah sukri-----
                    plt.imshow(img,zorder = 0,extent= [112.7221, 112.7354,-7.4556,-7.4453])
                    plt.ylim(-7.4556,-7.4453,)
                    plt.xlim(112.7221,112.7354)
                    
                    #----rumah adam--------
                    #plt.imshow(img,zorder = 0,extent= [112.67548, 112.68313,-7.44400,-7.43970])
                    #plt.ylim(-7.44400,-7.43970,)
                    #plt.xlim(112.67548,112.68313)
                    
                    
                    if putnode1 != '':
                        y1 = float(putnode1[0])
                        x1 = float(putx1[0:10])
                        plt.scatter(x1,y1, c='red')
                
                    if putnode2 != '':
                        y2 = float(putnode2[0])
                        x2 = float(putx2[0:10])
                        plt.scatter(x2,y2, c='green')
                        
                    if putnode3 != '':
                        y3 = float(putnode3[0])
                        x3 = float(putx3[0:10])
                        plt.scatter(x3,y3, c='yellow')
                
                    plt.show()

def show_cursor(a):
        monitor.config(cursor="hand2")   

def normal_cursor(a):
        monitor.config(cursor='')    

class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.paket1 = ''
        self.paket2 = ''
        self.paket3 = ''
        self.start()
    
    def all_quit(self):
        app.quit()
    
    
    def run (self):
        if (lorthon.py_LoRaInit("global_conf.json") == 0):
            while True:
                value = json.loads(lorthon.py_LoRaRx())
                x = ''
                x1 = 'FF01-7.450673,112.728694'
                x2 = 'FF02-7.450701,112.728765'
                x3 = 'FF03-7.450521,112.728274'
                self.paket1 = x1
                self.paket2 = x2
                self.paket3 = x3
                for data in value['packets']:
                    print (data['payload'])
                    x = bytes.fromhex(data['payload']).decode('utf-8','ignore')
                    
                    #print (x)
                    if x1[2:4] == '01':
                       self.paket1 = x
                       #print(self.paket1)
                    if x2[2:4] == '02':
                       self.paket2 = x
                    if x3[2:4] == '03':
                       self.paket3 = x
                display_data()
                time.sleep(1)

    
            
		
		
        

app = App()

def display_data():
    
    ch = '1234567890-,.'
    fixedgps1 = ''
    fixedgps2 = ''
    fixedgps3 = ''
    A = len(app.paket1)
    B = len(app.paket2)
    C = len(app.paket3)
    for i in range(A):
        if app.paket1[i] not in ch:
            print(app.paket1[i] in ch)

        else:
            print(app.paket1[i] in ch)
            fixedgps1 = fixedgps1 + app.paket1[i]
            
    for i in range(B):
        if app.paket2[i] not in ch:
            print(app.paket2[i] in ch)

        else:
            print(app.paket2[i] in ch)
            fixedgps2 = fixedgps2 + app.paket2[i]
            
    for i in range(C):
        if app.paket3[i] not in ch:
            print(app.paket3[i] in ch)

        else:
            print(app.paket3[i] in ch)
            fixedgps3 = fixedgps3 + app.paket3[i]
    
	    
    start_time = time.time()
    monitor.tag_config("tag",foreground = "blue")
    monitor.tag_config("tag1",foreground = "green")
    monitor.tag_config("tag2",foreground = "orange")
    monitor.tag_config("tag3",foreground = "red")
    monitor.config(state = NORMAL)
    hour = time.strftime("%H") 
    minute = time.strftime("%M")
    second = time.strftime("%S")
    if drop.get() == "Node 1" and len(fixedgps1[2:]) <= 20 :
        if fixedgps1[:2] == '01':
            monitor.insert(tk.END, "[")
            monitor.insert(tk.END, hour, "tag1")
            monitor.insert(tk.END, ":")
            monitor.insert(tk.END, minute, "tag1")
            monitor.insert(tk.END, ":")
            monitor.insert(tk.END, second, "tag1")
            monitor.insert(tk.END, "] ")
            monitor.insert(tk.END, "Node 1 : " )
            monitor.tag_bind("tag", "<Button-1>", callback)
            monitor.tag_bind("tag", "<Enter>", show_cursor)
            monitor.tag_bind("tag", "<Leave>", normal_cursor)
            monitor.insert(tk.END, fixedgps1[2:], "tag")
            monitor.insert(tk.END, " (executed : %.2f second) " %(time.time() - start_time),"tag2")
            monitor.insert(tk.END,"\n")
            
    if drop.get() == "Node 2"  and len(fixedgps2[2:]) <= 20:
        if fixedgps2[:2] == '02':
            monitor.insert(tk.END, "[")
            monitor.insert(tk.END, hour, "tag1")
            monitor.insert(tk.END, ":")
            monitor.insert(tk.END, minute, "tag1")
            monitor.insert(tk.END, ":")
            monitor.insert(tk.END, second, "tag1")
            monitor.insert(tk.END, "] ")
            monitor.insert(tk.END, "Node 2 : " )
            monitor.tag_bind("tag", "<Button-1>", callback)
            monitor.tag_bind("tag", "<Enter>", show_cursor)
            monitor.tag_bind("tag", "<Leave>", normal_cursor)
            monitor.insert(tk.END, fixedgps2[2:], "tag")
            monitor.insert(tk.END, " (executed : %.2f second) " %(time.time() - start_time),"tag2")
            monitor.insert(tk.END,"\n")
	    
    if drop.get() == "Node 3"  and len(fixedgps3[2:]) <= 20:
        if fixedgps3[:2] == '03':
            monitor.insert(tk.END, "[")
            monitor.insert(tk.END, hour, "tag1")
            monitor.insert(tk.END, ":")
            monitor.insert(tk.END, minute, "tag1")
            monitor.insert(tk.END, ":")
            monitor.insert(tk.END, second, "tag1")
            monitor.insert(tk.END, "] ")
            monitor.insert(tk.END, "Node 3 : " )
            monitor.tag_bind("tag", "<Button-1>", callback)
            monitor.tag_bind("tag", "<Enter>", show_cursor)
            monitor.tag_bind("tag", "<Leave>", normal_cursor)
            monitor.insert(tk.END, fixedgps3[2:], "tag")
            monitor.insert(tk.END, " (executed : %.2f second) " %(time.time() - start_time),"tag2")
            monitor.insert(tk.END,"\n")
            
    if drop.get() == "View All": 
        monitor.insert(tk.END, "[")
        monitor.insert(tk.END, hour, "tag1")
        monitor.insert(tk.END, ":")
        monitor.insert(tk.END, minute, "tag1")
        monitor.insert(tk.END, ":")
        monitor.insert(tk.END, second, "tag1")
        monitor.insert(tk.END, "] ")
        monitor.insert(tk.END, "View All : " )
        monitor.tag_bind("tag", "<Button-1>", callback)
        monitor.tag_bind("tag", "<Enter>", show_cursor)
        monitor.tag_bind("tag", "<Leave>", normal_cursor)
        monitor.insert(tk.END, "Click here", "tag")
        monitor.insert(tk.END, " (executed : %.2f second) " %(time.time() - start_time),"tag2")
        monitor.insert(tk.END,"\n")
        
        
    
    monitor.config(state = DISABLED)
    if var.get() == 1:
        monitor.see(tk.END)






root.mainloop()

