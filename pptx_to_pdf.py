import os
import comtypes.client

def convert_pptx_to_pdf(input_pptx, output_pdf):
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = 1

    ppt = powerpoint.Presentations.Open(input_pptx)
    ppt.SaveAs(output_pdf, 32)  # 32 represents PDF format

    ppt.Close()
    powerpoint.Quit()

if __name__ == "__main__":
    input_directory = "C:\\Users\\lnsnd\\OneDrive\\문서\\DWU\\운영체제\\pptx" #input directory
    output_directory = "C:\\Users\\lnsnd\\OneDrive\\문서\\DWU\\운영체제\\pdf" #output directory

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    pptx_files = [file for file in os.listdir(input_directory) if file.endswith(".pptx")]

    for pptx_file in pptx_files:
        input_pptx_path = os.path.join(input_directory, pptx_file)
        output_pdf_path = os.path.join(output_directory, os.path.splitext(pptx_file)[0] + ".pdf")

        convert_pptx_to_pdf(input_pptx_path, output_pdf_path)

    print("Conversion completed. PDF files are saved in the output directory.")
