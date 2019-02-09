// 			Q) 28. Implement strStr()
// 			https://leetcode.com/problems/valid-sudoku/description/
//code
class Solution {
    public int subMatrix(int i,int j){
        
        //int[] subMatArr = new int[9];
        if(i <=2 && j <= 2){
            //subMatArr[0] = 1;
            return 0;
        }
        if(i <=2 && j >=3 && j <=5){
            //subMatArr[1] = 1;
            return 1;
        }
        if(i <=2 && j >=6 && j <=8){
            //subMatArr[2] = 1;
            return 2;
        }
        if(i >=3 && i<=5 && j <= 2){
            //subMatArr[3] = 1;
            return 3;
        }
        if(i >=3 && i<=5 && j >=3 && j <=5){
            //subMatArr[4] = 1;
            return 4;
        }
        if(i >=3 && i<=5 && j >=6 && j <=8){
            //subMatArr[5] = 1;
            return 5;
        }if(i >=6 && i<=8  && j <= 2){
            //subMatArr[6] = 1;
            return 6;
        }
        if(i >=6 && i<=8 && j  >=3 && j <=5){
            //subMatArr[7] = 1;
            return 7;
        }if(i >=6 && i<=8 && j >=6 && j <=8){
            //subMatArr[8] = 1;
            return 8;
        }
        
        return -1;
        
    }
    public boolean isValidSudoku(char[][] board) {
        
        Map<Integer,List<Character>> row_map = new HashMap<>();
        Map<Integer,List<Character>> col_map = new HashMap<>();
        
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[i].length;j++){
                if(board[i][j] != '.'){
                    if(row_map.keySet().contains(i)){
                        List<Character> ll = new ArrayList<>();
                        ll = row_map.get(i);
                        ll.add(board[i][j]);
                        row_map.put(i,ll);
                    }else{
                        List<Character> l = new ArrayList<>();
                        l.add(board[i][j]);
                        row_map.put(i,l);
                    }
                }
            }
            
        }
        for(int i=0;i<board[0].length;i++){
            for(int j=0;j<board.length;j++){
                if(board[j][i] != '.'){
                    
                    if(col_map.keySet().contains(i)){
                        List<Character> ll = new ArrayList<>();
                        ll = col_map.get(i);
                        ll.add(board[j][i]);
                        col_map.put(i,ll);
                    }else{
                        List<Character> l = new ArrayList<>();
                        l.add(board[j][i]);
                        col_map.put(i,l);
                    }
                }
            }
            
        }
        for(int key:row_map.keySet()){
            Set<Character> set_row = new HashSet<>((row_map.get(key)));
            if(set_row.size() != (row_map.get(key)).size()){
                return false;
            }
        }
        
        for(int key:col_map.keySet()){
            Set<Character> set_col = new HashSet<>((col_map.get(key)));
            if(set_col.size() != (col_map.get(key)).size()){
                return false;
            }
        }
        
        Map<Integer,List<Character>> subMat_map = new HashMap<>();
        ///List<Integer> l = new ArrayList<>(Arrays.asList(1,2,3,5));
        for(int i=0;i<board.length;i++){ 
            for(int j=0;j<board[i].length;j++){
                if(board[i][j] != '.'){
                    if(subMat_map.keySet().contains(subMatrix(i,j))){
                        List<Character> lll = new ArrayList<>();
                        lll = subMat_map.get(subMatrix(i,j));
                        lll.add(board[i][j]);
                        subMat_map.put(subMatrix(i,j),lll);
                    }else{

                        subMat_map.put(subMatrix(i,j),new ArrayList<>(Arrays.asList(board[i][j])));
                    }
                    //System.out.println(subMat_map.get(subMatrix(i,j)) + " " + i + " " +j + " " + subMatrix(i,j));
                }
            
            }
            
        }
        
        for(int key:subMat_map.keySet()){
            //System.out.println(subMat_map.get(key));
            Set<Character> set_submat = new HashSet<>((subMat_map.get(key)));
            if(set_submat.size() != (subMat_map.get(key)).size()){
                //System.out.println("This one!" + key);
                return false;
            }
        }
        
        return true;
        
    }
}