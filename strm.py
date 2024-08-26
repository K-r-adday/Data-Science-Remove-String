import sys

def remove_specific_string(input_file, output_file, string_to_remove):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            cleaned_line = line.replace(string_to_remove, '')
            file.write(cleaned_line)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python strm.py <input_file> <output_file> <string_to_remove>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        string_to_remove = sys.argv[3]
        remove_specific_string(input_file, output_file, string_to_remove)
