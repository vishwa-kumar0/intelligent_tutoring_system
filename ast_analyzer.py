import ast

class AdvancedCodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.issues = []
        self.concepts_used = set()
        self.loop_depth = 0
        self.assigned_vars = set()
        self.used_vars = set()

    def visit_FunctionDef(self, node):
        self.concepts_used.add("function_definition")
        if not ast.get_docstring(node):
            self.issues.append({"type": "missing_docstring", "line": node.lineno, "func": node.name})
        self.generic_visit(node)

    def visit_For(self, node):
        self.concepts_used.add("for_loop")
        self.loop_depth += 1
        if self.loop_depth > 1:
            self.issues.append({"type": "nested_loop", "line": node.lineno})
            self.concepts_used.add("nested_loops")
        self.generic_visit(node)
        self.loop_depth -= 1

    def visit_While(self, node):
        self.concepts_used.add("while_loop")
        if isinstance(node.test, ast.Constant) and node.test.value is True:
            has_break = any(isinstance(n, ast.Break) for n in ast.walk(node))
            if not has_break:
                self.issues.append({"type": "infinite_while_loop", "line": node.lineno})
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.assigned_vars.add(node.id)
        elif isinstance(node.ctx, ast.Load):
            self.used_vars.add(node.id)
        self.generic_visit(node)

def analyze_code(source_code):
    try:
        tree = ast.parse(source_code)
        analyzer = AdvancedCodeAnalyzer()
        analyzer.visit(tree)
        
        unused = analyzer.assigned_vars - analyzer.used_vars
        for var in unused:
            analyzer.issues.append({"type": "unused_variable", "var_name": var})
            
        return {
            "parsed_successfully": True,
            "issues": analyzer.issues,
            "concepts": list(analyzer.concepts_used),
            "error_msg": None
        }
    except SyntaxError as e:
        return {
            "parsed_successfully": False,
            "issues": [{"type": "syntax_error", "line": e.lineno, "msg": e.msg}],
            "concepts": [],
            "error_msg": f"Syntax Error on line {e.lineno}: {e.msg}"
        }
