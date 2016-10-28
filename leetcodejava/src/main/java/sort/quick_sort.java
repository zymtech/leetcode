package sort;

/**
 * Created by Administrator on 9/29/2016.
 */
public class quick_sort {
    public void quicksort(int[] nums,int low, int high){
        if (low<high){
            int pivot_index = partition(nums, low, high);
            quicksort(nums,low, pivot_index);
            quicksort(nums,pivot_index + 1,high);
        }
    }

    public int partition(int[] nums, int low, int high){
        int pivot_index = low;
        int pivot = nums[pivot_index];
        for (int i=low+1; i< high + 1;i++){
            if (nums[i] < pivot){
                pivot_index += 1;
                if (pivot_index != i){
                    int temp = nums[i];
                    nums[i] = nums[pivot_index];
                    nums[pivot_index] = temp;
                }
            }
        }
        int temp = nums[low];
        nums[low] = nums[pivot_index];
        nums[pivot_index] = temp;
        return pivot_index;
    }
    public static void main(String[] args){
        quick_sort test = new quick_sort();
        int[] nums = {1,2,5,2,3,62,1};
        test.quicksort(nums, 0, nums.length-1);
        for (int i: nums){
            System.out.print(i);
        }
    }
}
