for i in range(100):
    for j in range(5):
        j+=1
        print("A" * j)
        if j ==5:
            for x in range(4,1,-1):
                print("Q" * x)