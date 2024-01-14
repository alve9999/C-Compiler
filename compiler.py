from textx import metamodel_from_file
from textx.export import model_export
from textx.export import metamodel_export
from graphviz import Source


def parse_c_code():
    c_meta = metamodel_from_file("c.tx")
    model = c_meta.model_from_file("hello.c")

    return model,c_meta

ast,model = parse_c_code()

print(ast)

model_export(ast, 'entity.dot')
metamodel_export(model, "model.dot")

path = 'entity.dot'
s = Source.from_file(path)
s.view()
