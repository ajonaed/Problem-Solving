from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print('Hello World!')

def findEven(data):
    t1 = datetime.now()
    for i in data:
        if i%2 == 0:
            print('Even')
    t2 = datetime.now()
    print()
    print('Time took by findEvenFunction: ',t2-t1)
def main():
    t3 = datetime.now()
    array = [1,2,3,4,5,6,7,8,9,10,11,12,22,33,5,4,56,4,1,5,4,65,4,5,1,1,23,3,4,5,87,425,41,2,335,222,2222,2222,2,222,39666,669,336954,3331,6664,3333,6999,4111,1111,877,89,744,5652]
    findEven(array)
    t4 = datetime.now()
    print(t4)
    print('Time took by MainFunction: ', t4-t3)

if __name__ == '__main__':
    main()
