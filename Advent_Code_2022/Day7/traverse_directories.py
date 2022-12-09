
with open('../Input_files/7_test.txt') as file:
    input = [line.strip() for line in file.readlines()]

class Dir:
    def __init__(self,name,parent):
        self.parent = parent
        self.name = name
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
        # if root.subdir == []:
        #     return None
        #
        # if name in root.subdir:
        #     return root
        #
        #
        # # If target is present in tree, then prints the parent node
        # #fix for true recorsion!!!
        # for dir in root.subdir:
        #     p = find_parent(name, dir)
        #     if p is None:
        #         for dir in dir.subdir:
        #             p = find_parent(name, dir)
        #         if p is not None:
        #             return p
        #     else:
        #         return p


for count,cmd in enumerate(input):
    #match cmd:
    #    case '$ cd /':
    #only happens on start of file
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
    elif cmd.split(' ')[1] == 'cd':
        #change directory
        if cmd.split(' ')[2] == '..':
            #go up one level
            curr_dir = curr_dir.find_parent()
        else: #regular go into subdir
            new_dir = cmd.split(' ')[2]
            curr_dir = curr_dir.getsubdir(new_dir)

dir_sizes = []
def traverse_dir(root,dir_sizes):
    #implement breat first search
    if len(root.files.keys()) > 0:
        dir_size = sum(root.files.values())
        if len(root.subdir.keys()) > 0:
            sub_list = []
            for name, subdir in root.subdir.items():
                traverse_dir(subdir, sub_list)
            dir_size += sum(sub_list)
        dir_sizes.append(dir_size)
    if len(root.subdir.keys()) > 0:
        for name,subdir in root.subdir.items():
            traverse_dir(subdir,dir_sizes)

def getTotalFileSize(dir):
    file_sum = 0
    if len(dir.subdir.keys()) == 0:
        if len(dir.files.values()) > 0:
            file_sum += sum(dir.files.values())
        #base case, no subdirectories
        size_dict[dir.name] = file_sum
        return size_dict
    else:
        #check if there are files in the dir
        if len(dir.files.values()) > 0:
            file_sum += sum(dir.files.values())
        #go into each subdirectory and get the dict of dir and file sizes
        subdir_list = list(dir.subdir.values())
        for subdir in subdir_list:
            subdir_dict = getTotalFileSize(subdir)
            #size_dict.update(subdir_dict)
            file_sum += sum(subdir_dict.values())
        size_dict[dir.name] = file_sum



size_dict = {}
dir_output = getTotalFileSize(root)
# 1.762.286 too high, 1.253.145 too low
print('Part 1:',sum([dir_size for dir_size in dir_sizes if dir_size <= 100000]))





