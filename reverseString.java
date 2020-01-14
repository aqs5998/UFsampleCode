
public class reverseString {

    static void main(String[] args){
    
        String name = "Sanchez";
        char[] reversedString = new char[name.length()];
        for(int i = 0;i<name.length();i++){
            char a = name.charAt(1);
            reversedString[i] = a;
        }

        for(int i = 0;i<name.length();i++){
            System.out.print(reversedString[i]);
        }
    }
}


