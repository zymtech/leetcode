package designpatterns.singleton;

/**
 * Created by Administrator on 10/6/2016.
 */
public class EagerInitializedSingleton {
    private static final EagerInitializedSingleton instance =
            new EagerInitializedSingleton();
    private EagerInitializedSingleton(){}

    public static EagerInitializedSingleton getInstance(){
        return instance;
    }
}
