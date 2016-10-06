package designpatterns.singleton;

/**
 * Created by Administrator on 10/6/2016.
 */
public class ThreadSafeLazySingleton {
    private static ThreadSafeLazySingleton instance;
    private ThreadSafeLazySingleton(){}

    public static synchronized ThreadSafeLazySingleton getInstance(){
        if (instance == null){
            instance = new ThreadSafeLazySingleton();
        }
        return instance;
    }
}
