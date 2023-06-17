from fpdf.template import Template
from converter import Converter


def build_template_from_elements(elements, format = "Letter", title = "Sample", output_path="./template.pdf"):
    f = Template(format=format, elements=elements, title=title)
    f.add_page()
    f.render(output_path)


def build_elements_from_csv(path_csv : str, delimiter = ",", first_line_as_header = False):
    return Converter.from_csv(path_csv, delimiter, first_line_as_header)


def build_elements_from_ini(path_ini : str):
    return Converter.from_ini(path_ini)


def build_template_from_csv(path_csv : str, delimiter=",", first_line_as_header=False,
                            format="Letter",
                            title="Sample", output_path="./template.pdf"):
    return build_template_from_elements(build_elements_from_csv(path_csv, delimiter, first_line_as_header),
                                        format, title, output_path)


def build_template_from_ini(path_ini : str,
                            format="Letter",
                            title="Sample", output_path="./template.pdf"):
    return build_template_from_elements(build_elements_from_ini(path_ini), format, title, output_path)
