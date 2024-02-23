
from fpdf import FPDF
class Shirt(FPDF):
    def __init__(self, name ,output_file="shirtificate.pdf"):
        super().__init__()
        self._name = name
        self.add_page()
        self.set_font('helvetica', size=40)
        self.multi_cell(0, 50, text="CS50 Shirtificate" , align='C')
        self.image("shirtificate.png", x=10, y=80, w = 190, keep_aspect_ratio=True)
        self.set_text_color(255, 255, 255)
        self.set_y(125)
        self.set_x(35)
        self.cell_width = 140
        self.multi_cell(self.cell_width, 25, text=f"{name} took CS50", align='C')
        self.output(output_file)


name = input("Name: ")
pdf = Shirt(name)
