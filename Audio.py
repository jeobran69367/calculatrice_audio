import speech_recognition as sr
from gtts import gTTS
import os



# Créez un objet recognizer
recognizer = sr.Recognizer()

# Un dictionnaire pour faire correspondre les mots aux chiffres
word_to_number = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def convert_words_to_numbers(text):
    # Convertit les mots en chiffres
    words = text.split()
    converted_words = []
    for word in words:
        if word.lower() in word_to_number:
            converted_words.append(word_to_number[word.lower()])
        else:
            converted_words.append(word)
    return ' '.join(converted_words)


def get_operations():
    while True:
        with sr.Microphone() as source:
            print("Speak your operations...")
            try:
                # Enregistrez les données audio
                audio_data = recognizer.listen(source, timeout=5)
                # Convertissez la parole en texte
                text = recognizer.recognize_google(audio_data, language='en-US')
                print(f"Recognized text: {text}")  # Ajout de cette ligne pour afficher la transcription
                return text
            except sr.WaitTimeoutError:
                print("Timeout: No speech detected. Please try again.")
            except sr.UnknownValueError:
                print("Speech not recognized. Please try again.")
            except sr.RequestError as e:
                print(f"Error with the service; {e}. Please try again.")

def convert_words_to_numbers(text):
    # Convertit les mots en chiffres
    words = text.split()
    for i, word in enumerate(words):
        if word.lower() in word_to_number:
            words[i] = word_to_number[word.lower()]
    return ' '.join(words)

def calculate_results(operations):
    results = []
    # Supprimez tous les espaces et séparez les opérations par le signe "+"
    operation_list = operations.replace(" ", "").split('+')
    
    for operation in operation_list:
        try:
            result = eval(operation)
            results.append(result)
        except (ValueError, SyntaxError):
            print(f"Invalid operation: {operation}. Skipping it.")
    
    return results



def speak_results(results):
    if results:
        total_result = sum(results)
        tts = gTTS(f'Total result: {total_result}')
        tts.save("result.mp3")
        os.system("start result.mp3")
    else:
        print("No valid results to speak.")


# Programme principal
if __name__ == "__main__":
    while True:
        operations = get_operations()
        if operations:
            results = calculate_results(operations)
            speak_results(results)
        else:
            print("No valid operations detected. Please try again.")
