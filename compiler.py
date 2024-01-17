from textx import metamodel_from_file
from textx.export import model_export
from textx.export import metamodel_export
from graphviz import Source

def simplify_2op(obj):
    if not obj.Right:
        return obj.Left

def simplify_1op(obj):
    if not obj.Content:
        return obj.Cont


obj_processors = {
    'AdditiveExpression' : simplify_2op,
    'MultiplicativeExpression' : simplify_2op,
    'PrimaryExpression' : simplify_1op
}


def parse_c_code():
    c_meta = metamodel_from_file("c.tx")
    c_meta.register_obj_processors(obj_processors)
    model = c_meta.model_from_file("hello.c")

    return model,c_meta

ast,model = parse_c_code()

print(ast)

model_export(ast, "entity.dot")
metamodel_export(model, "model.dot")

path = 'entity.dot'
s = Source.from_file(path)
s.view()
