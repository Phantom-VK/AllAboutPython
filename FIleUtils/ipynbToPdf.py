import os
from nbconvert import PDFExporter
import nbformat


def convert_ipynb_to_pdf(notebook_path, output_path=None):
    """
    Convert a Jupyter Notebook to PDF using nbconvert

    Args:
        notebook_path (str): Path to the input .ipynb file
        output_path (str, optional): Path for the output PDF. Defaults to same directory as input.
    """
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Create PDF exporter
    pdf_exporter = PDFExporter()

    # Configure the exporter (optional)
    pdf_exporter.exclude_input_prompt = True
    pdf_exporter.exclude_output_prompt = True

    # Convert to PDF
    body, resources = pdf_exporter.from_notebook_node(nb)

    # Set output path if not provided
    if output_path is None:
        output_path = os.path.splitext(notebook_path)[0] + '.pdf'

    # Write to file
    with open(output_path, 'wb') as f:
        f.write(body)

    print(f"PDF successfully created at: {output_path}")


# Example usage
convert_ipynb_to_pdf('example_notebook.ipynb')