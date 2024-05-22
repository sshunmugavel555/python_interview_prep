from random import randint, choice

lot=list(range(10))
lotter=[ str(e) for e in lot]
let=['a','b','c','d','e']
lottery=lotter+let
print(lottery)

win=[]
for _ in range(4):
    win.append(choice(lottery))

winner=''.join(win)
print(f"winning combo --> {winner}")

print('Finding the winner now ')
ole=[]
cnt=0
while True:
    cnt+=1
    for _ in range(4):
        ole.append(choice(lottery))

    if ''.join(ole) == winner:
        print(f'Won after {cnt} iterations')
        break

    for _ in range(4):
        ole.pop()


