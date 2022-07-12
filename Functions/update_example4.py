#Define function to calculate fine for a book based on days late book category
# Using following rules
# 1. fine for books in category A is Rs. 100 per day
# 2. fine for books in category B is Rs. 50 per day
# 3. fine for books in category C is Rs. 10 per day
# 4. fine for books more than 10 days fine double
def book_fine(days,category):
    fine = 0
    if days <=10 and category == 'A':
        fine = (days * 100)
        return fine
    elif days <=10 and category == 'B':
        fine = (days * 50)
        return fine
    elif days <=10 and category == 'C':
        fine = (days * 10)
        return fine
    elif days >=10 and category == 'A':
        fine = (days * 100)*2
        return fine
    elif days >=10 and category == 'B':
        fine = (days * 50)*2
        return fine
    elif days >=10 and category == 'C':
        fine = (days * 10)*2
        return fine
    
if __name__ == "__main__":
    days = 15
    cat = 'B'
    book=book_fine(days,cat)
    print(f"The total book fine is {book}")


