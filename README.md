# User Manager - program do zarządzania użytkownikami

## Wprowadzenie

Jest to program napisany w języku Python, pozwalający na zarządzanie użytkownikami. Możliwe jest wykonanie takich operacji jak dodawanie nowych użytkowników, usuwanie użytkowników oraz wyświetlanie listy dodanych użytkowników. Dodatkowo zaimplementowane zostało logowanie operacji wykonywanych podczas działania programu do pliku.

## Uruchomienie programu

Aby uruchomić ten program, wykonaj poniższe czynności, bądź upewnij się, że zostały one już wcześniej przez Ciebie wykonane:

## Instalacja Pythona

Sprawdź, czy na Twoim komputerze zainstalowany jest Python. Jeżeli nie, oto sposoby jak możesz go zainstalować, w zależności od systemu operacyjnego, na jakim pracujesz:

### Windows

1. Wejdź na stronę [python.org](https://www.python.org)
2. Pobierz instalator Pythona w zakładce "Downloads"
3. Uruchom instalator
4. Upewnij się, że opcja "Add Python to PATH" jest zaznaczona.
5. Kliknij "Install now"

### Linux (Ubuntu/Debian)

Wykonaj poniższe instrukcje w terminalu:

```bash
sudo apt update
sudo apt install python
```

### MacOS

Wykonaj poniższe instrukcje w terminalu:

```bash
brew install python
```

## Sprawdzenie wersji Pythona

Upewnij się, że zainstalowana przez Ciebie wersja Pythona to co najmniej **3.12**.  

Możesz to zrobić w jeden z kilku poniższych sposobów, w zależności od tego, jakiego systemu operacyjnego używasz:

### Windows

Wykonaj w terminalu poniższą instrukcję:

```bash
python -V
```

### Linux (Debian/Ubuntu)

Wykonaj w terminalu poniższą instrukcję:

```bash
python3 --version
```

Lub w przypadku Pythona starszego niż Python3;

```bash
python --version
```

### MacOS

Wykonaj w terminalu poniższą instrukcję:

```bash
python3 --version
```

Lub w przypadku Pythona starszego niż Python3;

```bash
python --version
```

## Tworzenie wirtualnego środowiska

Zalecane jest stworzenie wirtualnego środowiska, aby odizolować swoje zależności od globalnych pakietów Pythona.

Możesz to zrobić w jeden z następujących sposobów, w zależności od tego, na jakim systemie operacyjnym pracujesz:

### Windows

```bash
python3 -m venv venv

venv\Scripts\activate
```

### Linux (Debian/Ubuntu) i MacOS

```bash
python3 -m venv venv

source venv/bin/activate
```

## Klasa `User`

Jest to klasa reprezentująca użytkownika. Posiada takie atrybuty jak nazwa użytkownika, adres e-mail oraz rola. Posiada również konstruktor, który tworzy nowy obiekt klasy User ze wszystkimi niezbędnymi danymi.

---

### Atrybuty

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `username` | string | nazwa użytkownika |
| `email` | string | adres e-mail użytkownika |
| `role` | string | rola użytkownika |

---

### Metody

#### `get_data()`

Jest to metoda pozwalająca na uzyskanie danych użytkownika (nazwa, e-mail, rola) w postaci słownika. Nie przyjmuje żadnych parametrów.

#### Parametry

Metoda `get_data()` nie przyjmuje żadnych parametrów.

#### Zwracane dane

| Typ | Opis |
| --- | --- |
| dict | słownik zawierający dane użytkownika (nazwa, e-mail, rola) |

#### Przykładowe użycie

```python
user = User("Brian66", "brian66@outlook.com", "user")

user_data = user.get_data()

print(user_data)
```

#### Output

```python
{"username": "Brian66", "email": "brian66@outlook.com", "role": "user"}
```

---

### Przykładowe utworzenie obiektu klasy User

```python
user = User("John12", "john.smith@gmail.com", "admin")
```

---

## Klasa `UserManager`

Jest to klasa reprezentująca system zarządzania użytkownikami. Posiada wiele przydatnych metod, pozwalających na zarządzanie użytkownikami.

---

### Atrybuty

Klasa `UserManager` nie posiada żadnych atrybutów.

---

### Metody

#### `load_users()`

Jest to metoda pozwalająca na załadowanie użytkowników z pliku. Jeżeli plik z użytkownikami jest pusty, zwracana jest pusta lista.

#### Parametry

Metoda `load_users` nie przyjmuje żadnych parametrów.

#### Zwracane dane

| Typ | Opis |
| -- | -- |
| list | lista zawierająca dane użytkowników |

#### Przykładowe użycie

```python
users = UserManager.load_users()

for user in users:
    print(user)
```

#### Output

```python
{"username": "Brian66", "email": "brian66@outlook.com", "role": "user"}

{"username": "John12", "email": "john12@gmail.com", "role": "admin"}
```

---

#### `add_user(user)`

Jest to metoda pozwalająca na dodanie nowego użytkownika. **Uwaga!** W celu dodania użytkownika zalecane jest utworzenie obiektu klasy User z danymi, które nas interesują i pobranie danych tego użytkownika za pomocą metody `get_data()`, której wynik przekazujemy jako parametr do metody `add_user(user)`.

#### Parametry

| Nazwa | Typ | Opis |
| --- | --- | --- |
| user | dict | słownik zawierający dane użytkownika |

#### Zwracane dane

Metoda `add_user(user)` nie zwraca żadnych danych.

#### Przykładowe użycie

```python
user = User("michael123", "michael123@abc.com", "premium user")

user_data = user.get_data()

UserManager.add_user(user_data) # Do pliku users.json dodany został użytkownik z takimi danymi
```

---

#### `remove_user(username)`

Jest to metoda pozwalająca na usunięcie użytkownika z pliku na podstawie jego nazwy.

#### Parametry

| Nazwa | Typ | Opis |
| --- | --- | --- |
| username | string | nazwa użytkownika, którego chcemy usunąć |

#### Zwracane dane

Metoda `remove_user(username)` nie zwraca żadnych danych.

#### Przykładowe użycie

```python
UserManager.remove_user("john12") # Z pliku users.json usunięty zostaje użytkownik o nazwie "john12", o ile taki istnieje
```

---

#### `display_users()`

Jest to metoda pozwalająca na wyświetlenie danych wszystkich użytkowników.

#### Parametry

Metoda `display_users()` nie przyjmuje żadnych parametrów.

#### Zwracane dane

Metoda `display_users()` nie zwraca żadnych danych.

#### Przykładowe użycie

```python
UserManager.display_users()
```

#### Output

```python
Nazwa użytkownika: "abc"         Adres e-mail: "abc@abc.com"    Rola: "role_abc"
Nazwa użytkownika: "xyz"         Adres e-mail: "xyz@xyz.com"    Rola: "role_xyz"
```

---

#### `validate_email(email)`

Jest to metoda, która sprawdza według danego wzorca, czy adres e-mail jest poprawny.

#### Parametry

| Nazwa | Typ | Opis |
| --- | --- | --- |
| email | string | adres e-mail |

#### Zwracane dane

| Typ | Opis |
| -- | -- |
| bool | prawda/fałsz w zależności od tego, czy adres e-mail jest prawidłowy |

#### Przykładowe użycie

```python
nieprawidlowy_email = "email123"
prawidlowy_email = "abc.xyz@outlook.com"

print(UserManager.validate_email(nieprawidlowy_email))
print(UserManager.validate_email(prawidlowy_email))
```

#### Output

```python
False

True
```

---

#### `validate_username(username)`

Jest to metoda, sprawdzająca czy nazwa użytkownika jest poprawna.

#### Parametry

| Nazwa | Typ | Opis |
| --- | --- | --- |
| username | string | nazwa użytkownika |

#### Zwracane dane

| Typ | Opis |
| -- | -- |
| bool | prawda/fałsz w zależności od tego, czy nazwa użytkownika jest prawidłowa |

#### Przykładowe użycie

```python
nieprawidlowa_nazwa_uzytkownika = "       "
prawidlowa_nazwa_uzytkownika = "kacper1234"

print(UserManager.validate_username(nieprawidlowa_nazwa_uzytkownika))
print(UserManager.validate_username(prawidlowa_nazwa_uzytkownika))
```

#### Output

```python
False

True
```

---

#### `validate_role(role)`

Jest to metoda, sprawdzająca czy nazwa roli użytkownika jest poprawna.

#### Parametry

| Nazwa | Typ | Opis |
| --- | --- | --- |
| role | string | nazwa roli użytkownika |

#### Zwracane dane

| Typ | Opis |
| -- | -- |
| bool | prawda/fałsz w zależności od tego, czy nazwa roli jest prawidłowa |

#### Przykładowe użycie

```python
nieprawidlowa_rola_uzytkownika = "       "
prawidlowa_rola_uzytkownika = "admin"

print(UserManager.validate_username(nieprawidlowa_rola_uzytkownika))
print(UserManager.validate_username(prawidlowa_rola_uzytkownika))
```

#### Output

```python
False

True
```

---

#### `check_user(username)`

Jest to metoda, sprawdzająca, czy użytkownik o danej nazwie istnieje już w pliku.

#### Parametry

| Nazwa | Typ | Opis |
| --- | --- | --- |
| username | string | nazwa użytkownika |

#### Zwracane dane

| Typ | Opis |
| --- | --- |
| bool | prawda/fałsz w zależności od tego, czy użytkownik o określonej nazwie istnieje już w pliku

#### Przykładowe użycie

```python
# Załóżmy, że użytkownik "user1" istnieje w pliku user.json, a użytkownik "user2" nie

print(UserManager.check_user(user1))

print(UserManager.check_user(user2))
```

#### Output

```python
True

False
```

## Funkcja `main()`

Jest to funkcja odpowiadająca za główne działanie tego programu. Funkcja ta zapewnia prosty, lecz przejrzysty interfejs pozwalający na wybór opcji przez użytkownika. Oto wynik wywołania tej funkcji:

```bash
1 - Wyświetl użytkowników
2 - Dodaj użytkownika
3 - Usuń użytkownika
4 - Wyjdź

Wybierz opcję:
```

## Plik z użytkownikami
Użytkownicy są przechowywani domyślnie w pliku `users.json`. Plik ten zawiera dane użytkowników w formacie JSON. Oto przykładowa struktura pliku:

```json
[
    {"username": "Brian66", "email": "brian66@outlook.com", "role": "user"},
    {"username": "John12", "email": "john.smith@gmail.com", "role": "admin"}
]
```

## System logowania operacji

Program ten posiada funkcje logowania operacji wykonywanych podczas działania programu do pliku. Domyślnie zapisywane są one do pliku o nazwie `logs.log`. Oto przykładowa struktura pliku:

```text
2025-01-26 21:52:17,605 - INFO - Program został uruchomiony.
2025-01-26 21:52:19,471 - INFO - Wybrano opcję wyświetlenia danych użytkowników.
2025-01-26 21:52:19,472 - ERROR - Nie udało się wyświetlić użytkowników. Nie znaleziono żadnych użytkowników w pliku.
2025-01-26 21:52:20,318 - INFO - Wybrano opcję dodania nowego użytkownika.
2025-01-26 21:52:21,351 - DEBUG - Wprowadzono nazwę użytkownika: "abc".
2025-01-26 21:52:21,351 - DEBUG - Walidacja wprowadzonej nazwy użytkownika "abc" przebiegła pomyślnie.
2025-01-26 21:52:24,007 - DEBUG - Wprowadzono adres e-mail użytkownika: "abc@abc.com".
2025-01-26 21:52:24,007 - DEBUG - Walidacja wprowadzonego adresu e-mail "abc@abc.com" przebiegła pomyślnie.
2025-01-26 21:52:26,264 - DEBUG - Wprowadzono rolę użytkownika: "role".
2025-01-26 21:52:26,264 - DEBUG - Walidacja wprowadzonej roli "role" przebiegła pomyślnie.
2025-01-26 21:52:26,264 - INFO - Utworzono obiekt klasy User z danymi: username: "abc"; email: "abc@abc.com"; role: "role".
2025-01-26 21:52:26,265 - INFO - Dodano nowego użytkownika o nazwie "abc".
2025-01-26 21:52:27,145 - INFO - Wybrano opcję wyjścia z programu.
2025-01-26 21:52:27,145 - INFO - Zakończono działanie programu.

```

## Best practices

- Upewniaj się, że plik z danymi użytkowników nie jest uszkodzony
- Uważaj, aby wprowadzane przez Ciebie dane były prawidłowe
- Zwracaj uwagę na to, czy dodawani użytkownicy nie istnieją już w pliku
- Dodając nowego użytkownika, używaj metody `get_data()`, aby pobrać dane danego użytkownika i przekazać je do metody `add_user(user)`

## Możliwości rozszerzenia programu

1. Dodanie opcji modyfikacji danych użytkowników
2. Dodanie opcji dodawania/usuwania kilku użytkowników na raz
3. Dodanie opcji wyświetlania danych tylko konkretnego użytkownika
4. Dodanie opcji wysyłania maila na podany adres użytkownika po dodaniu go do pliku
