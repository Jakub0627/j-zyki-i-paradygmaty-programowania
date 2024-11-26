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

type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages

    member this.GetInfo() =
        printfn "Tytuł: %s \nAutor: %s \nLiczba stron: %d" this.Title this.Author this.Pages


type User(name: string)=
    member this.Name = name
    member this.BorrowedBooks = new List<Book>()

    member this.BorrowedBook(book: Book)=
        this.BorrowedBooks.Add(book)
        printfn "%s wypożyczył książke: %s" this.Name book.Title

    member this.ReturnBook(book: Book)=
        if this.BorrowedBooks.Remove(book) then
            printfn "%s zwrócił ksiązke: %s" this.Name book.Title
        else printfn "%s nie ma wypożyczonej książki: %s" this.Name book.Title

type Library()=
    let books = new List<Book>()

    member this.AddBook(book: Book)=
        book.Add(book)
        printfn "Dodano Książkę: %s" book.Title

    member this.RemoveBook(book: Book)=
        if books.Remove(book) then
            printfn "Usunięto książkę: %s" book Title
        else 

[<EntryPoint>]
let main argv = 
    let book1 = Book("Książka 1", "Autor 1", 123)
    let book2 = Book("Książka 2", "Autor 2", 1000)
    let book3 = Book("Książka 3", "Autor 3", 12)

    book1.GetInfo()
    book2.GetInfo()
    book3.GetInfo()

    0
