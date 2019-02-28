import concurrent.futures
import zipfile
import re

filenames = [
    'ex2_1.zip',
    'ex2_2.zip',
    'ex2_3.zip',
    'ex2_4.zip',
    'ex2_5.zip', ]


def read_data(filename):
    total = 0
    with zipfile.ZipFile(filename) as zipfp:
        with zipfp.open(zipfp.namelist()[0], 'r') as fp:
            for a_line in fp.readlines():
                a_line = a_line.decode('utf-8')
                for number in re.finditer(r'(\d+(\.?\d*)|\.\d+)', a_line):
                    total += float(number.group())
    return total


def main():
    sum = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for total in executor.map(read_data, filenames):
            sum += total

        print(sum)


if __name__ == '__main__':
    main()
