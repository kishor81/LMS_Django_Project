from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    MembershipDate = models.DateField()

    def __str__(self):
        return self.Name
    
class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13, unique=True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=50)

    def __str__(self):
        return self.Title

class BookDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    Book = models.OneToOneField(Book, on_delete=models.CASCADE)
    NumberOfPages = models.PositiveIntegerField()
    Publisher = models.CharField(max_length=255)
    Language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Book.Title} - Details"

class BorrowedBooks(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.User.Name} - {self.Book.Title}"
