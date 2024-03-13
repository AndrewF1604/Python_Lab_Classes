import os


def list_files(directory):
    try:
        # Lista na przechowywanie ścieżek do plików
        files_list = []

        # Przechodzenie przez katalog i podkatalogi rekurencyjnie
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                # Pełna ścieżka do pliku
                file_path = os.path.join(foldername, filename)
                # Dodanie ścieżki do listy plików
                files_list.append(file_path)

        # Wyświetlenie listy plików
        print("Lista plików:")
        for file_path in files_list:
            print(file_path)

    except Exception as e:
        print(f"Błąd: {e}")


# Ścieżka do katalogu, którego pliki chcemy wypisać (np. /path/to/directory)
#directory_path = "C:\Windows\Panther"
a
# Wywołanie funkcji list_files
list_files("C:\Windows\Panther")