from typing import List



def convert_to_absolute() -> float:
    
    mon_nombre = float(input("Veuillez entrez votre nombre : "))
    if mon_nombre < 0:
        return mon_nombre * -1
    else:
        return mon_nombre
    


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    
    my_list = []
    
    for lettre in prefixes:
        my_list.append(lettre + suffixes)
    
    return my_list


def prime_integer_summation() -> int:
    
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
            
        return True
    
    my_sum = 0
    prime_i = 1
    n_prime = 0;
    
    x = []
    
    while n_prime < 101:
        if isPrime(prime_i):
            my_sum += prime_i
            n_prime += 1
            
            x.append(prime_i)

        else:
            pass
        prime_i += 1
        
    print("x = ", x, " longeur = ", len(x))
            
    return (my_sum-1)


def factorial(number: int) -> int:
    
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)

def use_continue() -> None:
    
    for i in range(1,11):
        if i==5:
            continue
        else:
            print(i)
        
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
