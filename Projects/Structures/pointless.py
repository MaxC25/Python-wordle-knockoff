#LinkedListUsingLinkedLists,start=[['ocean',1],['fish',2] ,['eyelids',3],['lizard',4],['salamander',5],['rock',None]],0#pointless
start=0
nextFree=6
LinkedListUsingDicts=[
    {'data':'ocean','pointer':1},       #0
    {'data':'fish','pointer':2},        #1
    {'data':'eyelids','pointer':3},     #2
    {'data':'lizard','pointer':4},      #3
    {'data':'salamander','pointer':5},  #4
    {'data':'rock','pointer':None},     #5
    {'data': "-",'pointer':7},          #6
    {'data': "-",'pointer':8},          #7
    {'data': "-",'pointer':9},          #8
    {'data': "-",'pointer':None}        #9
    ]
print(LinkedListUsingDicts[start]['data'],'''
''')
def traverseList(x):
    if start==None:print('Empty list.')
    else:
        current=start
        while current!=None:
            print(x[current]['data'])
            current=x[current]['pointer']
traverseList(LinkedListUsingDicts)
def search(x,term):#linear also, x is the linked list item
    if start!=None:
        current=start
        while current!=None:
            if x[current]==term:
                return term,current
            current=x[current]['pointer']
print('''
'''+str(search(LinkedListUsingDicts,'fish')))
def insert(pos,y):#y is the item to insert, pos is obvious
    global nextFree,LinkedListUsingDicts
    if pos==0 and nextFree!=None:
        #Change the data stored at location indicated nextFree to item to add
        global start
        LinkedListUsingDicts[nextFree]["data"]=y
        #Store pointer indicated by nextFree as temporary variable
        tmp=LinkedListUsingDicts[nextFree]["pointer"]
        #Change pointer indicated by nextFree to start
        LinkedListUsingDicts[nextFree]["pointer"]=start
        #Change start to nextfeee
        start=nextFree
        #Change nextfree to temporary pointer
        try:LinkedListUsingDicts[tmp]={'data': None,'pointer':tmp+1}
        except:pass
        nextFree=tmp
    else:
        #1 traverse linked list until item before where the item we want to add to is
        current,i=start,0
        while i<pos-1 and current!=None:
            i+=1
            oldcurrent=current
            current=LinkedListUsingDicts[current]['pointer']#2 store pointer of current location
        #3 Change pointer of current location to nextFree
        LinkedListUsingDicts[current]['pointer']=nextFree
        #4 Change data at nextFree to item being added
        LinkedListUsingDicts[nextFree]['data']=y
        #5 Update nextFree location to current nextFree
        tmp=nextFree
        nextFree=LinkedListUsingDicts[nextFree]['pointer']
        try:LinkedListUsingDicts[nextFree]={'data': None,'pointer':nextFree+1} #dangerous
        except:pass
        #6 Update pointer to location of where previous item once was
        LinkedListUsingDicts[tmp]['pointer']=current
insert(4,input('\nInsert item to middle: '))
# traverseList(LinkedListUsingDicts)
print(start)
print(nextFree)
print(LinkedListUsingDicts)