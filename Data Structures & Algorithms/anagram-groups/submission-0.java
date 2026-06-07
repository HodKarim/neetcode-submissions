class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> idk = new ArrayList<>();
        ArrayList<String> bullshit = new ArrayList<>();
        
        if (strs.length == 0){
            bullshit.add("");
            idk.add(bullshit);
            return idk; 
        }
        if (strs.length == 1) {
            bullshit.add(strs[0]);
            idk.add(bullshit);
            return idk;
        }
        else {
            HashMap<String, ArrayList<String>> ogToNewSpellingHashMap = new HashMap<>();

            for (int x = 0; x < strs.length ; x++){ //make new array
                String check = strs[x]; //original word
                char[] arr = check.toCharArray();
                Arrays.sort(arr);
                String bruh = new String(arr);
                strs[x] = bruh;
                if(ogToNewSpellingHashMap.containsKey(bruh)){
                    ArrayList<String> girlWhat = ogToNewSpellingHashMap.get(bruh);
                    girlWhat.add(check);
                    ogToNewSpellingHashMap.put(strs[x], girlWhat);
                }
                else{
                    ArrayList<String> huh = new ArrayList<>();
                    huh.add(check);
                    ogToNewSpellingHashMap.put(strs[x], huh);
                }
            }  //now we have hashmap with arraylists, just return the values ig
            //for loop ig adding the values to the list list
            
            List<List<String>> listOfLists = new ArrayList<>(ogToNewSpellingHashMap.values());
            return listOfLists;
        }
    }
}