# Toot Splitter
This Python program takes a long post as input and breaks it into 500-character blocks suitable for posting on Mastodon. 

You can run the program directly [here](https://colab.research.google.com/github/pbeens/Toot-Splitter/blob/main/toot-splitter.ipynb).

## Program Summary

This Python program takes a long post as input and breaks it into 500-character blocks suitable for posting on Mastodon. It ensures that the threads break between words rather than within them. 

The program initializes a variable called `post` with the long text. It defines a `block_size` of 500 characters and starts a `counter` at 1.

Using a `while` loop, the program iterates as long as there are characters remaining in the `post` variable. In each iteration, it extracts the next block of 500 characters from `post`, ensuring that the break occurs at the last space character within the block. The remaining characters are then updated in the `post` variable for the next iteration.

The program prints each block with the counter prepended as "1/n" (where n is the block number) followed by a space. This format is suitable for posting on Mastodon, where each block represents a part of the original post.

By breaking the long post into smaller, manageable blocks, the program helps users share lengthy content on Mastodon without exceeding the character limit per post.

## Technical Requirements
1. Accept a long post as input: The program should allow the user to input a long text, which will be divided into blocks.

2. Break the post into 500-character blocks: The program should split the long post into smaller blocks, with each block containing a maximum of 500 characters.

3. Ensure breaks occur between words: When dividing the post into blocks, the program should ensure that the breaks occur at the last space character within the 500-character limit. This ensures that words are not split between different blocks.

4. Prepend each block with "1/n" and a space: The program should add a prefix to each block before displaying it. The prefix should consist of "1/n", where n represents the block number, followed by a space.

5. Maintain a counter: The program should keep track of a counter variable that increments with each block. This counter indicates the order of the blocks.

6. Print the blocks: The program should output each block, including the prefix and a newline character, preferably to the console. The output should be suitable for posting on Mastodon, allowing users to share the long post as separate blocks.

## Twitter?

To adapt the program for Twitter, you would need to make the following modification:

Adjust the block size: Twitter has a maximum character limit of 280 characters per tweet. Therefore, you would need to change the block_size variable to 280 to ensure each block fits within a tweet.
