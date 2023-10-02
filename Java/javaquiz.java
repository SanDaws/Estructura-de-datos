package Java;

import java.util.Scanner;

enum dificultad{
    //"clase" que representa un grupo de constantes, se puede hacer switch entre ellas
    FACIL,
    MEDIO,
    DIFICIL
}

public class javaquiz {
public Scanner in=new Scanner(System.in);//asi hacemos input
    public void pruebaenum(){
        dificultad definicio= dificultad.MEDIO;
        System.out.println(definicio);
        for(dificultad definicion: dificultad.values()){
            System.out.println(definicion);
        }

    }


    public static void main(String[] args) {
        System.out.print("Seleccione su ejercicio");

        

        
    
 }   
}
