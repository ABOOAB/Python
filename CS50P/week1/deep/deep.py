s = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
s = s.lower().strip()
match s :
    case "42" | "forty-two" | "forty two" :
        print ("Yes")
    case _ :
        print ("No")
