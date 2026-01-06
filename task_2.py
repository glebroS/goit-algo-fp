import turtle


def draw_tree(t, branch_len, level):
    if level == 0:
        return

    # Малюємо стовбур
    t.forward(branch_len)

    # Зберігаємо позицію та кут
    pos = t.pos()
    heading = t.heading()

    # Ліва гілка
    t.left(45)
    draw_tree(t, branch_len * 0.7, level - 1)

    # Відновлюємо позицію та кут
    t.setheading(heading)
    t.setpos(pos)

    # Права гілка
    t.right(45)
    draw_tree(t, branch_len * 0.7, level - 1)

    # Відновлюємо позицію та кут (на всяк випадок)
    t.setheading(heading)
    t.setpos(pos)


def main():
    # Отримання рівня рекурсії від користувача
    recursion_level = 0
    while True:
        try:
            val = input("Введіть рівень рекурсії (рекомендовано 5-10): ")
            recursion_level = int(val)
            if recursion_level >= 0:
                break
            else:
                print("Будь ласка, введіть невід'ємне ціле число.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    # Налаштування екрану та черепашки
    screen = turtle.Screen()
    screen.title("Фрактал 'Дерево Піфагора'")

    t = turtle.Turtle()
    t.speed('fastest')  # Максимальна швидкість малювання
    t.left(90)          # Повертаємо черепашку вгору
    t.up()
    t.goto(0, -200)     # Початкова позиція внизу екрану
    t.down()

    # Виклик функції малювання
    draw_tree(t, 100, recursion_level)

    print("Малювання завершено. Клікніть на вікно, щоб закрити.")
    screen.exitonclick()


if __name__ == "__main__":
    main()
