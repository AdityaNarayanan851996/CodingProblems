// 			Q) 71. Simplify Path
// 			https://leetcode.com/problems/simplify-path/description/
//code
class Solution {
    public String simplifyPath(String path) {
        
        //List<Character> l = new ArrayList<>();
        //l.add(path.charAt(0));
        if(path.length() > 0){
            String s = "";
            s += path.charAt(0);
            for(int i=1;i<path.length();i++){
                //System.out.println(Character.isLetter(path.charAt(i)));
                if(path.charAt(i) == '/'){
                    if(path.charAt(i-1) != '/'){
                        //l.add(path.charAt(i));
                        s +=path.charAt(i);

                    }
                }else{
                    //l.add(path.charAt(i));
                    s +=path.charAt(i);
                }
            }
            Stack<String> st = new Stack<>();
            //System.out.println(s);
            String[] m = s.split("/");
            //if(m.length>1){
            //     m[0] = "/";
            //}
           
            //System.out.println(Arrays.toString(m));
            for(int i=0;i<m.length;i++){
                 if(m[i].equals( "..")){
                    if(!st.isEmpty()){
                        st.pop();
                    }else{
                      //  st.push("/");
                    }
                 }
                else if(m[i].equals(".") || m[i].equals("/") || m[i].equals("")){
                   continue;
                }
                else{
                     st.push("/"+m[i]);
                }
                //System.out.println(st);


            }
            String final_str = "";
            if(st.isEmpty()){
                final_str="/";
            }
            for(String t:st){
                final_str+=t;
            }
            //System.out.println(st);
            return final_str;

        }
        return path;
    }
}