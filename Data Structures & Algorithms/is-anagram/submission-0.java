class Solution {
    public boolean isAnagram(String s, String t) {
        //idea: make two hashmaps:
        //key is letter and value is count
        //anagram means same letters AND same letter count
        //sort letters alphabetically and check if words are equal?

        char[] sArray = s.toCharArray();
        Arrays.sort(sArray);
        String sNew = new String(sArray);

        char[] tArray = t.toCharArray();
        Arrays.sort(tArray);
        String tNew = new String(tArray);

        return tNew.equals(sNew);
    }
}
