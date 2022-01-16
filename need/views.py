from django.shortcuts import render, HttpResponse, redirect


# we have to import our models from model file of app for initialising objects
from need.models import BookCollection, StudentRecord, BookRecord, HistoryRecord

from django.contrib.auth.models import auth, User

from accounts.models import StudentInfo

from datetime import datetime, timedelta

from django.contrib import messages  

# Create your views here.

def catalog(request):

    return render(request, 'catalog.html')

def search(request):

    if request.method == "POST":
        
        name = request.POST.get("name")
        author = request.POST.get("author")

        if BookCollection.objects.filter(name=name).exists():    

            lst = list(BookCollection.objects.filter(name=name, author=author).all())

            if lst == []:

                messages.warning(request, "Sorry!!We have this book butof different author..")

                return redirect("search")  

            else:    

                obj = BookCollection.objects.filter(name=name, author=author).all()[0]

                if obj.quantity != 0:
                
                    return redirect("IssueConfirmation")

                else:

                    messages.warning(request, "Sorry, we don't have this book in our library, Please search another book..")

                    return redirect("search")    

        else:

            messages.warning(request, "Sorry, we dont have this book in our library, please search anyother book..")

            return redirect("search")   

    else:

        return render(request, 'search.html')    


def IssueConfirmation(request):
    
    if request.method == "POST":
        
        yes = request.POST.get("yes", "off")
        no = request.POST.get("no", "off")
        
        if yes == "on":
            
            return redirect("Issue")

        elif no == "on":
            
            return redirect("catalog")

    else:
        
        return render(request, "issueConfirmation.html")    



def askIssue(request):

    if request.method == "POST":
        
        yes = request.POST.get("yes", "off")
        no = request.POST.get("no", "off")
        
        if yes == "on":
            
            return redirect("Issue")

        elif no == "on":
            
            return redirect("search")

    else:

        return render(request, "askIssue.html")


def Issue(request):

    if request.method == "POST":
   
        bookName = request.POST.get("bookName")
        author = request.POST.get("author")

        lst = list(BookCollection.objects.filter(name=bookName, author=author).all())

        if lst == []:

            # displaying warning message if student didn't search their book properly.
            messages.warning(request, "It seems that you didn't search your desired book or any other student were issued this book before you !!!.. Please Search it again properly")
                    
            return redirect("search")

        else:

            obj = lst[0]

            if obj.quantity != 0:     
                print("My name is Naveennnnnn")
                temp = request.user
                
                if temp.is_authenticated:

                    temp1 = temp.detail 
                    
                    lst = list(StudentRecord.objects.filter(rollNumber = temp1.rollNumber))

                    if (len(lst) == 0):

                        student = StudentRecord(rollNumber=temp1.rollNumber, fname=temp.first_name, lname=temp.last_name, phone=temp1.phone, email=temp.email)
                        student.save()

                        bo = BookRecord(bookName=bookName, author=author, key=student)
                        bo.save()
                        
                        # displaying success message if book successfully issued.
                        messages.success(request, "Book Issued, Have a nice day & Keep Learning!!!!")
                    
                        book = BookCollection.objects.filter(name=bookName, author=author).all()[0]
                        book.quantity -= 1
                        book.save()

                        return redirect("catalog")


                    else:

                        # False indicates Not returned that book
                        lst = list(StudentRecord.objects.get(rollNumber = temp1.rollNumber).books.filter(BookStatus="False").all())

                        if ( len(lst) == 0 ) or ( len(lst) == 1 ) :
                            
                            student =  StudentRecord.objects.get(rollNumber = temp1.rollNumber)

                            bo = BookRecord(bookName=bookName, author=author, key=student)
                            bo.save()

                            # displaying success message if book successfully issued.
                            messages.success(request, "Book Issued, Have a nice day & Keep Learning!!!!")

                            book = BookCollection.objects.filter(name=bookName, author=author).all()[0]
                            book.quantity -= 1
                            book.save()

                            return redirect("catalog")


                        else:    
                
                            # displaying warning message if student already Issued their Maximum Books i.e 2 books/student,
                            messages.warning(request, "Sorry!! You already Issued 2 Books (Maximum), We can only allow 2 Books/Student at a time, Please Return One Book to Issue this Book!!")
                    
                            return redirect("Return")    


                else:

                    print("Don't Enter Others Details")

                    return redirect("Issue")    
            
            else:

                # displaying warning message if we don't have any copy of this book.
                messages.warning(request, "Sorry!! We don't have any copy of this book, Please search anyother book..!!")
                    
                return redirect("search") 

    else:

        return render(request, "Issue.html")


def reIssue(request):

    if request.method == "POST":

        bookName = request.POST.get("bookName")
        author = request.POST.get("author")

        temp = request.user

        # rollNumber, phone accessed by temp1 
        temp1 = temp.detail

        studentObject = StudentRecord.objects.get(rollNumber = temp1.rollNumber).books.filter(bookName = bookName, author = author).all()[0]

        Issuedate = studentObject.Issuedate
        DueDate = studentObject.DueDate

        # print(DueDate.date()) 

        # datetime.today.date() gives error, better to use
        # today = datetime.today()
        # print(today.date()) or print(today.day()) etc

        today = datetime.today()
        # print(today.date())

        # No fine
        if DueDate.date() >= today.date():
            
            # displaying success message for Re-Issuing the book.
            messages.success(request, "Your book get reIssued, Have a nice day & Keep Learning!!")
                   
            Fine = 0

        # date crossed, fine!!
        else:

            difference = today.date() - DueDate.date()

            # difference.days() is wrong
            Fine = difference.days * 5  
  
            # displaying success message for Re-Issuing the book with fine details.
            messages.success(request, "Please Pay your due fine of rupess %d by considering 5 Rs/Day !!.... Your book Re-Issued to you!!" % Fine)

        # Very Important to find, for IdKey... or for linking
        student =  StudentRecord.objects.get(rollNumber = temp1.rollNumber)

        record = HistoryRecord(bookName = bookName, author = author, Issuedate = Issuedate, DueDate = DueDate, ReturnDate = today, Fine = Fine, IdKey = student)
        record.save()


        book = BookRecord.objects.filter(bookName=bookName, author=author, key=student).all()[0]        
        book.Issuedate = datetime.today()
        book.DueDate = datetime.today() + timedelta(days = 15)
        book.save()

        return redirect("catalog")


    else:

        return render(request, "reIssue.html")


def Return(request):

    if request.method == "POST":

        bookName = request.POST.get("bookName")
        author = request.POST.get("author")

        temp = request.user

        # rollNumber, phone accessed by temp1 
        temp1 = temp.detail

        studentObject = StudentRecord.objects.get(rollNumber = temp1.rollNumber).books.filter(bookName = bookName, author = author).all()[0]

        Issuedate = studentObject.Issuedate
        DueDate = studentObject.DueDate

        today = datetime.today()

        # No fine
        if DueDate.date() >= today.date():
            
            # displaying success message for Returning the book.
            messages.success(request, "Your book Returned, Have a nice day & Keep Learning!!")
            
            Fine = 0

        # date crossed, fine!!
        else:

            difference = today.date() - DueDate.date()

            Fine = difference.days * 5  

            # displaying success message for Returning the book with fine details.
            messages.success(request, "Please Pay your due fine of rupess %d by considering 5 Rs/Day !!.... Your book Returned!!" % Fine)


        # Very Important to find, for IdKey... or for linking
        student =  StudentRecord.objects.get(rollNumber = temp1.rollNumber)

        record = HistoryRecord(bookName = bookName, author = author, Issuedate = Issuedate, DueDate = DueDate, ReturnDate = today, Fine = Fine, IdKey = student)
        record.save()
        
        book = BookRecord.objects.filter(bookName=bookName, author=author, key=student).all()[0]        
        book.delete()

        # OR
        # BookRecord.objects.filter(-------,-------,-------).delete()

        bo = BookCollection.objects.filter(name=bookName, author=author).all()[0]
        bo.quantity += 1
        bo.save()

        return redirect("catalog")


    else:

        return render(request, "Return.html")

