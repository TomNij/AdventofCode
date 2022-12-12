
with open('../Input_files/7.txt') as file:
    input = [line.strip() for line in file.readlines()]

class Dir:
    def __init__(self,name,parent):
        self.parent = parent
        self.name = parent.name + '/' + name if parent != 'NA' else name
        self.files = {}
        self.subdir = {}

    def __eq__(self, name):
        return self.name == name

    def __repr__(self):
        return f"Dir {self.name},files:{len(self.files.keys())},subdir:{len(self.subdir)}"

    def addfiles(self,file : str,size : int):
        self.files[file] = size

    def addsubdir(self,dir_name,parent):
        self.subdir[dir_name] = Dir(dir_name,parent)

    def getsubdir(self,dir_name):
        return self.subdir[dir_name]

    def find_parent(self):
        return self.parent


tot_sum = 0
for count,cmd in enumerate(input):
    if cmd == '$ cd /':
        root = Dir('/','NA')
        curr_dir = root
    elif cmd == '$ ls':
        pass
    elif cmd[0:3] == 'dir':
        new_dir = cmd.split(' ')[1]
        curr_dir.addsubdir(new_dir,curr_dir)
    elif cmd.split(' ')[0].isnumeric():
        size,name = cmd.split(' ')
        curr_dir.addfiles(name,int(size))
        tot_sum += int(size)
    elif cmd.split(' ')[1] == 'cd':
        #change directory
        if cmd.split(' ')[2] == '..':
            #go up one level
            curr_dir = curr_dir.find_parent()
        else: #regular go into subdir
            new_dir = cmd.split(' ')[2]
            curr_dir = curr_dir.getsubdir(new_dir)


def getTotalFileSize(dir):
    size_dict = {}
    file_sum = 0
    if len(dir.subdir.keys()) == 0:
        if len(dir.files.values()) > 0:
            file_sum += sum(dir.files.values())
        #base case, no subdirectories
        global_dict[dir.name] = file_sum
        size_dict[dir.name] = file_sum
        return size_dict
    else:
        #check if there are files in the dir
        if len(dir.files.values()) > 0:
            file_sum += sum(dir.files.values())
        #go into each subdirectory and get the dict of dir and file sizes
        subdir_list = list(dir.subdir.values())[::-1]
        sub_dir_sum = 0
        for subdir in subdir_list:
            subdir_dict = getTotalFileSize(subdir)
            sub_dir_sum += sum(subdir_dict.values())
            #size_dict.update(subdir_dict)
        size_dict[dir.name] = file_sum + sub_dir_sum
        global_dict[dir.name] = file_sum + sub_dir_sum
        return size_dict


global_dict ={}
getTotalFileSize(root)
# 1.762.286 too high, 1.253.145 too low
print('Part 1:',sum([dir_size for dir_size in global_dict.values() if dir_size <= 100000]))

tot_size = 70000000
file_size = max(global_dict.values())
update_size = 30000000
to_remove = update_size - (tot_size - file_size)
#print min dir size that is bigger than the size we need to remove
print('Part 2:',min([dir_size for dir_size in global_dict.values() if dir_size >= to_remove]))





