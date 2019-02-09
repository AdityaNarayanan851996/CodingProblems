// 			Q) 833. Find And Replace in String
// 			https://leetcode.com/problems/find-and-replace-in-string/description/
//code
class Solution {
    public String findReplaceString(String S, int[] indexes, String[] sources, String[] targets) {
        
        String rep ="";
        int k=0;
        int i=0;
        HashMap<Integer,List<String>> map = new HashMap<>();
        for(int m=0; m< indexes.length;m++){
            map.put(indexes[m],new ArrayList<String>(Arrays.asList(sources[m],targets[m])));
        } 
        Arrays.sort(indexes);
        for(int m=0;m<indexes.length;m++){
            
            sources[m] = ((map.get(indexes[m])).get(0));
            targets[m] = ((map.get(indexes[m])).get(1));
            //System.out.println(indexes[m] +" " +sources[m] + " "+ targets[m]);
        }
       
        List<Integer> indxs = new ArrayList<>();
        
        for(int j=0; j<indexes.length;j++){
            indxs.add(indexes[j]);
        }
      
        while(i < S.length()){
            if(!indxs.contains(i)){
                rep += S.charAt(i);
                i += 1;
            }
            else if(indxs.contains(i)){
                //System.out.println(sources[k] + " " + indexes[k] + " " +S.indexOf(sources[k]));
                int indexof = S.indexOf(sources[k]);
                List<Integer> indexList = new ArrayList<>();
                while(indexof <S.length()){
                    if(indexof == -1){
                        break;
                    }else{
                    indexList.add(indexof);
                    
                    indexof = S.indexOf(sources[k],indexof + 1);
                    }
                }
                    
                
                
                if(indexList.contains(indexes[k])){
                    rep += targets[k];
                    i = i + sources[k].length();
                    
                }else{
                    rep += S.charAt(i);
                    i += 1;
                }
                k += 1;
            }
            //System.out.println(rep);
        }
        //System.out.println(rep);
        return rep;
    }
}