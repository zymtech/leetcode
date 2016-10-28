package designpatterns.proxy;

/**
 * Created by Administrator on 10/27/2016.
 */
public class Client {

    public static void main(String[] args){
        //testGreetingProxy();
        //testJDKDynamicProxy();
        testCGLibDynamicProxy();
    }

    private static void testGreetingProxy(){
        Greeting greetingProxy = new GreetingProxy(new GreetingImpl());
        greetingProxy.sayHello("Jack");
    }

    private static void testJDKDynamicProxy(){
        Greeting greeting = new JDKDynamicProxy(new GreetingImpl()).getProxy();
        greeting.sayHello("Jack");
    }

    private static void testCGLibDynamicProxy(){
        Greeting greeting = CGLibDynamicProxy.getInstance().getProxy(
                GreetingImpl.class
        );
        greeting.sayHello("Jack");
    }
}
