import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("Ошибка: не указан путь к файлу.", file=sys.stderr)
        print("Использование: uv run main.py <путь_к_файлу> [путь_к_выходному_файлу]", file=sys.stderr)
        sys.exit(1) 

    file_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    stats = {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                station, temp_str = line.rsplit(";", 1)
                temp = float(temp_str)

                if station not in stats:
                    stats[station] = [temp, temp, temp, 1]
                else:
                    if temp < stats[station][0]:
                        stats[station][0] = temp
                    if temp > stats[station][1]:
                        stats[station][1] = temp
                    stats[station][2] += temp
                    stats[station][3] += 1
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.", file=sys.stderr)
        sys.exit(1) 

    sorted_stations = sorted(stats.keys())
    results = []

    for station in sorted_stations:
        min_temp, max_temp, total_temp, count = stats[station]
        mean_temp = total_temp / count
        results.append(f"{station};{min_temp:.1f};{mean_temp:.1f};{max_temp:.1f}")

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            for res in results:
                f.write(res + "\n")
        print(f"Результат успешно сохранен в {output_path}")
    else:
        for res in results:
            print(res)

if __name__ == "__main__":
    main()