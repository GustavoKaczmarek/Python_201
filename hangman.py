import random

def hangman():
    words = []
    with open("./archivos/data.txt","r") as f:
        for line in f:
            words.append(str(line.replace("\n", "")[::]))
    
    my_dict = {i:len(i) for i in words}
    
    my_list = [word for word in my_dict]
    chosen_word = random.choice(my_list)
    guessed_word = "_"*len(chosen_word)
 

    print("Adivina la palabra!")
    print("\n")
    
    while chosen_word != guessed_word:
        print(guessed_word)
        char = input("Ingresa una letra: ")
        if char in chosen_word:
            guessed_word = list(guessed_word)
            for i,x in enumerate(chosen_word):
                if x == char:
                    guessed_word[i] = x
            guessed_word = "".join(guessed_word)
            
  
    print("Ganaste! tu palabra era: " + chosen_word)


def run():
    hangman()


if __name__ == '__main__':
    run()