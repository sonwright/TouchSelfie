###############CHANGE ME###########################
printer_MAC = "70:2C:1F:25:77:F3"
my_email = 'sonwright@gmail.com' # must be gmail account. 
my_email_password = 'strongpassword'
subject = 'Alexandra\'s First Luau'
####################################################

def print_photo():
    print "print photo"
    print "command: " + "obexftp --nopath --noconn --uuid none --bluetooth " +  printer_MAC +  " --channel 4 -p "


def print_photo2():
    global printer_MAC
    kill_keyboard()

    top = Tkinter.Tk()
    top.title("Printing")
    msg = Tkinter.Label(top, text="Sending to printer. Please wait 1-2 minutes.",width=50,background='#B1B1B1')
    msg.pack()
    top.geometry("%dx%d%+d%+d" % (400, 100, 250, 125))
    top.configure(background='#B1B1B1')
    center(top)
   
    master.config(cursor="watch")
    top.config(cursor="watch")
    master.update()
    top.update()
 
    print ("Print photo")
    pp = subprocess.Popen(["obexftp --nopath --noconn --uuid none --bluetooth " +  printer_MAC +  " --channel 4 -p " + output],shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    message =  pp.communicate(input)
    master.config(cursor="")
    top.destroy()
    msg = "failed"
    if msg.encode('utf-8') in message[0]:
        tkMessageBox.showerror("Error", "Print failed. Check paper or make sure printer is on and paired and print again")
        
    else:
        tkMessageBox.showinfo("Printing", "Photo successfully sent. Now printing...")
        
    return True
