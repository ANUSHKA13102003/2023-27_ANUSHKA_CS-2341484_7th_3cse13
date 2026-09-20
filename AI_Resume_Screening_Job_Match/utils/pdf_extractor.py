"""PDF text extraction helpers."""

def extract_text_from_pdf(pdf_file) -> str:
    """Extract readable text from all pages of an uploaded PDF."""
    try:
        import fitz
    except ImportError as exc:
        raise ValueError("PyMuPDF is not installed. Run: pip install -r requirements.txt") from exc
    try:
        data = pdf_file.read()
        if not data:
            raise ValueError("The uploaded PDF is empty. Please choose another file.")
        document = fitz.open(stream=data, filetype="pdf")
        text = "\n".join(page.get_text("text") for page in document).strip()
        document.close()
    except ValueError:
        raise
    except Exception as exc:
        raise ValueError("This file could not be read as a valid PDF. Please upload a text-based PDF.") from exc
    if not text:
        raise ValueError("No readable text was found in this PDF. Scanned-image PDFs need OCR before use.")
    return text
