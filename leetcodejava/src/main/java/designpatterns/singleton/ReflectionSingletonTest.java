package designpatterns.singleton;

import java.lang.reflect.Constructor;

/**
 * Created by Administrator on 10/6/2016.
 */
public class ReflectionSingletonTest {
    public static void main(String[] args){
        EagerInitializedSingleton instanceOne = EagerInitializedSingleton.getInstance();
        EagerInitializedSingleton instanceTwo = EagerInitializedSingleton.getInstance();

        try{
            Constructor[] constructors =
                    EagerInitializedSingleton.class.getDeclaredConstructors();
            for (Constructor constructor : constructors){
                constructor.setAccessible(true);
                instanceTwo = (EagerInitializedSingleton) constructor.newInstance();
                break;
            }
            }catch (Exception e){
            e.printStackTrace();
        }

        System.out.println(instanceOne.hashCode());
        System.out.println(instanceTwo.hashCode());
    }
}
