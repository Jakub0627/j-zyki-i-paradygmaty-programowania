open System.Collections.Generic
open System

//definicja listy łązconej
type LinkedList<'T> =
    | Empty
    | Node of 'T * LinkedList<'T>

//moduł zawierający funkcje do zadań
module LinkedList =

    //wczytanie listy od usera
    let rec fromList =
        function
        | [] ->Empty
        | x :: xs -> Node(x, fromList xs)

    let rec printList list =
        match list with 
        | Empty ->()
        | Node(value, next) ->
            printf "%A " value
            printList next

    let rec sumList =
        function
        | Empty -> 0
        | Node(x, xs) -> x + sumList xs

    let rec findMinMax list = 
        match list with
        | Empty -> failwith "Lista jest pusta, brak elementów do porównania"
        | Node(value, tail) ->
            let rec helper currentMin currentMax remaining =
                match remaining with
                | Empty -> (currentMin, currentMax)
                | Node(v, t) ->
                    let newMin = min currentMin v
                    let newMax = max currentMax v
                    helper newMin newMax t

            helper value value tail


//koniec modułu

// funkcja do wczytywanie elementow z klawiatury
let rec readUserList() =
    printf "Podaj elementy listy oddzielone spacją: "
    let input = Console.ReadLine() // e.g. "1 2 3"
    let items =
        input.Split(' ')
        |> Array.choose (fun x ->
            match Int32.TryParse(x) with
            | (true, v) -> Some v
            | _ -> None)
        |> Array.toList

    LinkedList.fromList items

[<EntryPoint>]
let main argv = 
    let mutable userList = LinkedList.Empty

    userList <- readUserList()

    printf "\nElementy listy:\t"
    LinkedList.printList userList

    printf "\nSuma elementów listy:\t"
    let suma = LinkedList.sumList userList
    printf "\nSuma elementów listy: %d" suma

    0

//type LinkedList<'T> = 
//    | Empty
//    | Node of 'T * LinkedList<'T>

//let Head =
//    function
//    | Empty -> failwith "Nie można pobrać głowy z listy pustej"
//    | Node(Head,_) -> Head
        
//let Tail = 
//    function
//    | Empty -> failwith "Nie można pobrać ogona z listy pustej"
//    | Node(Tail,_) -> Tail

//let addHead value list =
//    Node(value, list)

//let rec printList list =
//    match list with 
//    | Empty ->()
//    | Node(value, next) ->
//        printf "%A " value
//        printList next

//let rec numberElements =
//    function
//    | Empty -> 0
//    | Node(_, Tail) -> numberElements Tail + 1


//[<EntryPoint>]
//let main argv =
//    let list1 = Empty
//    let list2 = addHead 1 list1
//    let list3 = addHead 2 list2
//    let list4 = addHead 3 list3

//    printList list4

//    0