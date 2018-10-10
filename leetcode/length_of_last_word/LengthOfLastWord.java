
/**
 * id: 58
 * <p>
 * Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
 * <p>
 * If the last word does not exist, return 0.
 */

public class LengthOfLastWord {

    public int lengthOfLastWord(String s) {
        int length = 0;
        boolean found = false;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ') {
                if (found) {
                    break;
                }
            } else {
                if (!found) {
                    found = true;
                }
                length++;
            }
        }
        return length;
    }

}
