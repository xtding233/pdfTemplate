from pdfTemplate import build_elements_from_csv, build_template_from_ini

print("Build tempalte from ini file")
build_template_from_ini(path_ini=r".\example\config\four_block.ini", format="Letter", title = "Three Block",
                        output_path=r".\example\output\four_block_from_ini.pdf")