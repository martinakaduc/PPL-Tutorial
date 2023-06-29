import os

cf = os.path.abspath(__file__)
td = os.path.dirname(cf)
print(td)

modules = os.listdir(td)
modules = [module for module in modules if os.path.isdir(
    os.path.join(td, module))]

for module in modules:
    print("Testing", module)
    examples = os.listdir(os.path.join(td, module))
    for example in examples:
        if 'Example' not in example:
            continue

        os.system(
            f'''
            cd "{td}/{module}/{example}/LanguageGenerator" && python gen.py BKIT.g4
            '''
        )

        os.system(
            f'''
            cd "{td}/{module}/{example}/FinalProgram" && python run.py testcase.txt
            '''
        )
