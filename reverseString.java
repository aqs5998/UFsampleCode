
java.util.*;

String name = "Sanchez";
String[] reversedString = new String[name.length()];
for(int i = 0;i<name.length();i++){
    reversedString[i] = charAt(name.length() - i);
}

for(int i = 0;i<name.length();i++){
    System.out.print(reversedString[i]);
}
