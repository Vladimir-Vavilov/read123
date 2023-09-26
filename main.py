import os

def merge_files(file_paths, result_file):
    files_with_line_counts = [(sum(1 for line in open(file_path, 'r')), file_path) for file_path in file_paths]
    sorted_files = sorted(files_with_line_counts, key=lambda x: x[0])
    with open(result_file, 'w') as result:
        for line_count, file_path in sorted_files:
            result.write(f'Имя файла: {os.path.basename(file_path)}\n')
            result.write(f'Строк в файле: {line_count}\n')
            with open(file_path, 'r') as source_file:
                for line in source_file:
                    result.write(line)
                    result.write('\n')

merge_files(['1.txt', '2.txt', '3.txt'], 'result.txt')

with open('result.txt', 'r') as f:
    print(f.read())