package threeSum;

import java.util.Hashtable;

/**
 * Created by Administrator on 7/15/2016.
 */
public class twoSum {
    public int[] twoSum(int[] numbers, int target) {
        if (numbers.length == 0) {
            return null;
        }
        Hashtable<Integer, Integer> memo = new Hashtable<Integer, Integer>();
        int[] result = new int[2];
        for (int i = 0; i < numbers.length; i++) {
            if (memo.containsKey(target - numbers[i])) {
                result[0] = memo.get(target - numbers[i]);
                result[1] = i;
                return result;
            }
            memo.put(numbers[i],i);
        }
        return result;
    }

    public static void main(String[] args) {
        twoSum test = new twoSum();
        int[] numbers = {2, 7, 11, 15};
        int target = 9;
        int[] result;
        result = test.twoSum(numbers, target);
        for (int i:result){
            System.out.println(i);
        }
        for (int i = 0; i<result.length; i ++){
            System.out.println(result[i]);
        }
    }
}



