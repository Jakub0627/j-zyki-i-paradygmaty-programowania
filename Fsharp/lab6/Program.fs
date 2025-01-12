open System


// Zadanie 1. Liczba słów i znaków (bez spacji)
let zadanie1() =
    printfn "Zadanie 1: Liczba słów i znaków"
    printf "Podaj tekst: "
    let text = Console.ReadLine()
    // Rozdzielamy tekst na słowa (po spacji) - usuwając puste elementy
    let words = text.Split([|' '|], StringSplitOptions.RemoveEmptyEntries)
    let wordCount = words.Length

    // Usuwamy wszystkie spacje i liczymy znaki
    let charCount = text.Replace(" ", "").Length

    printfn "Liczba słów: %d" wordCount
    printfn "Liczba znaków (bez spacji): %d" charCount
    printfn ""


// Zadanie 2. Sprawdzenie palindromu
let isPalindrome (s: string) =
    // Dla pewności, ignorujemy wielkość liter
    let lower = s.ToLower()
    lower = new string (lower.ToCharArray() |> Array.rev)

let zadanie2() =
    printfn "Zadanie 2: Sprawdzenie palindromu"
    printf "Podaj ciąg znaków: "
    let input = Console.ReadLine()
    if isPalindrome input then
        printfn "Tekst \"%s\" jest palindromem." input
    else
        printfn "Tekst \"%s\" nie jest palindromem." input
    printfn ""


// Zadanie 3. Usuwanie duplikatów
let zadanie3() =
    printfn "Zadanie 3: Usuwanie duplikatów"
    printf "Podaj słowa oddzielone spacjami: "
    let input = Console.ReadLine()
    // Dzielenie na listę słów
    let words = input.Split([|' '|], StringSplitOptions.RemoveEmptyEntries) |> List.ofArray
    // Usuwanie duplikatów
    let uniqueWords = List.distinct words
    // Wyświetlamy listę unikalnych słów
    printfn "Unikalne słowa: %A" uniqueWords
    printfn ""


// Zadanie 4. Zmiana formatu tekstu

let zadanie4() =
    printfn "Zadanie 4: Zmiana formatu tekstu"
    printfn "Wprowadzaj kolejne linie w formacie \"imię; nazwisko; wiek\"."
    printfn "Pozostaw pusty wiersz, aby zakończyć."

    let mutable running = true
    while running do
        printf "\nPodaj dane lub naciśnij Enter, aby zakończyć: "
        let line = Console.ReadLine()
        if String.IsNullOrWhiteSpace(line) then
            running <- false
        else
            let parts = line.Split([|';'|], StringSplitOptions.RemoveEmptyEntries)
            if parts.Length = 3 then
                let imie = parts.[0].Trim()
                let nazwisko = parts.[1].Trim()
                let wiek = parts.[2].Trim()
                printfn "%s, %s (%s lat)" nazwisko imie wiek
            else
                printfn "Nieprawidłowy format. Spróbuj ponownie."
    printfn ""


// Zadanie 5. Znajdowanie najdłuższego słowa
let zadanie5() =
    printfn "Zadanie 5: Najdłuższe słowo w tekście"
    printf "Podaj tekst: "
    let text = Console.ReadLine()
    let words = text.Split([|' '|], StringSplitOptions.RemoveEmptyEntries)
    // Znajdujemy słowo o największej długości
    if words.Length > 0 then
        let longestWord = words |> Array.maxBy (fun w -> w.Length)
        printfn "Najdłuższe słowo: %s" longestWord
        printfn "Długość najdłuższego słowa: %d" longestWord.Length
    else
        printfn "Nie wprowadzono żadnych słów."
    printfn ""


// Zadanie 6. Wyszukiwanie i zamiana słowa
let zadanie6() =
    printfn "Zadanie 6: Wyszukiwanie i zamiana słowa"
    printf "Podaj tekst: "
    let text = Console.ReadLine()
    printf "Podaj słowo do wyszukania: "
    let searchWord = Console.ReadLine()
    printf "Podaj słowo, na które zamienić: "
    let replaceWord = Console.ReadLine()

    // Wykonanie zamiany
    let modifiedText = text.Replace(searchWord, replaceWord)
    printfn "Zmodyfikowany tekst: %s" modifiedText
    printfn ""


// Program główny
[<EntryPoint>]
let main _ =

    
    zadanie1()
    zadanie2()
    zadanie3()
    zadanie4()
    zadanie5()
    zadanie6()

    0
