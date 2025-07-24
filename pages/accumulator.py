  # הגדרת מחלקה
class Accumulator:
    # זהו בנאי (constructor) – פונקציה שמופעלת כשיוצרים אובייקט חדש מהמחלקה
    def __init__(self, count=0):
        self.__count = count  #משתנה פרטי (private)
        self.__brand = "Accumulator"

    @property
    def count(self):  #זהו getter – מאפשר לגשת לערך של count כמו תכונה (ולא פונקציה)
        return self.__count

    @count.setter
    def count(self, count):  #זהו setter – מאפשר לעדכן את הערך של count
        self.__count = count

#פונקציה שמוסיפה ערך למונה (count)
    def add_counts(self, counts_to_add=1):
        self.__count += counts_to_add