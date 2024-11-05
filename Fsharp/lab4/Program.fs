open System

// For more information see https://aka.ms/fsharp-console-apps
printfn "Hello from F#"

//let x = 5
//let name = "ala"
//let floatA = 3.1415

//printfn "witaj %s" name
//printfn "liczba x ma wartość %d a wartosc float %.2f" x floatA
//printfn "liczba x ma wartość %d a wartosc float %f" x floatA

//let name = System.Console.ReadLine()
//printfn "podaj liczba: "
//let input = Console.ReadLine()
//let mutable liczba = 0

//if Int32.TryParse(input, &liczba) then
//    printfn "podano liczbe %d" liczba
//else
//    printfn "nieprawidłowe dane"


//match liczba with
//| 1 -> "jeden"
//| 2 -> "dwa"
//| 3 -> "trzy"
//| _ -> "inna liczba"

let listaA = [1;2;3;4]
let listaB = 8 :: listaA

for element in listaA do
    printfn "%d " element

printfn "\n"
for element in listaB do
    printfn "%d " element

//

type user = {
    Weight: float
    Height: float
}

let calculateBMI (user: user) = 
    let HeightMeters = user.Height / 100.0
    let bmi = user.Weight / (HeightMeters ** 2)
    bmi

let getCategoryBMI bmi = 
    match bmi with
    | x when x < 18.5 -> "Niedowaga"
    | x when x >= 18.5 && x < 24.9 -> "Prawidłowa waga"
    | x when x >= 25.0 && x < 29.9 -> "Nadwaga"
    | _ -> "błędne dane, coś źle wyliczyło ... "

// main

[<EntryPoint>]
let main argv =
    // instrukcje
    printfn "Podaj wage w kg "
    let weightInput = Console.ReadLine()
    printfn "Podaj wzrost "
    let heightInput = Console.ReadLine()
