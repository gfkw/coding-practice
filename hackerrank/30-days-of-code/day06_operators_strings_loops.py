class PrintString:
    def __init__(self,s):
        self.s = s
        s1 = ""
        s2 = ""
        for l in range(0, int(len(self.s))):
            if l % 2 == 0:
                s1 += self.s[l]
            else:
                s2 += self.s[l]

        print(s1, s2)

t = int(input())
for i in range(0, t):
    string = str(input())
    p = PrintString(string)
