Given_List_Score=[2,3,6,6,5]
First=Given_List_Score[0]
Runner=Given_List_Score[1]
for i in Given_List_Score:
    if i > First:
        Runner=First
        First=i
    if i > Runner & i!=First:
        Runner=i
print("The Runner up score is",Runner)
