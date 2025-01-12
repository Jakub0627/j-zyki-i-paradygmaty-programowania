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

//let rec fibRec n =
//    if n <= 1 then n
//    else fibRec(n - 1) + fibRec(n - 2)

//let fibTail n =
//    let rec fibRecTail n a b =
//        if n = 0 then a
//        elif n = 1 then b
//        else fibRecTail (n - 1) b (a + b)
//    fibRecTail n 0 1

//let x = fibTail 4
//printf("%d") x

//Poniższe zadania poza Fibonacci'm zostały wykonane z pomocą internetu, nie jestem aż tak dobry z F#.

// Zadanie 1: Rekurencyjne generowanie ciągu Fibonacciego
let rec fibonacci n =
    match n with
    | 0 -> 0
    | 1 -> 1
    | _ -> fibonacci (n - 1) + fibonacci (n - 2)

let fibonacciTailRecursive n =
    let rec fibHelper n a b =
        match n with
        | 0 -> a
        | _ -> fibHelper (n - 1) b (a + b)
    fibHelper n 0 1

// Wywołanie funkcji Fibonacci
printfn "Fibonacci (rekurencyjny): %d" (fibonacci 10)
printfn "Fibonacci (ogonowa rekurencja): %d" (fibonacciTailRecursive 10)

// Zadanie 2: Wyszukiwanie elementu w drzewie binarnym
type BinaryTree<'T> =
    | Empty
    | Node of 'T * BinaryTree<'T> * BinaryTree<'T>

let rec searchBinaryTree tree value =
    match tree with
    | Empty -> false
    | Node(v, left, right) when v = value -> true
    | Node(_, left, right) -> searchBinaryTree left value || searchBinaryTree right value

let searchBinaryTreeIterative tree value =
    let stack = System.Collections.Generic.Stack<BinaryTree<'T>>()
    stack.Push(tree)
    let mutable found = false

    while stack.Count > 0 && not found do
        match stack.Pop() with
        | Empty -> ()
        | Node(v, left, right) ->
            if v = value then found <- true
            else
                stack.Push(right)
                stack.Push(left)
    found

// Wywołanie funkcji wyszukiwania w drzewie binarnym
let tree = Node(10, Node(5, Empty, Empty), Node(15, Empty, Empty))
printfn "Wynik wyszukiwania (rekurencyjnie): %b" (searchBinaryTree tree 5)
printfn "Wynik wyszukiwania (iteracyjnie): %b" (searchBinaryTreeIterative tree 15)

// Zadanie 3: Generowanie permutacji listy
let rec generatePermutations list =
    match list with
    | [] -> [[]]
    | _ ->
        [for x in list do
            for perm in generatePermutations (List.filter ((<>) x) list) do
                yield x :: perm]

// Wywołanie funkcji generowania permutacji
printfn "Permutacje: %A" (generatePermutations [1; 2; 3])

// Zadanie 4: Rekurencyjne rozwiązywanie problemu wież Hanoi
let rec solveHanoi n source target auxiliary =
    if n > 0 then
        solveHanoi (n - 1) source auxiliary target
        printfn "Move disk from %s to %s" source target
        solveHanoi (n - 1) auxiliary target source

let solveHanoiIterative n source target auxiliary =
    let stack = System.Collections.Generic.Stack<(int * string * string * string)>()
    stack.Push(n, source, target, auxiliary)

    while stack.Count > 0 do
        let (disks, src, tgt, aux) = stack.Pop()
        if disks > 0 then
            stack.Push(disks - 1, aux, tgt, src)
            printfn "Move disk from %s to %s" src tgt
            stack.Push(disks - 1, src, aux, tgt)

// Wywołanie funkcji rozwiązania wież Hanoi
solveHanoi 3 "A" "C" "B"
solveHanoiIterative 3 "A" "C" "B"

// Zadanie 5: Implementacja algorytmu QuickSort
let rec quickSort list =
    match list with
    | [] -> []
    | pivot :: rest ->
        let smaller = List.filter ((>=) pivot) rest
        let greater = List.filter ((<) pivot) rest
        quickSort smaller @ [pivot] @ quickSort greater

let quickSortIterative list =
    let stack = System.Collections.Generic.Stack<(int list)>()
    stack.Push(list)
    let mutable result = []

    while stack.Count > 0 do
        match stack.Pop() with
        | [] -> ()
        | pivot :: rest ->
            let smaller = List.filter ((>=) pivot) rest
            let greater = List.filter ((<) pivot) rest
            stack.Push(greater)
            stack.Push([pivot])
            stack.Push(smaller)

        | x -> result <- x @ result
    result

// Wywołanie funkcji QuickSort
printfn "Sortujemy: [3; 1; 4; 1; 5; 9; 2; 6; 5; 3; 5]"
printfn "QuickSort (rekurencyjny): %A" (quickSort [3; 1; 4; 1; 5; 9; 2; 6; 5; 3; 5])
printfn "QuickSort (iteracyjny): %A" (quickSortIterative [3; 1; 4; 1; 5; 9; 2; 6; 5; 3; 5])
