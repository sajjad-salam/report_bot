# Telegram Report Generator

منشء تقارير اعتمادا على نموذج ذكاء اصطناعي gpt2

## المتطلبات

- Python 3.x
- `telebot` library
- `fpdf` library
- `transformers` library

يمكنك تثبيت كل المتطبات من خلال هذا الأمر:

```bash
pip install pyTelegramBotAPI fpdf transformers
```

## Usage

1. Clone or download the repository.
2. Run the script using Python:

```bash
python report_generator.py
```

3. Input your Telegram bot token when prompted.
4. Start a conversation with your bot and send the desired report title.
5. The bot will generate the report and send it back to you in PDF format.

## Functionality Overview

- The script initializes a Telegram bot using the provided token.
- It sets up message handlers to respond to `/start` and `/help` commands with instructions.
- Upon receiving a message (presumably the report title), the script generates the report using a GPT-2 model.
- The generated report is then sent back to the user in PDF format.

## Important Notes

- A stable internet connection is required for the script to communicate with the Telegram API and the Hugging Face model server.
- Depending on the length of the generated report, the process may take some time.
- Feel free to customize the script according to your specific requirements and use case!
