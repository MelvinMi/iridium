import sys
import time

stats = {}
total_messages = 0
last_print_time = time.time()

def print_dashboard():
    global stats, total_messages
    if total_messages == 0:
        return

    output_parts = []
    for msg_type, count in sorted(stats.items()):
        percentage = (count / total_messages) * 100
        output_parts.append(f"{msg_type}: {percentage:.1f}%")

    dashboard_line = " | ".join(output_parts)

    # L'astuce est le '\r' au début et end='' à la fin : 
    # Ça force le curseur à revenir au début de la MÊME ligne pour écraser l'ancien texte
    print(f"\r[RÉPARTITION LIVE] (Total: {total_messages}) -> {dashboard_line}", file=sys.stderr, end='', flush=True)

for line in sys.stdin:
    clean_line = line.strip()
    if not clean_line:
        continue


    parts = clean_line.split()
    if not parts:
        continue
    first_word = parts[0]

    if ":" in first_word:
        msg_type = first_word.replace(":", "")

        stats[msg_type] = stats.get(msg_type, 0) + 1
        total_messages += 1

        current_time = time.time()

        if current_time - last_print_time >= 1.0:
            print_dashboard()
            last_print_time = current_time
