open System
open System.Collections.Generic

type BankAccount(accountNumber: string, initialBalance: decimal) =
    let mutable balance = initialBalance 

    member this.AccountNumber = accountNumber

    member this.Balance = balance

    member this.Deposit(amount: decimal) =
        if amount <= 0m then
            invalidArg "amount" "Kwota wpłaty musi być większa niż 0."
        else
            balance <- balance + amount
            printfn "[%s] Wpłata: %M, Nowe saldo: %M" accountNumber amount balance

    member this.Withdraw(amount: decimal) =
        if amount <= 0m then
            invalidArg "amount" "Kwota wypłaty musi być większa niż 0."
        elif amount > balance then
            printfn "[%s] Brak wystarczających środków do wypłaty %M. Saldo: %M" accountNumber amount balance
        else
            balance <- balance - amount
            printfn "[%s] Wypłata: %M, Nowe saldo: %M" accountNumber amount balance


type Bank() =
    let accounts = Dictionary<string, BankAccount>()

    member this.CreateAccount(accountNumber: string, initialBalance: decimal) =
        if accounts.ContainsKey(accountNumber) then
            printfn "Konto o numerze %s już istnieje!" accountNumber
        else
            let newAccount = BankAccount(accountNumber, initialBalance)
            accounts.Add(accountNumber, newAccount)
            printfn "Utworzono konto o numerze %s z saldem początkowym %M." accountNumber initialBalance

    member this.GetAccount(accountNumber: string) =
        if accounts.ContainsKey(accountNumber) then
            Some(accounts.[accountNumber])
        else
            None

    member this.UpdateAccount(accountNumber: string, newBalance: decimal) =
        match this.GetAccount(accountNumber) with
        | Some account ->
            let oldBalance = account.Balance
            match newBalance.CompareTo(oldBalance) with
            | 0 -> 
                printfn "Saldo na koncie %s pozostaje bez zmian (%M)." accountNumber oldBalance
            | 1 -> 
                let diff = newBalance - oldBalance
                account.Deposit(diff)
                printfn "Zaktualizowano saldo konta %s do %M." accountNumber newBalance
            | -1 ->
                let diff = oldBalance - newBalance
                account.Withdraw(diff)
                printfn "Zaktualizowano saldo konta %s do %M." accountNumber newBalance
            | _ -> () 
        | None ->
            printfn "Nie znaleziono konta o numerze %s. Nie można zaktualizować." accountNumber

    member this.DeleteAccount(accountNumber: string) =
        if accounts.Remove(accountNumber) then
            printfn "Usunięto konto o numerze %s." accountNumber
        else
            printfn "Nie znaleziono konta o numerze %s. Usunięcie nie powiodło się." accountNumber

    member this.ListAccounts() =
        if accounts.Count = 0 then
            printfn "W banku nie ma żadnych kont."
        else
            printfn "Dostępne konta w banku:"
            accounts
            |> Seq.iter (fun kvp -> printfn " - Numer konta: %s, Saldo: %M" kvp.Key kvp.Value.Balance)


[<EntryPoint>]
let main argv =
    let bank = Bank()

    bank.CreateAccount("123-456-789", 1000m)
    bank.CreateAccount("987-654-321", 500m)
    bank.CreateAccount("987-654-321", 600m) 

    bank.ListAccounts()
    printfn "------------------------------------------------\n"

    match bank.GetAccount("123-456-789") with
    | Some acc ->
        acc.Deposit(250m)
        acc.Withdraw(100m)
    | None ->
        printfn "Konto o numerze '123-456-789' nie istnieje."

    printfn "------------------------------------------------\n"

    bank.UpdateAccount("987-654-321", 1000m)
    bank.UpdateAccount("111-222-333", 300m) 
    printfn "------------------------------------------------\n"

    bank.ListAccounts()
    printfn "------------------------------------------------\n"

    bank.DeleteAccount("123-456-789")
    bank.DeleteAccount("123-456-789")  

    printfn "------------------------------------------------\n"
    bank.ListAccounts()

    0
