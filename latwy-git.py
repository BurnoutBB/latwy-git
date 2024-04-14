import os

def display_git_folders():
    git_folders = []
    for root, dirs, files in os.walk(".", topdown=True):
        if ".git" in dirs:
            git_folders.append(root)
    return git_folders

def main_menu():
    while True:
        print("=" * 35)
        print()
        git_folders = display_git_folders()
        if not git_folders:
            print("Brak folderów zawierających .git.")
            return
        print("Dostępne repozytoria:")
        for idx, folder in enumerate(git_folders, start=1):
            print(f"{idx}. {os.path.basename(folder)}")
        print()
        choice = input("Wybierz numer repozytorium lub wpisz 'q' aby wyjść: ")
        if choice.lower() == "q":
            return
        try:
            choice = int(choice)
            if choice < 1 or choice > len(git_folders):
                raise ValueError
            return git_folders[choice - 1]
        except ValueError:
            print("Niepoprawny wybór. Wpisz numer repozytorium lub 'q' aby wyjść.")

def execute_action(folder):
    os.chdir(folder)
    while True:
        print("=" * 35)
        print()
        print("Co chcesz zrobić:")
        print("1. Pull")
        print("2. Push")
        print("3. Commit")
        print("4. Add")
        print("5. Branch")
        print("6. Klonuj")
        print("7. Powrót")
        print()
        choice = input("Wybierz numer czynności lub 'q' aby wyjść: ")
        if choice.lower() == "q":
            return
        if choice == "1":
            os.system("git pull")
        elif choice == "2":
            os.system("git push")
        elif choice == "3":
            message = input("Wpisz komunikat do commita: ")
            os.system(f"git commit -m \"{message}\" -a")
        elif choice == "4":
            os.system("git add .")
        elif choice == "5":
            print("=" * 35)
            print()
            print("Dostępne branch'e:")
            print("1. dev")
            print("2. main")
            print("3. beta")
            print()
            branch_choice = input("Wybierz numer branch'a: ")
            if branch_choice == "1":
                os.system("git checkout dev")
            elif branch_choice == "2":
                os.system("git checkout main")
            elif branch_choice == "3":
                os.system("git checkout beta")
            else:
                print("Niepoprawny wybór branch'a.")
        elif choice == "6":
            link = input("Wpisz link do repozytorium do sklonowania: ")
            os.chdir("..")
            os.system(f"git clone {link}")
        elif choice == "7":
            os.chdir("..")
            return

if __name__ == "__main__":
    while True:
        repo_folder = main_menu()
        if not repo_folder:
            print("Nie znaleziono folderów zawierających .git. Zakończono program.")
            break
        execute_action(repo_folder)
