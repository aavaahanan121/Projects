import main
List_orginal = []

def List_to_string(List):
    _List_orginal = ""
    first = True
    for i in List:
        if first:
            _List_orginal += str(i)
            first = False
        else:
            _List_orginal += (", " + str(i))
    return _List_orginal + "."


for i in range(int(input("How much number do you want to put\n> "))):
    List_orginal.append(input(f"enter no {i + 1} : "))

sort_met = int(input("what type of sorting do you want? 1 : bubble sort, 2 : Selection sort, 3 : insertion_sort\n>"))

print(f"\nOriginal list : {List_to_string(List_orginal)}")

if sort_met == 1:
    print("\nSorted List : " , List_to_string(main.bubble_sort(List_orginal)))
elif sort_met == 2:
    print("\nSorted List : " , List_to_string(main.selection_sort(List_orginal)))
elif sort_met == 3:
    
    print("\nSorted List : " , List_to_string(main.insertion_sort(List_orginal)))

