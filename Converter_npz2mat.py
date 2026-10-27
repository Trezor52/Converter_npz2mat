import os

try:
    import numpy as np
except ImportError:
    print("Ошибка: не удалось загрузить библиотеку 'numpy'")

try:
    from scipy.io import savemat
except ImportError:
    print("Ошибка: не удалось загрузить библиотеку 'scipy'")

def convert_npz_2_mat(npz_file_full_path: str) -> str:

    if not os.path.isfile(npz_file_full_path):
        raise FileNotFoundError('Файл не найден!')

    with np.load(npz_file_full_path, allow_pickle=True) as npz:
        data = {key: npz[key] for key in npz.files}

    mat_path = os.path.splitext(npz_file_full_path)[0] + ".mat"
    savemat(mat_path, data)

    print('Готово! Файл .mat сохранен в ту же директорию')

if __name__ == '__main__':

    input_path = input('Введите полный путь до файла .npz: ')
    convert_npz_2_mat(input_path)