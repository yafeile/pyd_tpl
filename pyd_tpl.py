# encoding:utf-8
import os
import sys

from jinja2 import FileSystemLoader
from jinja2.sandbox import SandboxedEnvironment

IS_WIN = sys.platform == "win32"
IS_PY3 = sys.version_info[0] == 3


def main(module_name="demo", module_type="c"):
    path = os.path.dirname(__file__)
    if IS_PY3:
        _path = os.path.join(path, "py3")
    else:
        _path = os.path.join(path, "py2")
    loader = FileSystemLoader(_path)
    env = SandboxedEnvironment(loader=loader)
    tpl = env.get_template("demo.tpl")
    text = tpl.render({"module_name": module_name})
    # if IS_WIN:
    #     text = """#include "stdafx.h"\n{}
    #     """.format(text)
    fmt = "{}.{}"
    if module_type == "cpp":
        module_type = "cpp"
    else:
        module_type = "c"
    filename = fmt.format(module_name, module_type)
    with open(filename, "w") as f:
        f.write(text)
    print("Generate Module {} success".format(module_name))

if __name__ == '__main__':
    args = sys.argv[1:]
    l = len(args) 
    if l == 2:
        module_name = args[0]
        module_type = args[1]
    elif l == 1:
        module_name = args[0]
        module_type = "c"
    else:
        print("arguments wrong")
        exit()
    main(module_name,module_type)