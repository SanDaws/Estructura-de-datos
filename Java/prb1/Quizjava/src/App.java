import java.util.Scanner;

public class App {
    class anidado{
        //esto es un a clase dentro de otra, nested classes ayudan al encapsulamiento
        public void anidado(){System.out.println("mirame, estoy anidado dentro de una clase");    }
    
    public class llema {
        private String definicion= "yo soy la llema, funcion dentro de funcion, y haz accedido a mi";
    } 
    }

    enum listaEjercicios{
    //aqui pondremos nombre a todos los ejercicios que hagamos
    NESTED,
    INNER }
    

    public static void main(String[] args) throws Exception {
        Scanner in= new Scanner(System.in);
        System.out.print("Sellecciones su interaccion: ");
        listaEjercicios ejercicio;

        ejercicio=listaEjercicios.NESTED;
        switch (ejercicio) {
            case NESTED:
                
                break;
        
            default:
                break;
        }
    }

}

