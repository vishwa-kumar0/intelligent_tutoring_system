def generate_feedback(issues, student_mastery):
    if not issues:
        return "✅ Perfect! Your code is structurally sound and optimal."
        
    feedback = []
    for issue in issues:
        if issue['type'] == 'syntax_error':
            feedback.append(f"🚨 Syntax Error on line {issue['line']}: {issue['msg']}. The code won't run.")
        elif issue['type'] == 'infinite_while_loop':
            mastery = student_mastery.get('while_loop', 0.5)
            if mastery < 0.5:
                feedback.append(f"💡 Line {issue['line']}: A `while True:` loop runs forever. You MUST add a `break` statement inside an `if` block to stop it.")
            else:
                feedback.append(f"🤔 Line {issue['line']}: Infinite loop detected. Remember to manage your control flow exits.")
        elif issue['type'] == 'nested_loop':
            feedback.append(f"⚠️ Line {issue['line']}: You have a nested loop (O(n²) time complexity). If you are processing large data, try using a dictionary instead.")
        elif issue['type'] == 'unused_variable':
            feedback.append(f"🧹 Optimization: You created the variable '{issue['var_name']}' but never used it. Clean it up to save memory.")
        elif issue['type'] == 'missing_docstring':
            feedback.append(f"📝 Style: The function '{issue['func']}' on line {issue['line']} is missing a docstring. Good programmers document their code!")

    return "\n".join(feedback)
