import os
import google.generativeai as genai
from utils.pdf_utils import validate_and_read_pdf

# Load API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise EnvironmentError("Missing GOOGLE_API_KEY. Please set it as an environment variable.")

# Configure model
genai.configure(api_key=GOOGLE_API_KEY)

model_config = {
    "temperature": 0.2,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=model_config,
    safety_settings=safety_settings
)

def analyze_receipt(pdf_path, question):
    pdf_data = validate_and_read_pdf(pdf_path)

    system_prompt = """
    You are a specialist in comprehending receipts and invoices.
    The PDF provided contains receipt information.
    """

    input_prompt = [system_prompt, pdf_data[0], question]
    response = model.generate_content(input_prompt)
    return response.text

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_path", help="Path to the PDF receipt")
    args = parser.parse_args()

    print("Example: Convert invoice to JSON or ask a question")
    user_question = input("Enter your prompt: ")
    output = analyze_receipt(args.pdf_path, user_question)
    print("\nGenerated Output:\n")
    print(output)