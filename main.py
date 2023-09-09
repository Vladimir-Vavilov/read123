import os


def merge_files(file_paths, result_file_path):
    files_with_line_counts = [(sum(1 for line in open(file_paths, 'r')), file_path) for file_path in file_paths]
    sorted_files = sorted(files_with_line_counts, key=lambda x: x[0])
    with open(result_file_path, 'w') as result_file:
        for line_count, file_path in sorted_files:
            result_file.write(f'File Name: {os.path.basename(file_path)}\n')
            result_file.write(f'Line Count: {line_count}\n')
            with open(file_path, 'r') as source_file:
                for line in source_file:
                    result_file.write(line)
                    result_file.write('\n')



merge_files(['1.txt', '2.txt', '3.txt'], 'result.txt')


with open('result.txt', 'r') as f:
    print(f.read())