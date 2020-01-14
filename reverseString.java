
public class reverseString {

    public static void main(String[] args){
    // Reversed string by putting reverse string in an array
        String name = "Sanchez";
        char[] reversedString = new char[name.length()];
        for(int i = 0;i<name.length();i++){
            char a = name.charAt(name.length() - i - 1);
            reversedString[i] = a;
        }

        for(int i = 0;i<name.length();i++){
            System.out.print(reversedString[i]);
        }
        System.out.println("");
    }
}


