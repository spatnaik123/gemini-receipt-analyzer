from pathlib import Path
import mimetypes

def validate_and_read_pdf(pdf_path):
    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_file}")

    mime_type, _ = mimetypes.guess_type(pdf_path)
    if mime_type != 'application/pdf':
        raise ValueError(f"File is not a valid PDF: {pdf_path} (type: {mime_type})")

    return [
        {
            "mime_type": mime_type,
            "data": pdf_file.read_bytes()
        }
    ]
