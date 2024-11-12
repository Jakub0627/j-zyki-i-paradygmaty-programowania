let rec countDown n =
    if n<=0 then
        printfn "Koniec obliczeń"
    else
        printfn "n = %d" n
        countDown(n-1)

countDown 5

let fibonacciTail n =
    let rec aux n acc =
        if n <= 0 then acc
        else aux(n-1) (acc+n)
    aux n 0


let wynik =fibonacciTail 5
printf "wynik %d" wynik

let sumaTailRec n =
    let rec aux n acc =
        if n <= 0 then acc
        else aux (n - 1) (acc + n)
    aux n 0

let wynik1 = sumaTailRec 5
printfn "wynik %d" wynik1

//fibbonacci

let rec fibRec n =
    if n <= 1 then n
    else fibRec(n - 1) + fibRec(n - 2)

let fibTail n =
    let rec fibRecTail n a b =
        if n = 0 then a
        elif n = 1 then b
        else fibRecTail (n - 1) b (a + b)
    fibRecTail n 0 1

let x = fibTail 4
printf("%d") x
