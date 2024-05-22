def make_album(artist,title,tracks=None):
    """ Create a music album dict using an artist and music title """
    albumDict={'artist':artist,
               'title' : title,
               'tracks' : tracks,
    }
    return albumDict

while True:
    artist=input("Enter artist name / Q to quit ")
    if artist=='Q':
        break
    title=input('Enter title name / Q to quit ')
    if title=='Q':
        break
    tracks=input('Enter number of tracks / Q to quit ')
    if tracks=='Q':
        break
    elif tracks=='':
        tracks=None
    print(make_album(artist,title,tracks))


""" alb1=make_album('rahman','dilse')
alb2=make_album('ani','jalier',6)
alb3=make_album('Harris','KK',5)

print(alb1)
print(alb2)
print(alb3) """


