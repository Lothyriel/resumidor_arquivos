import openai
import dotenv
import os

class Resumer:
    def __init__(self) -> None:
        openai.api_key = dotenv.get_key(".env","API_KEY")

    def resume_file(self, file_name):
        file_path = os.path.join("cap", file_name)
        with open(file_path, 'r', encoding="utf8") as file:
            text = file.read()

        slice_size = 10000
        print(file_name)

        for i in range(0, len(text), slice_size):
            slice_text = text[i:i+slice_size]

            output_path = os.path.join("output", file_name)
            print(output_path)
            self.resume_slice(slice_text, output_path)

    def resume_slice(self, slice_text, output_path):
        response_chat_gpt = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você resume textos em português"},
                    {"role": "user", "content": slice_text},
                ]
            )

        response = ''
        for choice in response_chat_gpt.choices:
            response += choice.message.content

        with open(output_path, 'a') as file:
            file.write(response)
