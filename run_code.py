from exec_code import exec_code

def run(code, tests):
    for i,(code_input,expected_output) in enumerate(tests):
        output, time = exec_code(code,code_input)
        if output.rstrip() == expected_output.rstrip():
            print(f"Test {i} passed, running time: {time:.3f} seconds.")
        else:
            print(f"Wrong Answer on test {i}")