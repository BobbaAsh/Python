import random
import pandas

choiceMenu = input("Menu:\n\n 1. FETEKDO\n\n 2. ReadMe\n\n 3. Quitter \n")

while choiceMenu == "1" or "2":
    if choiceMenu == "1":
        df = pandas.read_csv('names.csv')
        list = df.values.tolist()

        random.shuffle(list)

        i=0

        while i != len(list):
            index_max = len(list) - 1
            continue_sort = input('Tirer le duo suivant ? O/N ')
            if continue_sort.lower() == 'o':
                if i < index_max:
                    print(list[i], ' donne à ', list[i+1])
                    i = i + 1
                else:
                    print(list[len(list) - 1], ' donne à ', list[0])
                    break
            elif continue_sort.lower() == 'n':
                print('Salut, à la prochaine !')
                break
            else:
                print("Lettre 'O' ou lettre 'N' !")

        choiceMenu = input("Menu:\n\n 1. FETEKDO\n\n 2. ReadMe\n\n 3. Quitter")

    elif choiceMenu == "2":
        print("REEEAAAADMEEE")
        print("Menu:\n\n 1. FETEKDO\n\n 2. ReadMe\n\n 3. Quitter")
        choiceMenu = input()

    else: 
        break