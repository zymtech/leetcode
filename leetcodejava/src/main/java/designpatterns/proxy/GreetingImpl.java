package designpatterns.proxy;

/**
 * Created by Administrator on 10/27/2016.
 */
public class GreetingImpl implements Greeting{
    @Override
    public void sayHello(String name){
        before();
        System.out.println("Hello " + name);
        after();
    }

    private void before(){
        System.out.println("Before");
    }

    private void after(){
        System.out.println("After");
    }
}
