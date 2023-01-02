import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("LogSearcher")
print(ascii_banner)

log_files = sys.argv[1:]

for log_file in log_files:

    with open(log_file, "r") as f:

        for line in f:
            if "KEYWORD" in line:
                print(line)
