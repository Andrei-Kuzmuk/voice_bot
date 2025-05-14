from gtts import gTTS


def text_to_speech(text, output_filename, language="ru"):
    # Озвучивает текст с помощью gTTS и сохраняет в MP3-файл.
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_filename)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        print("Убедитесь, что у вас есть подключение к интернету.")


def test() -> None:
    # Пример использования
    text = "Привет, это пример озвучивания с использованием gTTS (только MP3)."
    text_to_speech(text, "my_audio.mp3")


if __name__ == "__main__":
    test()
