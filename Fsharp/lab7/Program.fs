//type Person(name: string, age: int) =
//    let mutable _name = name
//    let mutable _age = age

//    member this.Name
//        with get() = _name
//        and set(value) = _name <- value

//    member this.Age
//        with get() = _age
//        and set(value) = _age <- value

//    member this.View() =
//        printfn "Witaj %s, twój wiek: %d" _name _age

//type Pracownik(name: string, age: int, stanowisko: string) =
//    inherit Person(name, age)

//    member this.Stanowisko = stanowisko

//    member this.View() =
//        printfn "Witaj %s, twój wiek: %d, twoje stanowisko: %s" this.Name this.Age this.Stanowisko


//let person = Person("Jan", 23)
//person.View()


//let pracownik = Pracownik("Anna", 30, "Inżynier")
//pracownik.View()

//type IWalkable =
//    abstract member Walk : unit -> unit

//type Person(name:string)=
//    member this:Walk(): unit = 
//        printfn "%s chodzi na spacer" this.Name


//let person = Person("Jan") 

//type Animal() = 
//     member this.Speak() = printfn "Zwierze wydaje głos"

//type Dog() = 
//    inherit Animal()
//    override this.Speak() = printfn "pies szczeka"

//type Cat() = 
//    inherit Animal()
//    override this.Speak() = printfn "Kot miauczy"


//type Animal() = 
//     static member this.Speak() = printfn "Zwierze wydaje głos"

open System
open System.Collections.Generic

/// Klasa Book
type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages

    member this.GetInfo() =
        printfn "Tytuł: %s" this.Title
        printfn "Autor: %s" this.Author
        printfn "Liczba stron: %d" this.Pages


/// Klasa User
type User(name: string) =
    member this.Name = name
    member val BorrowedBooks = new List<Book>() with get

    member this.BorrowBook(book: Book) =
        this.BorrowedBooks.Add(book)
        printfn "%s wypożyczył książkę: %s" this.Name book.Title

    member this.ReturnBook(book: Book) =
        if this.BorrowedBooks.Remove(book) then
            printfn "%s zwrócił książkę: %s" this.Name book.Title
        else
            printfn "%s nie ma wypożyczonej książki: %s" this.Name book.Title


/// Klasa Library
type Library() =
    let books = new List<Book>()

    member this.AddBook(book: Book) =
        books.Add(book)
        printfn "Dodano książkę: %s" book.Title

    member this.RemoveBook(book: Book) =
        if books.Remove(book) then
            printfn "Usunięto książkę: %s" book.Title
        else
            printfn "Nie znaleziono książki: %s" book.Title

    member this.ListBooks() =
        printfn "\nAktualne książki w bibliotece:"
        if books.Count = 0 then
            printfn "Biblioteka jest pusta."
        else
            for b in books do
                printfn " - %s (Autor: %s, Strony: %d)" b.Title b.Author b.Pages


[<EntryPoint>]
let main argv = 
    let library = Library()

    let book1 = Book("Książka 1", "Autor 1", 123)
    let book2 = Book("Książka 2", "Autor 2", 1000)
    let book3 = Book("Książka 3", "Autor 3", 12)

    library.AddBook(book1)
    library.AddBook(book2)
    library.AddBook(book3)

    library.ListBooks()

    let user = User("Jan Kowalski")

    user.BorrowBook(book1)
    user.BorrowBook(book2)

    library.RemoveBook(book1)

    library.ListBooks()

    user.ReturnBook(book1)

    library.AddBook(book1)

    library.ListBooks()

    //--------------------------------------------------------


    0
