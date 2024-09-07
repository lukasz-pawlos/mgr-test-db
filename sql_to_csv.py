import re
import csv
import os

def sql_copy_to_csv(sql_file, base_output_folder):
    print(f"Przetwarzanie pliku: {sql_file}")
    
    # Wyciąganie nazwy pliku bez rozszerzenia i generowanie ścieżki do podkatalogu
    file_name = os.path.basename(sql_file)
    file_name_without_ext = os.path.splitext(file_name)[0]  # Nazwa pliku bez ".sql"
    
    # Podział nazwy pliku na części po spacjach i utworzenie ścieżki do katalogu
    directory_name = " ".join(file_name_without_ext.split("_")[2:])  # Pobieramy wszystko po "logdatabase_test_"
    output_folder = os.path.join(base_output_folder, directory_name)

    # Tworzenie katalogu, jeśli nie istnieje
    os.makedirs(output_folder, exist_ok=True)
    print(f"Zapis do katalogu: {output_folder}")
    
    # Czytanie pliku SQL
    try:
        with open(sql_file, 'r', encoding='utf-8') as file:
            sql_data = file.read()
            print(f"Plik {sql_file} został wczytany.")
    except Exception as e:
        print(f"Błąd podczas otwierania pliku: {e}")
        return

    # Wyszukiwanie poleceń COPY
    copy_statements = re.findall(r"COPY (\w+\.\w+) \((.*?)\) FROM stdin;\n(.*?)(?=\\\.)", sql_data, re.DOTALL)
    print(f"Znaleziono {len(copy_statements)} poleceń COPY.")

    # Przetwarzanie każdej komendy COPY
    for table_name, columns, values in copy_statements:
        print(f"Przetwarzanie tabeli: {table_name}")
        
        # Przygotowanie nagłówków
        columns_list = [col.strip().strip('"') for col in columns.split(",")]
        
        # Przygotowanie danych
        rows = [row.split("\t") for row in values.strip().split("\n")]
        
        # Tworzenie ścieżki do pliku CSV
        csv_file = os.path.join(output_folder, f"{table_name.split('.')[1]}.csv")
        
        # Zapis danych do pliku CSV
        try:
            with open(csv_file, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                
                # Zapis nagłówków
                writer.writerow(columns_list)
                
                # Zapis danych
                writer.writerows(rows)
            
            print(f"Zapisano dane do: {csv_file}")
        except Exception as e:
            print(f"Błąd podczas zapisywania pliku CSV: {e}")

# Wywołanie funkcji dla przykładowych plików
# Zakładamy, że masz katalogi test1, test2, test3, które zawierają pliki SQL
for folder in ['test2','test3']:
    folder_path = folder  # lub pełna ścieżka do folderu
    for sql_file in os.listdir(folder_path):
        if sql_file.endswith(".sql"):
            sql_file_path = os.path.join(folder_path, sql_file)
            sql_copy_to_csv(sql_file_path, folder_path)
