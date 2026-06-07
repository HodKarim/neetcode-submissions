class Solution:

    def encode(self, strs: List[str]) -> str:
        # create empty string to store encoded result
        encoded = ""

        # go thru every word in strs
        for word in strs:
            # add the length of the word, then a special separator, then the word
            # example: "hello" becomes "5#hello"
            encoded += str(len(word)) + "#" + word

        # return the final encoded string
        return encoded

    def decode(self, s: str) -> List[str]:
        # create list to store decoded words
        result = []

        # pointer that moves thru the encoded string
        i = 0

        # keep going while pointer is inside the string
        while i < len(s):
            # j will find where the # separator is
            j = i

            # move j until it reaches #
            # everything before # is the length of the next word
            while s[j] != "#":
                j += 1

            # get the length of the next word
            length = int(s[i:j])

            # the actual word starts right after #
            word_start = j + 1

            # the word ends after length characters
            word_end = word_start + length

            # add the decoded word into result
            result.append(s[word_start:word_end])

            # move i to the start of the next encoded word
            i = word_end

        # return the original list of strings
        return result


        """
        Pattern Type: String Parsing + Encoding pattern

        need to turn list of strings into one string, then be able to split it back correctly.
        use the length of each word before the word so decode knows exactly how many characters to read.

        Time Complexity:
        O(n), because go thru every character while encoding and decoding

        Space Complexity:
        O(n), because store the encoded string and decoded list

        How long it took: 35 minutes
        """