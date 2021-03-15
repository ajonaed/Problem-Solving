def main():
    aMatrix = [[0,1,0,0,1], [1,0,1,1,1],[0,1,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]

    # for vertex in range(len(aMatrix)):
    #     for edge in range(len(aMatrix[vertex])):
    #         if aMatrix[vertex][edge] == 1:
    #             print(vertex, ' Has Connection with ', edge)
    #     print()

    print('Tour is started:', len(aMatrix)-1)
    # for vertex for vertex in range(len(aMatrix)):
    v = 0
    edge = 0
    counter = 0;
    while counter < len(aMatrix):
        if v == len(aMatrix)-1:
            edge = 0
        else:
            edge = v + 1

        if aMatrix[v][edge] == 1:
            if v == len(aMatrix)-1 and edge == 0:
                print('From ',v,', the tourists are now in ',edge)
                print('We are back at the starting point, Tour is finished!')
                counter += 1
            else:
                print('From ',v,', the tourists are now in ',edge)
                v = edge
                counter += 1
        else:
            print('Incremental Cyle is not available!')
            break


if __name__ == '__main__':
    main()
