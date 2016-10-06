package designpatterns.singleton;

/**
 * Created by Administrator on 10/6/2016.
 */
public class DoubleLockingSingleton {
    private static DoubleLockingSingleton instance;
    private DoubleLockingSingleton(){}

    public static DoubleLockingSingleton getInstance(){
        if (instance == null){
            synchronized (DoubleLockingSingleton.class){
                if (instance == null){
                    instance = new DoubleLockingSingleton();
                }
            }
        }
        return instance;
    }
}
