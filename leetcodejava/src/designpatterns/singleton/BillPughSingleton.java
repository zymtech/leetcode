package designpatterns.singleton;

/**
 * Created by Administrator on 10/6/2016.
 */
public class BillPughSingleton {
    private BillPughSingleton instance;

    private static class SingletonHelper{
        private static final BillPughSingleton INSTANCE = new BillPughSingleton();
    }

    public static BillPughSingleton getInstance(){
        return SingletonHelper.INSTANCE;
    }
}
