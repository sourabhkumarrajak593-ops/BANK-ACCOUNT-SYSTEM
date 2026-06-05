# Create a class Book with the following attributes: 
# • title 
# • author 
# • list of reviews 

# And add methods to: 
# • add a new review 
# • count reviews 
# • display all reviews 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)
        print("Review Added successfully!")

    def count_reviews(self):
        print("Total Reviws: ", len(self.reviews))

    def display_reviews(self):
        print("\nReviews: ")
        for review in self.reviews:
            print("-", review)


title = input("Enter Book Title: ").lower()
author = input("Enter Author Name: ").lower()

book = Book(title, author)

n = int(input("How many reviews do you want to add: "))

for i in range(n):
    review = input(f"Enter Review {i+1}: ")
    book.add_review(review)

book.count_reviews()
book.display_reviews()
