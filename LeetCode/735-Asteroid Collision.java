// 			Q) 735. Asteroid Collision
// 			https://leetcode.com/problems/asteroid-collision/description/
//code
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        
        Stack<Integer> st = new Stack<>();
        for(int ast: asteroids){
            if(st.isEmpty()){
                st.push(ast);
            }
            else if(st.peek() > 0 && ast < 0){
                while(st.peek() > 0){
                    
                    if(st.peek() < Math.abs(ast)){
                        st.pop();
                        if(st.isEmpty() || st.peek() < 0){
                            st.push(ast);
                            break;
                        }
                    }else if(st.peek() == Math.abs(ast)){
                        st.pop();
                        break;
                    }
                    else{
                        break;
                    }
                }
            }else{
                st.push(ast);
            }
        
            //System.out.println(st);
        }
        
        Object[] f = st.toArray();
        int[] final_state = new int[f.length];
        for(int i=0;i<f.length;i++){
            final_state[i] = (int) f[i];
        }
        return final_state;
        
    }
}