class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
            
                if bracket_map[char] != top_element:
                        return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched correctly
        return len(stack) == 0