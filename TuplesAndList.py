

def main():
    #string
    Data="software engineer"
    print(Data[0:5])
    #List
    Ages=[44,33,45,33,54]
    Ages.append(100)
    Ages.insert(0,33)
    Ages.pop(2)
    Ages.remove(54)
    Ages.index(33)
    Ages.sort()
    print(sum(Ages))
    print(Ages)
    #Tuples
    Ages=[44,33,45,33,54]
    Ages.append(100)
    Ages.insert(0,33)
    print(Ages)



if __name__ == '__main__':main()
