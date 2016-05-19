import os

relevant_path = "/home/spuran/Caffe/caffe/data/Images/test"#given the path of the folder where test images in jpg format are present
included_extenstions = ['jpg']
file_names = [fn.strip(".jpg") for fn in os.listdir(relevant_path)
              if any(fn.endswith(ext) for ext in included_extenstions)]

f = open('test.csv','w')#creates a file to store the ids of the photos and wiite them into it.
for fn in file_names:
    # b= relevant_path+"/"+fn
    f.write(""+(fn)+""+"\n")
print(len(file_names))


