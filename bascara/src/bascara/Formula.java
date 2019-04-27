
package bascara;


public class Formula {
    
    public static double delta(double a,double b,double c){
    
        double del;
        del =  Math.pow(b,2)-4*a*c;
        return del;
    }
    public static double posi(double del,double a,double b){
        
        double resul;
        resul =  (-b+ Math.sqrt(del))/(2.0*a);
        return resul;
    }
    public static double nega(double del,double a,double b){
        
        double resul;
        resul =  (-b- Math.sqrt(del))/(2.0*a);
        return resul;
    }
    public static double inreal(double del,double a){
        
        double resul;
        del *=-1;
        resul = (Math.sqrt(del))/(2.0*a);
        return resul;
    }
    public static double inrealb(double a,double b){
        
        double resul;
        resul =  (-b)/(2.0*a);
        return resul;
    }

    
}
