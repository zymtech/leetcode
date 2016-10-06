package designpatterns.singleton;

/**
 * Created by Administrator on 10/6/2016.
 */
public class StaticBlockSingleton {
    private static StaticBlockSingleton instance;
    private StaticBlockSingleton(){}

    static {
        try{
            instance = new StaticBlockSingleton();
        }catch (Exception e){
            throw new RuntimeException("Exception occured in creating singleton instance");
        }
    }

    public static StaticBlockSingleton getInstance(){
        return instance;
    }
}
