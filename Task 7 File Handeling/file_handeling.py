def find_and_replace(filename, find_word, replace_word):
    try:
        # Read content from file
        with open(filename, 'r') as file:
            content = file.read()

        # Show original content preview
        print("\nOriginal Content Preview:")
        print(content[:200], "...\n")

        # Replace word(s)
        modified_content = content.replace(find_word, replace_word)

        # Write modified content back to file
        with open(filename, 'w') as file:
            file.write(modified_content)

        print(f"✅ All occurrences of '{find_word}' replaced with '{replace_word}' successfully!")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print("❌ Error: Permission denied while accessing the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def main():
    print("📝 Basic File Handling – Find and Replace\n")
    filename = input("Enter the name of the text file (with .txt extension): ")

    find_word = input("Enter the word you want to find: ")
    replace_word = input("Enter the word you want to replace it with: ")

    find_and_replace(filename, find_word, replace_word)

main()