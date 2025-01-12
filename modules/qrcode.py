import qrcode
import os

# qr = qrcode.QRCode(
#     version=10, # число от 1 до 40, отвечающее за размер поля QR-кода. Единица задает матрицу 21 на 21 квадрат. None позволяет автоматически подстраивать размер.
#     error_correction=qrcode.constants.ERROR_CORRECT_H,  # определяет избыточность QR-кода, допустимый процент ошибок. Варьируется от 7% (ERROR_CORRECT_L) до 30% (ERROR_CORRECT_H), по умолчанию - 15%.
#     box_size=8, # размер квадратов в пикселях
#     border=4,  # определяет толщину границы. Не может быть меньше 4 (значение по умолчанию).
# )

def func_qr_generator(data_xml: dict):
  directory_qr_imgs = str(os.getcwd()) + '/qr_imgs'

  for k, i in data_xml.items():
    name_png = i.get('Сетевое имя')
    qr = qrcode.QRCode(version=1, box_size=5, border=1)

    for key, value in i.items():
      result = f"{key}: {value}\n"
      qr.add_data(result)
      #qr.add_data(json.dumps(result, indent=4, ensure_ascii=False))
    try:
      qr.make(fit=True)
      qr.make_image().save(os.path.join(directory_qr_imgs, f'{name_png}.png'))
    except Exception as error:
      #print(error)
      print(f"Файл {k}.png не удалось сохранить.")
