# Метод Гауса.
def gauss(matrixA=list, vectorB=list) -> None:
    n = len(matrixA)  # Кількість рядків у матриці
    x = [0.0] * n  # Вектор розв'язку

    for k in range(n - 1):
        print("\nЕтап", k + 1, ":")

        # Виведення початкового стану матриці A і вектора b
        print("Матриця A:")
        for i in range(n):
            for j in range(n):
                print("{:7.3f}".format(matrixA[i][j]), end="   ")
            print(" |", vectorB[i])

        for i in range(k + 1, n):
            factor = matrixA[i][k] / matrixA[k][k]
            for j in range(k, n):
                matrixA[i][j] -= factor * matrixA[k][j]
            vectorB[i] -= factor * vectorB[k]

        # Виведення оновленого стану матриці A і вектора b після елімінації Гауса
        print("\nОновлена матриця A та вектор b після етапу", k + 1, ":")
        for i in range(n):
            for j in range(n):
                print("{:7.3f}".format(matrixA[i][j]), end="   ")
            print(" |", vectorB[i])

    # Зворотний хід
    for i in range(n - 1, -1, -1):
        x[i] = vectorB[i]
        for j in range(i + 1, n):
            x[i] -= matrixA[i][j] * x[j]
        x[i] /= matrixA[i][i]

    print("\nЗнайдені розв'язки:")
    for i in range(n):
        print("x[{}] = {:.3f}".format(i, x[i]))

# Метод Гауса-Жордана.
def gauss_jordan_with_steps(matrixA=list, vectorB=list) -> None:
    n = len(matrixA)

    print("Початкова матриця A:")
    print_matrix(matrixA)
    print("Початковий вектор B:")
    print_vector(vectorB)
    print("-------------------------------")

    # Прямий хід методу Гауса-Жордана.
    for i in range(n):
        pivot = matrixA[i][i]
        print(
            f"Ділимо рядок {i + 1} на {pivot} для отримання одиниці в головному діагональному елементі A[{i + 1}][{i + 1}]")
        for j in range(i, n):
            matrixA[i][j] /= pivot
        vectorB[i] /= pivot

        print(f"Матриця A після кроку {i + 1}:")
        print_matrix(matrixA)
        print(f"Вектор B після кроку {i + 1}:")
        print_vector(vectorB)
        print("-------------------------------")

        for k in range(n):
            if k != i:
                factor = matrixA[k][i]
                print(
                    f"Віднімаємо {factor} * рядок {i + 1} від рядку {k + 1} для зроблення нуля під головним діагональним елементом A[{k + 1}][{i + 1}]")
                for j in range(i, n):
                    matrixA[k][j] -= factor * matrixA[i][j]
                vectorB[k] -= factor * vectorB[i]

                print(f"Матриця A після кроку {i + 1}:")
                print_matrix(matrixA)
                print(f"Вектор B після кроку {i + 1}:")
                print_vector(vectorB)
                print("-------------------------------")

# Вивід матриці для Методу Гауса-Жордана.
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:.3f}", end="   ")
        print()

# Вивід вектора для Методу Гауса-Жордана.
def print_vector(vector):
    for element in vector:
        print(f"{element:.3f}")

# Заміна ряду, якщо діагональний елемент рівний нулю.
def move_rows_if_diagonal_zero(matrixA=list, vectorB=list) -> None:
    n = len(matrixA)

    for i in range(n):
        if matrixA[i][i] == 0:
            # Знаходимо індекс рядка, де на головній діагоналі 0
            j = i + 1
            while j < n and matrixA[j][i] == 0:
                j += 1

            # Переміщуємо рядок j на позицію i в матриці matrix_a
            matrixA[i], matrixA[j] = matrixA[j], matrixA[i]

            # Переміщуємо відповідний елемент вектора vector_b
            vectorB[i], vectorB[j] = vectorB[j], vectorB[i]

# Функція використання методів.
def use_method(key=int) -> None:
    matrixA = [
        [-4, 13, 5, 19, 6],
        [-10, 21, 1, -13, -2],
        [-15, -20, 14, 21, -12],
        [21, -16, -18, 19, 13],
        [-13, 5, 19, 23, 9]
    ]

    vectorB = [16, 9, 2, -3, 16]

    move_rows_if_diagonal_zero(matrixA, vectorB)
    lineMethod = "=" * 160
    print(lineMethod)
    match key:
        case 1:
            print("Метод Гауса")
            gauss(matrixA, vectorB)
        case 2:
            print("Метод Гауса-Жордана")
            gauss_jordan_with_steps(matrixA, vectorB)
        case _:
            raise Exception("Погано вибраний метод в use_method")
    print(lineMethod)

# Програма виконання.
if __name__ == "__main__":
    print("Програму розробив студент групи ОІ-11 сп, Вальчевський П. В. для варіанту № 3 (згідно списку в журналі) ЛР № 3 з Чисельних методів")
    use_method(1)
    use_method(2)
