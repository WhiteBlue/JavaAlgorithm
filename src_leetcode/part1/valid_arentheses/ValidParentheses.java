package part1.valid_arentheses;

/**
 * id: 20
 * <p>
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
 */
public class ValidParentheses {

    public boolean isValid(String s) {
        if (s.length() == 1) {
            return false;
        }
        char[] stack = new char[s.length() + 1];
        int count = 0;
        stack[0] = s.charAt(0);

        for (int i = 1; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case '(':
                case '[':
                case '{': {
                    count++;
                    stack[count] = s.charAt(i);
                    break;
                }
                case '}':
                case ']':
                case ')': {
                    if (count < 0) {
                        return false;
                    }
                    String target = "" + stack[count] + s.charAt(i);
                    if (target.equals("{}") || target.equals("[]") || target.equals("()")) {
                        count--;
                    } else {
                        return false;
                    }
                    break;
                }
                default: {
                    return false;
                }
            }
        }
        return count < 0;
    }


}
