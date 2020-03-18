//author Michal Jastrzab
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Code code = new Code();
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String binary = code.getBinaryCode(input);
        StringBuilder temp = new StringBuilder("");
        ArrayList<String> byteCodes = new ArrayList<>();
        for (int i = 0; i < binary.length(); ++i) {
            if (i != 0 && i % 8 == 0) {
                byteCodes.add(temp.toString());
                temp.delete(0, 8);
            }
            temp.append(binary.charAt(i));
            if (i == binary.length() - 1) {
                for (int j = temp.length(); j < 8; ++j) {
                    temp.append("0");
                }
                byteCodes.add(temp.toString());
            }
        }
        for (String str : byteCodes) {
            int hex = Integer.parseInt(str, 2);
            String hexToPrint = Integer.toHexString(hex).toUpperCase();
            if (hexToPrint.length() == 1) {
                System.out.println("0" + hexToPrint + " ");
            } else {
                System.out.println(hexToPrint + " ");
            }
        }
    }
}

class Code {
    static final Map<Character, String> codes = new HashMap<Character, String>() {{
        put(' ', "11");
        put(' ', "11");
        put('e', "101");
        put('t', "1001");
        put('o', "10001");
        put('n', "10000");
        put('a', "011");
        put('s', "0101");
        put('i', "01001");
        put('r', "01000");
        put('h', "0011");
        put('d', "00101");
        put('l', "001001");
        put('!', "001000");
        put('u', "00011");
        put('c', "000101");
        put('f', "000100");
        put('m', "000011");
        put('p', "0000101");
        put('g', "0000100");
        put('w', "0000011");
        put('b', "0000010");
        put('y', "0000001");
        put('v', "00000001");
        put('j', "000000001");
        put('k', "0000000001");
        put('x', "00000000001");
        put('q', "000000000001");
        put('z', "000000000000");
    }};
    public String getBinaryCode(String string) {
        StringBuilder binary = new StringBuilder("");
        for (char ch : string.toCharArray()) {
            binary.append(codes.get(ch));
        }
        return binary.toString();
    }
}
