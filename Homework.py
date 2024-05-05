# Завдання 2
# Створіть програму для проведення опитування або
# анкетування. Зберігайте відповіді користувачів у форматі
# JSON файлу. Кожне опитування може бути окремим
# об'єктом у файлі JSON, а відповіді кожного користувача -
# списком значень.

import json


def conduct_survey(question, answer_options):
    print(question)
    for i, version in enumerate(answer_options, 1):
        print(f"{i}. {version}")
    choice = int(input("Виберіть номер відповіді: "))
    while choice not in range(1, len(answer_options) + 1):
        choice = int(input("Невірний номер. Виберіть номер відповіді ще раз: "))
    return choice


def save_answers(answers, filename):
    with open(filename, 'w') as file:
        json.dump(answers, file)


def download_survey(filename):
    with open(filename, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    poll = {
        "питання": "Яка ваша улюблена мова програмування?",
        "варіанти_відповідей": ["Python", "Java", "JavaScript", "C++", "Інша"]
    }

    answers  = []

    print("Вас вітає програма для проведення опитування!")

    number_participants = int(input("Скільки учасників буде проходити опитування? "))

    for member in range(1, number_participants + 1):
        print(f"\nУчасник {member}:")
        answers = conduct_survey(poll["питання"], poll["варіанти_відповідей"])
        answers.append(answers)

    save_answers(answers, "відповіді.json")
    print("Ваші відповіді було збережено у файлі 'відповіді.json'.")
