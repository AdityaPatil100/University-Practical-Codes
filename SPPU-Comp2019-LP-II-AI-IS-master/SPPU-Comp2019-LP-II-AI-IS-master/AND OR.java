package demo;

public class company {
	
	    public static void main(String s[]){

	        String Message="HelloWorld";
	        int var1 = 127;
	        int var2[]= new int[20];

	        System.out.println("----------- AND Values ----------");

	        for (int i = 0; i<Message.length(); i++){
	            var2[i]= 127 & Message.charAt(i);
	            System.out.println("127 & "+ Message.charAt(i) + " is = "+var2[i]);
	        }
	        for (int i = 0; i<Message.length(); i++){
	            System.out.println("Binary value of  "+ var2[i] +" = "+ Integer.toBinaryString(var2[i]));
	        }

	        System.out.println("----------- OR Values ----------");

	        for (int i = 0; i<Message.length(); i++){
	            var2[i]= 127 | Message.charAt(i);
	            System.out.println("127 OR "+ Message.charAt(i) + " is = "+var2[i]);
	        }
	        for (int i = 0; i<Message.length(); i++){
	            System.out.println("Binary value of "+ var2[i] +" = "+ Integer.toBinaryString(var2[i]));
	        }

	        System.out.println("--------------- XOR Values -------------");

	        for (int i = 0; i<Message.length(); i++){
	            var2[i]= 127 ^ Message.charAt(i);
	            System.out.println("127 XOR "+ Message.charAt(i) + " is = "+var2[i]);
	        }
	        for (int i = 0; i<Message.length(); i++){
	            System.out.println("Binary value of "+ var2[i] +" = "+Integer.toBinaryString(var2[i]));
	        }
	    }
	}



