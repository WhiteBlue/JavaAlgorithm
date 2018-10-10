package part2.count_and_say;

/**
 * id: 38
 * <p>
 * The count-and-say sequence is the sequence of integers beginning as follows:
 * 1, 11, 21, 1211, 111221, ...
 * <p>
 * 1 is read off as "one 1" or 11.
 * 11 is read off as "two 1s" or 21.
 * 21 is read off as "one 2, then one 1" or 1211.
 * Given an integer n, generate the nth sequence.
 * <p>
 * Note: The sequence of integers will be represented as a string.
 */
public class CountAndSay {

    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        } else {
            String target = countAndSay(n - 1);
            StringBuilder stringBuilder = new StringBuilder();
            char tmp = target.charAt(0);
            int count = 1;
            for (int j = 1; j < target.length(); j++) {
                if (target.charAt(j) != tmp) {
                    stringBuilder.append(count).append(tmp);
                    tmp = target.charAt(j);
                    count = 1;
                } else {
                    count++;
                }
            }
            stringBuilder.append(count).append(tmp);
            return stringBuilder.toString();
        }
    }


}
