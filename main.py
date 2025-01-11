import os
from modules.qrcode import func_qr_generator
from modules.openxml import exel_tabl


def main():
    directorys = ['xml_files', 'qr_imgs']

    for directory in directorys:
        directory_path = str(os.getcwd() + '/' + directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    try:
        data_xml = exel_tabl()
        if data_xml != False:
            func_qr_generator(data_xml)

    except FileNotFoundError:
        print("Ошибка: файл не найден")
    except KeyError:
        print("Ошибка: отсутствуют необходимые столбцы в DataFrame")


if __name__ == '__main__':
    print('START')
    main()


