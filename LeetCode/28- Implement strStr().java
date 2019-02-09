// 			Q) 28. Implement strStr()
// 			https://leetcode.com/problems/implement-strstr/description/
//code
class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.length() == 0){
            return 0;
        }
        if(needle.length() > haystack.length()){
            return -1;
        }
        int i =0;
        int j =0;
        int matched_count =0;
        int first_index = -1;
        while(i< haystack.length() && j < needle.length()){
            //System.out.println(haystack.charAt(i) + " " + needle.charAt(j));
            if(haystack.charAt(i) == needle.charAt(j)){
                if(first_index == -1){
                    first_index = i;
                }
                i+=1;
                j+=1;
                matched_count+=1;
            }else{
                if(first_index!= -1){
                i = first_index+1;
                first_index=-1;
                matched_count=0;
                }else{
                    i+=1;
                }
                j=0;
            }
        }
        if(matched_count == needle.length()){
            return first_index;
        }
        return -1;
    }
}