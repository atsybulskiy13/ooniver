from task_01 import convert_to_normal_view


def compare_files(file1, file2):

    if file1 == file2:

        print('Files are the same!')

    else:

        for list_index in range(len(file1)):

            if file1[list_index] != file2[list_index]:

                for elem_index in range(len(file1[list_index])):

                    if file1[list_index][elem_index] != file2[list_index][elem_index]:

                        print(f'Strings N{list_index + 1} are different!')
                        print(f'Symbols N{elem_index + 1} from {list_index + 1} string are different!')
                        print(f'String N{list_index + 1} from first file - "{file1[list_index]}"')
                        print(f'String N{list_index + 1} from second file - "{file2[list_index]}"')
                        print()


def main():

    file1 = convert_to_normal_view('file1.txt')

    file2 = convert_to_normal_view('file2.txt')

    compare_files(file1, file2)


if __name__ == '__main__':
    main()
