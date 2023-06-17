from pdfTemplate import build_template_from_html

build_template_from_html(path_html = r".\example\config\html_template.html", format="Letter", title = "HTML",
                        output_path=r".\example\output\from_html.pdf")

build_template_from_html(path_html = r".\example\config\html_table.html", format="Letter", title = "HTML",
                        output_path=r".\example\output\from_html_table.pdf")
