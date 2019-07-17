class PhoneBook:
    def __init__(self,line,dict):
        self.line = line
        self.phonedict = dict
        if len(self.line.split()) == 2:
            self.phonedict[self.line.split()[0]] = self.line.split()[1]

    def queryPhone(self,name):
        self.name = name
        if name in self.phonedict:
            print("{}={}".format(self.name,self.phonedict[self.name]))
        else:
            print("Not found")

n = int(input())
phonedict = dict()
for i in range(0, n):
    line = str(input())
    p = PhoneBook(line,phonedict)

qry_list = []
qry = str(input())
while qry:
    qry_list.append(qry)
    try:
        qry = str(input())
    except (EOFError):
        break

for name in qry_list:
    p.queryPhone(name)
