import os 
#getcwd ante c=current w= working d=directory or folder
print(os.getcwd())
print(os.listdir())
files=os.listdir()
print(files)
print(len(files))
#os.mkdir
# mk=make(create)
# dir=directory(folder)
#os.mkdir("tharun")           #
# projects ane oka new folder create avuthundhi
# os.rename()
#os.rename("python notes","AI projects")
#os.rename("tharun","os library")     #
if os.path.exists("projects"):
 print("folder already exits")
else:
 print("folder does not exists")
# oka file ni remove cheyyadaniki use chestharu 
os.remove("remove.py")




