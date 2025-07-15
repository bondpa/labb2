# Använder argparse för att hantera kommandoradsalternativ 
# och utför följande funktioner:
# 1. Krypterar en fil med en befintlig nyckel.
# 2. dekrypterar en krypterad fil och återställer originalet

import argparse

def encrypt(file_path, key):
    print(f"Krypterar {file_path} med nyckeln {key}")
    

def decrypt(file_path, key):
    print(f"Dekrypterar {file_path} med nyckeln {key}")


def main():
    parser = argparse.ArgumentParser(description="Kryptera eller dekryptera fil")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Kryptera eller dekryptera filen")
    parser.add_argument("file", help="Sökväg till filen")
    parser.add_argument("key", default="secret.key", help="Sökväg till nyckeln")

    args = parser.parse_args()

    if args.action == "encrypt":
        encrypt(args.file, args.key)
    elif args.action == "decrypt":
        decrypt(args.file, args.key)


if __name__ == "__main__":
    main()