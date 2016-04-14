def create_mem(id,name,last,age,classname,**subjects):
    file_creat_path = open ('/Users/Soroush/Desktop/'+id+".mi",'w')
    file_creat_path.writelines(id+"\n")
    file_creat_path.writelines(name+"\n")
    file_creat_path.writelines(last+"\n")
    file_creat_path.writelines(age+"\n")
    file_creat_path.writelines(classname+"\n")
    file_creat_path.writelines(subjects)
    file_creat_path.close()
def load_mem(id):
    file_load_path = open ('/Users/Soroush/Desktop/'+id+".mi",'r')
    load_read_lines = file_load_path.readlines()
    print(load_read_lines)