package designpatterns.singleton;

/**
 * Created by Administrator on 10/6/2016.
 */
public class LazyInitializedSingleton {
    private static LazyInitializedSingleton instance;
    private LazyInitializedSingleton(){}

    public static LazyInitializedSingleton getInstance(){
        if (instance == null){
            instance = new LazyInitializedSingleton();
        }
        return instance;
    }
}
