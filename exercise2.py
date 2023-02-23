countries = [[0]*5]*4
countries[0] = ["Iran" , 0 , 0 , 0 , 0]
countries[1] = ["Spain" , 0 , 0 , 0 , 0]
countries[2] = ["portugal" , 0 , 0 , 0 ,0]
countries[3] = ["Morroco" , 0 , 0 , 0 , 0] 
def main():
    
    # countriName = [name , wins , loses , goal differences , points]
    for i in range(4):
        for j in range(i+1 ,4):
            inArr = input().split("-")
            inArrTemp = []
            for p in inArr:
                inArrTemp.append(int(p))
            inArr = inArrTemp


            

            if inArr[0] > inArr[1]:
                diff  = inArr[0] - inArr[1]
                countries[i][1] += 1
                countries[j][2] += 1
                countries[i][3] += diff
                countries[j][3] += -diff
                countries[i][4] += 3


            elif inArr[0] < inArr[1]:
                diff  = inArr[1] - inArr[0]
                countries[j][1] += 1
                countries[i][2] += 1
                countries[j][3] += diff
                countries[i][3] += -diff
                countries[j][4] += 3
                

            else:
                countries[i][4] += 1
                countries[j][4] += 1

    for s in range(4):
        print(countries[s][0] + " wins : " + str(countries[s][1]) + " , loses :" + str(countries[s][2]) + ", goal differences :" + str(countries[s][3]) + ", points : " + str(countries[s][4]))
                
if __name__ == "__main__":
    main()