def twoDiskMove(src, dest, inter):
    print('Move', str(src), 'to', str(inter))
    print('Move', src, 'to', dest)
    print('Move', inter, 'to', dest)
twoDiskMove(1,2,3)
print('-------')
twoDiskMove(1,2,3)

def threeDiskMove(src, dest, inter):
    twoDiskMove(scr,inter,dest)
    print('Move', src, 'to', dest)
    twoDiskMove(src,inter,dest)
threeDiskMove(1,2,3)
