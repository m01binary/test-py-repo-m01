dict={
    "cybersecurity" : "my life",
    "math": "i like it",
    "networking" : "very good",
    "linux" : "the main os"
}

print("search engine \n")
while True:
    userInput=input("enter the text : \nor type quit for exit, thanks").strip().lower()


    if userInput=="exit":
        break

    valueFound = None

    for key in dict:
        if userInput == key:
            valueFound=dict[key]
            break
        

    if valueFound != None:
        print(f"the result for that word you searched is : {valueFound}")
    elif userInput == "quit":
        print("system turn off")
        break
    else:
        print(f"sorry not finding anythings - try again")

    
