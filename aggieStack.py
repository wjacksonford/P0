#************************************
#************************************
# Whittney Ford
#
# CSCE 678 Fall 2018
#
# Project Zero
#
# September 22, 2018
#
#*************************************
#*************************************

import sys
import datetime

data = datetime.datetime.today();

#***The Following are text files that will be read/written by this program
log_text_file = "aggiestack-log.txt"
hardware_log_file = "aggiestack-hardware.txt"
images_log_file = "aggiestack-images.txt"
flavors_log_file = "aggiestack-flavors.txt"
#***********************************************************************

#***The Following are variables to store configes
machines = []
machinestwo = []
machinethree = []
images = []
imagestwo = []
imagesthree = []
flavors = []
flavorstwo = []
flavorsthree = []
#**End of configuration variables

#*** The Following are functions used to do the work
def hardware_config():
    print("This configures hardware")
    infile = open(sys.argv[3],"r")
    print("Hi Whittney")
    line = infile.readline()
    with open(sys.argv[3]) as infile:
        for line in infile:
            linetwo = line.strip("\n")
            machines.append(linetwo)  # I'm going to need str.split()
            print("Hi ruchi")
    infile.close()
    machinestwo = machines[1:(int)(machines[0])]
    segment = machinestwo[0].split(" ")
    if len(segment)>5 | len(segment)<5:
        outfile = open(log_text_file, "a")
        outfile.write(str(data) + " FAILURE" + command + "\n")
        outfile.close()
        raise RuntimeError("Not a hardware confige file: ")
    for x in machinestwo:
        machinethree.append(x)
        hdwFileOut = open(hardware_log_file,"a")
        hdwFileOut.write(x + "\n")
        hdwFileOut.close()
    outfile = open(log_text_file, "a")
    outfile.write(str(data) + " SUCCESS " + command + "\n")
    outfile.close()


def images_config():
    print("This configures images")
    infile = open(sys.argv[3], "r")
    line = infile.readline()
    with open(sys.argv[3]) as infile:
        for line in infile:
            linetwo = line.strip("\n")
            images.append(linetwo)
    infile.close()
    imagestwo = images[1:(int)(images[0])]
    for x in imagestwo:
        imagesthree.append(x)
        imFileOut = open(images_log_file,"a")
        imFileOut.write(x + "\n")
        imFileOut.close()
    infile.close()
    outfile = open(log_text_file, "a")
    outfile.write(str(data) + " SUCCESS " + command + "\n")
    outfile.close()
def flavors_config():
    print("This configures flavors")
    infile = open(sys.argv[3], "r")
    line = infile.readline()
    with open(sys.argv[3]) as infile:
        for line in infile:
            linetwo = line.strip("\n")
            flavors.append(linetwo)
    infile.close()
    flavorstwo = flavors[1:(int)(flavors[0])]
    for x in flavorstwo:
        flavorsthree.append(x)
        flvFileOut = open(flavors_log_file,"a")
        flvFileOut.write(x + "\n")
        flvFileOut.close()
    infile.close()
    outfile = open(log_text_file, "a")
    outfile.write(str(data) + " SUCCESS " + command + "\n")
    outfile.close()
#*** End of working Functions *******************

def show_hardware():
        print("Available servers: ")

        print("Name: \t""IP Adrress: \t""GBs \t"" #Disks \t""#Virtual-CPUs")
        print("------------------------------------------------------------")
       # print(machines)
        hdwFile = open(hardware_log_file, "r")
        line = hdwFile.readline()
        with open(hardware_log_file) as hdwFile:
            for line in hdwFile:
                element = line.split(" ")
                print(element[0] + "\t" + format(element[1], ">11s") + "\t\t\t" + element[2] + "\t\t" + element[3] + "\t\t\t" + element[4])
        hdwFile.close()

def show_images():
    print("Available images: ")
    print("Path: \t""Location: \t")
    print("-------------------------------")
    imFile = open(images_log_file,"r")
    line = imFile.readline()
    with open(images_log_file) as imFile:
        for line in imFile:
            element = line.split(" ")
            print(element[0]+"\t\t"+element[1])
    imFile.close()

def show_flavors():
    print("Available flavors: ")
    print("What: \t""What: \t""What: \t")
    print("---------------------------------")
    flvFile = open(flavors_log_file,"r")
    line = flvFile.readline()
    with open(flavors_log_file) as flvFile:
        for line in flvFile:
            element = line.split(" ")
            print(element[0]+ "\t\t"+element[1]+"\t\t"+element[2])
    flvFile.close()

def configure_command():
    if config_dict.__contains__(commandtwo):
        config_dict[commandtwo]()
    else:
        print("Invalid command: " + command)
        outfile = open(log_text_file, "a")
        outfile.write(str(data) + " FAILURE" + command + "\n")
        outfile.close()
def show_command():
    if commandtwo == "hardware":
        show_hardware()
    if commandtwo == "images":
        show_images()
    if commandtwo == "flavors":
        show_flavors()
    if commandtwo == "all":
        show_hardware()
        show_images()
        show_flavors()
    else:
        print("Invalid command: " + command)
        outfile = open(log_text_file, "a")
        outfile.write(str(data) + " FAILURE" + command + "\n")
        outfile.close()
config_dict = {}
config_dict["hardware"] = hardware_config
config_dict["images"] = images_config
config_dict["flavors"] = flavors_config
config_dict["config"] = configure_command
config_dict["show"] = show_command
command = sys.argv[1]
commandtwo = sys.argv[2]
if config_dict.__contains__(command):
    config_dict[command]()
else:
    print("Invalid command: " +command)
    outfile = open(log_text_file, "a")
    outfile.write(str(data) + " FAILURE" +command+"\n")
    outfile.close()
show_flavors()
show_hardware()