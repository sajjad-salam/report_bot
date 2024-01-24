import telebot
from fpdf import FPDF
from io import BytesIO
from transformers import pipeline, set_seed

TOKEN = '6938276707:AAH0-NfQ92Fm91hpJv-a5RE8hCnuSFIcX5E'  # Replace with your token
bot = telebot.TeleBot(TOKEN)
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
def generate_report(title):
    prompt = f"Write a professional report on {title} including Introduction, Purpose of the Report, Standard Specifications, Steps of Work, Calculations, and Discussion."
    results = generator(prompt, max_length=500, num_return_sequences=1)
    return results[0]['generated_text']



report = generate_report("Climate Change")
print(report)


def create_pdf(content):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=14)
    for title, text in content.items():
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, title, ln=True, align='C')
        pdf.set_font("Arial", size=14)
        pdf.multi_cell(0, 10, text)
    pdf_content = pdf.output(dest='S').encode('latin-1')  # Get PDF content as a string
    pdf_file = BytesIO(pdf_content)  # Write PDF content to BytesIO object
    pdf_file.name = "report.pdf"  # Set a name for the in-memory file
    return pdf_file

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Send me the title of the report.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    title = message.text
    pdf_content = generate_report(title)
    pdf_file = create_pdf(pdf_content)
    pdf_file.name = "report.pdf"
    bot.send_document(message.chat.id, pdf_file)

bot.polling(timeout=60)  # Increase timeout to 60 seconds
