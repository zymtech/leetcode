package lengthOfLongestSubstring;
/*Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
 * For "bbbbb" the longest substring is "b", with the length of 1.
 */
public class LengthOfLongestSubstring {
	public int lengthOfLongestSubstring(String s){
		if (s==null) return 0;
		char[] str=s.toCharArray();
		if(str.length==0) return 0;
		
		int max=1;
		
		int barrier=0;
		
		for(int i=1;i<str.length;i++){
			for(int j=i-1;j>=barrier;j-- )
			{
				if(str[i]==str[j])
				{
					barrier=j+1;
					break;
				}
			}
			max=Math.max(max,i-barrier+1);
		}
		return max;
	}
	
	
}
