# def eval_rec(expression):
#     if not expression:
#         raise("INVALID EXPRESSION")
#     if len(expression) == 1:
#         return expression
    
#     slices = expression.split(':')
#     print(slices)
#     if expression[0]=='T':
#         t_ex=slices[0][2:]
#         return eval_rec(t_ex)
    
#     else:
#         f_ex = ':'.join(slices[1:])
#         return eval_rec(f_ex)


def evaluate_ternary_expression_recursive(expression):
    """
    Evaluates a nested ternary expression recursively by managing a shared index.
    
    Args:
        expression: The ternary expression string (e.g., 'F?a:T?F?b:c').
        
    Returns:
        The result of the evaluation.
    """
    
    # Use a mutable list (pass-by-reference) to track the current index 
    # across recursive calls.
    current_index = [0]
    
    def evaluate_recursive_helper(index_ref):
        """
        Helper function to evaluate a sub-expression starting at index_ref[0].
        Returns the result of the sub-expression.
        Updates index_ref[0] to the index *after* the evaluated sub-expression.
        """
        i = index_ref[0]
        
        # 1. Base Element (Condition)
        # Read the condition (T, F, or single value) and advance the index.
        condition_val = expression[i]
        index_ref[0] += 1
        
        # 2. Check for Base Case or End of Sub-expression
        # If we hit the end of the string OR the next character isn't '?', 
        # this is the final value of a branch.
        if index_ref[0] >= len(expression) or expression[index_ref[0]] != '?':
            return condition_val
            
        # 3. Process '?' (Start of a Ternary Operation)
        index_ref[0] += 1 # Move past '?'
        
        # 4. Recursively evaluate the True Expression
        true_expr_result = evaluate_recursive_helper(index_ref)
        
        # 5. Process ':'
        # CRITICAL FIX: Only attempt to check for and move past the ':' 
        # if the index hasn't gone past the end of the string.
        # This handles the case where a sub-expression is the very last part 
        # of the overall expression (e.g., the 'T?F?b:c' part of ex3).
        if index_ref[0] < len(expression) and expression[index_ref[0]] == ':':
            index_ref[0] += 1 # Move past ':'
            
            # 6. Recursively evaluate the False Expression
            false_expr_result = evaluate_recursive_helper(index_ref)
            
            # 7. Combine Results
            if condition_val == 'T':
                return true_expr_result
            else:
                return false_expr_result
        else:
            # If a '?' was found but no valid ':' followed (and the index is valid), 
            # the expression structure is invalid. For simplicity, we assume 
            # the input expression is valid, so this case means the full 
            # sub-expression was evaluated and we've stopped.
            # However, since a '?' implies a full structure, a missing ':' 
            # after the true_expr is technically an error in a well-formed ternary.
            # We return the condition result based on the true_expr being evaluated.
            return true_expr_result if condition_val == 'T' else 'ERROR: Missing Colon'


    # Start the evaluation from the beginning of the expression
    return evaluate_recursive_helper(current_index)

    
ex1 = 'T?a:b'
ex2 = 'F?a:b'
ex3 = 'F?a:T?T?b:c'
# print(eval_rec(ex1))
# print(eval_rec(ex2))
# print(eval_rec(ex3))
print(evaluate_ternary_expression_recursive(ex1))
print(evaluate_ternary_expression_recursive(ex2))
print(evaluate_ternary_expression_recursive(ex3))