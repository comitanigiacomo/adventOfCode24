import json

README_FILE = "README.md"
PROGRESS_FILE = "progress.json"

def load_progress(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_table(progress):
    table_header = "| Day | Part 1 | Part 2 | Solution Link |\n"
    table_header += "|-----|--------|--------|---------------|\n"

    table_rows = ""
    for day in range(1, 26):
        day_str = str(day)
        if day_str in progress:
            part1 = "⭐" if progress[day_str]["part1"] else "⚪"
            part2 = "⭐" if progress[day_str]["part2"] else "⚪"
            link = progress[day_str]["link"]
            link_cell = f"[Solution]({link})" if link else ""
        else:
            part1 = part2 = "⚪"
            link_cell = ""
        
        table_rows += f"| {day}   | {part1}      | {part2}      | {link_cell} |\n"
    return table_header + table_rows

# Aggiorna il README
def update_readme(readme_path, table_content):
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    start_marker = "### Advent of Code Progress Tracker 📅"
    end_marker = "|-----|--------|--------|---------------|"

    # Trova l'inizio della sezione e la fine della tabella esistente
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if start_marker in line:
            start_index = i
        if start_index is not None and end_marker in line and i > start_index:
            end_index = i
            break

    # Rimuovi la tabella esistente (se presente)
    if start_index is not None and end_index is not None:
        lines = lines[:start_index + 1]  # Mantieni la sezione, ma rimuovi la tabella
    else:
        # Se la sezione non esiste, aggiungiamola all'inizio
        lines.append("\n### Advent of Code Progress Tracker 📅\n")

    # Aggiungi la nuova tabella
    lines.append(table_content)

    # Scrivi il file aggiornato
    with open(readme_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    progress = load_progress(PROGRESS_FILE)

    new_table = generate_table(progress)

    update_readme(README_FILE, new_table)
    print("README updated successfully!")
