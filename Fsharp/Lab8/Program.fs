open System
open System.Collections.Generic

/// Definicja listy łączonej
type LinkedList<'T> =
    | Empty
    | Node of 'T * LinkedList<'T>

/// Typ pomocniczy do funkcji findIndex
type IndexResult =
    | Found of int
    | NotFound

/// Wyjątek rzucany, gdy dwie listy mają różną długość (używane w compareElements)
exception ListsHaveDifferentLengthException of string

/// Moduł zawierający funkcje do zadań
module LinkedList =

    // 1. Tworzenie listy łączonej ze zwykłej listy
    let rec fromList =
        function
        | [] -> Empty
        | x :: xs -> Node(x, fromList xs)

    // 2a. Wyświetlanie elementów listy
    let rec printList list =
        match list with 
        | Empty -> ()
        | Node(value, next) ->
            printf "%A " value
            printList next

    // 2b. Sumowanie elementów 
    let rec sumList =
        function
        | Empty -> 0
        | Node(x, xs) -> x + sumList xs

    // 3. Znajdowanie min i max w liście
    let findMinMax list = 
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

    // 4. Odwracanie kolejności elementów listy
    let reverse list =
        let rec loop acc lst =
            match lst with
            | Empty -> acc
            | Node(x, xs) -> loop (Node(x, acc)) xs
        loop Empty list

    // 5. Sprawdzanie, czy dany element znajduje się w liście
    let rec contains value list =
        match list with
        | Empty -> false
        | Node(x, xs) when x = value -> true
        | Node(_, xs) -> contains value xs

    // 6. Znajdowanie indeksu podanego elementu
    let findIndex value list =
        let rec loop i lst =
            match lst with
            | Empty -> NotFound
            | Node(x, xs) when x = value -> Found i
            | Node(_, xs) -> loop (i + 1) xs
        loop 0 list

    // 7. Zliczanie wystąpień danego elementu w liście
    let rec countOccurrences value list =
        match list with
        | Empty -> 0
        | Node(x, xs) ->
            let add = if x = value then 1 else 0
            add + countOccurrences value xs

    // 8. Łączenie dwóch list łączonych
    let concat list1 list2 =
        let rec loop l1 =
            match l1 with
            | Empty -> list2
            | Node(x, xs) -> Node(x, loop xs)
        loop list1

    // 9. Porównywanie elementów dwóch list (tej samej długości).
    let rec compareElements list1 list2 =
        match list1, list2 with
        | Empty, Empty -> Empty
        | Empty, Node(_) -> raise (ListsHaveDifferentLengthException "Listy mają różną długość.")
        | Node(_), Empty -> raise (ListsHaveDifferentLengthException "Listy mają różną długość.")
        | Node(x, xs), Node(y, ys) ->
            Node(x > y, compareElements xs ys)

    // 10. Zwracanie nowej listy zawierającej tylko elementy spełniające warunek (filter)
    let filter predicate list =
        let rec loop acc lst =
            match lst with
            | Empty -> reverse acc
            | Node(x, xs) ->
                if predicate x then
                    loop (Node(x, acc)) xs
                else
                    loop acc xs
        loop Empty list

    // 11. Usuwanie duplikatów 
    let distinct list =
        let rec loop (seen: Set<'T>) acc remaining =
            match remaining with
            | Empty -> reverse acc
            | Node(x, xs) ->
                if seen.Contains x then
                    loop seen acc xs
                else
                    loop (seen.Add x) (Node(x, acc)) xs
        loop Set.empty Empty list

    // 12. Dzielenie listy na dwie części: 
    //     - jedną z elementami spełniającymi warunek
    //     - drugą z pozostałymi
    let partition predicate list =
        let rec loop left right lst =
            match lst with
            | Empty -> (reverse left, reverse right)
            | Node(x, xs) ->
                if predicate x then
                    loop (Node(x,left)) right xs
                else
                    loop left (Node(x,right)) xs
        loop Empty Empty list


// MAIN
let readUserList() =
    printf "Podaj elementy listy (oddzielone spacją): "
    let input = Console.ReadLine() // np. "1 2 3"
    let items =
        input.Split([|' '; '\t'|], StringSplitOptions.RemoveEmptyEntries)
        |> Array.choose (fun x ->
            match Int32.TryParse(x) with
            | true, v -> Some v
            | _ -> None)
        |> Array.toList

    LinkedList.fromList items

[<EntryPoint>]
let main argv =

    let mutable userList = LinkedList.Empty
    userList <- readUserList()

    // Wyświetlanie elementów
    printfn "\nElementy listy:"
    LinkedList.printList userList

    // Suma elementów
    let suma = LinkedList.sumList userList
    printfn "\nSuma elementów listy: %d" suma

    // Min i max
    try
        let (minVal, maxVal) = LinkedList.findMinMax userList
        printfn "Minimalny: %d, Maksymalny: %d" minVal maxVal
    with
    | ex -> printfn "Błąd: %s" ex.Message

    // Przykład sprawdzenia, czy znajduje się jakiś element
    printf "\nPodaj wartość do sprawdzenia: "
    let toCheck = Console.ReadLine() |> int
    let isContained = LinkedList.contains toCheck userList
    printfn "Czy element %d jest na liście? %b" toCheck isContained

    // Przykład wyszukania indeksu
    let indexResult = LinkedList.findIndex toCheck userList
    match indexResult with
    | Found i -> printfn "Element %d znaleziony na indeksie: %d" toCheck i
    | NotFound -> printfn "Element %d nie został znaleziony." toCheck

    // Zliczanie liczby wystąpień
    let occurrences = LinkedList.countOccurrences toCheck userList
    printfn "Element %d występuje w liście %d raz(y)." toCheck occurrences

    // Przykład odwrócenia listy
    printfn "\nOdwracanie listy..."
    let reversed = LinkedList.reverse userList
    printf "Odwrócona lista: "
    LinkedList.printList reversed
    printfn ""

    // Przykład filtra: zostawiamy tylko elementy parzyste
    let onlyEven = LinkedList.filter (fun x -> x % 2 = 0) userList
    printf "Elementy parzyste z oryginalnej listy: "
    LinkedList.printList onlyEven
    printfn ""

    // Przykład distinct: usuwamy duplikaty
    let distinctList = LinkedList.distinct userList
    printf "Lista bez duplikatów: "
    LinkedList.printList distinctList
    printfn ""

    // Przykład partition: dzielimy listę na parzyste i nieparzyste
    let (evens, odds) = LinkedList.partition (fun x -> x % 2 = 0) userList
    printf "Parzyste: "
    LinkedList.printList evens
    printfn ""
    printf "Nieparzyste: "
    LinkedList.printList odds
    printfn ""

    printfn "\n(Działanie programu zakończone.)"
    0
