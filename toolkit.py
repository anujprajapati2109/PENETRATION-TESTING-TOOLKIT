from modules import port_scanner, brute_forcer

def main():
    while True:
        print("\n=== Penetration Testing Toolkit ===")
        print("1. Port Scanner")
        print("2. Brute Force Simulator")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            port_scanner.run()
        elif choice == '2':
            brute_forcer.run()
        elif choice == '3':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
