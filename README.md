# 🧾 Gemini Receipt Analyzer

This project uses **Google's Gemini 1.5 Flash** model to extract structured data from PDF receipts and invoices. It's designed to help recruiters, developers, and businesses convert unstructured financial documents into meaningful JSON or answer user queries based on receipt content.

---

## 🚀 Features

- ✅ Uses **Gemini 1.5 Flash** for high-speed content generation.
- ✅ Accepts **PDF receipts/invoices** as input.
- ✅ Converts receipt content into **structured JSON**.
- ✅ Allows natural language **Q&A on receipts**, e.g., "What is the quantity of Avobenzone?"
- ✅ Modular and scalable with separate utils and main logic.

---

## 📁 Project Structure

gemini-receipt-analyzer/
│
├── main.py                    # Main script: loads Gemini model & runs prompts
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── utils/
│   └── pdf_utils.py           # PDF validation and reading logic
│
└── sample_receipts/
    └── invoice-0.pdf          # Sample receipt used for testing


[![Run on Replit](https://replit.com/badge/github/spatnaik123/gemini-receipt-analyzer)](https://replit.com/new/github/spatnaik123/gemini-receipt-analyzer)
