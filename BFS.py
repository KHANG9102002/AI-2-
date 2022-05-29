from pyamaze import maze,agent,COLOR,textLabel
def BFS(m):
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for direction in 'ESNW':
            if m.maze_map[currCell][direction]==True:
                if direction =='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif direction =='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif direction =='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif direction =='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

if __name__=='__main__':
    print('-------------------------------')
    print('Mời bạn nhập số hàng của mê cung')
    a = int(input())
    print('Mời bạn nhập số cột của mê cung')
    b = int(input())
    print('-------------------------------')
    m=maze(a,b)
    m.CreateMaze(loopPercent=40)
    print('\n Bố cục maze_map =\n',m.maze_map)
    path=BFS(m)

    a=agent(m,footprints=True,filled=True)
    m.tracePath({a:path})
    l=textLabel(m,'Chiều dài đường đi: ',len(path)+1)

    m.run()