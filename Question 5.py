#Emily Nixon and Sarah Stephenson
book_author={
    "To Kill a Mockingbird" : "Harper Lee",
    "1984" : "George Orwell",
    "Warrior Cats" : "Erin Hunter",
    "The Inferno" : "Dante"
}
def author_name(name,dict):
    for key in dict:
        if key == name:
            print(key, dict[name])
        

author_name("1984", book_author)
