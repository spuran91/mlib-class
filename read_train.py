import csv

id_list =[]#list to store the photo ids
col_list =[]#list to store the lables
i =0
path = r'/home/spuran/Downloads/project/train.csv'#give the path of the train.csv file given with data
#labelsing is done based on the column value i.e. ex:if a 1 is in col8 then the corresponding id is labeled 8
with open(path, 'r') as csvfile:
    data = csvfile.readlines()

    for line in data:
        array = line.split(",")

        # print(array)
        if array[1] == "1" and array[1] != "col1" :
            col_list.append(1)
            if  array[0] != "id":
                id_list.append(array[0])
        elif array[2] == "1"  and array[2] != "col2":
            col_list.append(2)
            if  array[0] != "id":
                id_list.append(array[0])
        elif array[3] == "1"  and array[3] != "col3":
            col_list.append(3)
            if  array[0] != "id":
                id_list.append(array[0])
        elif array[4] == "1"  and array[4] != "col4":
            col_list.append(4)
            if  array[0] != "id":
                id_list.append(array[0])
        elif array[5] == "1"   and array[5] != "col5":
            col_list.append(5)
            if  array[0] != "id":
                id_list.append(array[0])
        elif array[6] == "1" and array[6] != "col6":
            col_list.append(6)
            if  array[0] != "id":
                id_list.append(array[0])
        elif array[7] == "1" and array[7] != "col7":
            col_list.append(7)
            if  array[0] != "id":
                id_list.append(array[0])
        elif  array[8] == '1' and array[8] != "col8":
            col_list.append(8)
            if  array[0] != "id":
                id_list.append(array[0])
                print (array[0])
        elif array[0] == "id":
            print("do nothing for ")
            print(array[0] +" ---")
        else:
            print("error found")
            print(array[0])
            print("---------")
            print(array)


    with open('new_train11.csv', 'w') as f:
       wr = csv.writer(f, quoting=csv.QUOTE_ALL)# a csv file i screated with headers as id and label
       wr.writerow(["id","label"])
       for a in zip(*(id_list,col_list)):
         wr.writerow(((a)))



