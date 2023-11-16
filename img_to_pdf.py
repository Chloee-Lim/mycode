from PIL import Image
from reportlab.pdfgen import canvas
from os import listdir
from os.path import isfile, join, splitext

def convert_images_to_pdf(input_folder, output_folder, output_pdf_name):
    image_files = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
    image_files.sort()  # 정렬이 필요한 경우

    output_pdf_path = join(output_folder, output_pdf_name)

    pdf = canvas.Canvas(output_pdf_path)

    for image_file in image_files:
        image_path = join(input_folder, image_file)

        try:
            img = Image.open(image_path)
            width, height = img.size

            # 페이지 크기를 이미지 크기에 맞게 설정
            pdf.setPageSize((width, height))
            pdf.drawInlineImage(image_path, 0, 0, width, height)

            pdf.showPage()  # 새 페이지로 이동

        except Exception as e:
            print(f"Error processing {image_file}: {e}")

    pdf.save()
    print(f"PDF 생성이 완료되었습니다: {output_pdf_path}")

# 사용 예제
input_folder = "C:\\Users\\lnsnd\\OneDrive\\문서\\DWU\\운영체제\\pr9"
output_folder = "C:\\Users\\lnsnd\\OneDrive\\문서\\DWU\\운영체제\\pr9"
output_pdf_name = "ouput.pdf"

convert_images_to_pdf(input_folder, output_folder, output_pdf_name)
