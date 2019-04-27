
package cone;

public class calc {
    
    public static double area(float R,float r, float h){
        float a = R+r;
        float b = R-r;
        double pi = 3.14159265;
        double g = Math.pow(h, 2) + Math.pow(b, 2);
        g = Math.sqrt(g);
        double area = g*a;
        return area*=pi;
    }
    public static double volume(float R,float r, float h){
        double pi = 3.14159265;
        double a = h/3.0;
        a*=pi;
        double b = Math.pow(r, 2);
        double c = Math.pow(R, 2);
        double volume = a*(b+(r*R)+c);
        return volume;
    }
}
