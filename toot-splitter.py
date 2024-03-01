# Edit the post variablebe before running the code!
post = """Mastodon is a free and open-source self-hosted social networking service. It allows anyone to host their own server node in the network, and its various separately operated user bases are federated across many different servers. These nodes are referred to as "instances" by Mastodon users. As of October 2021, there are more than 5,000 instances hosting more than 4.5 million users.
Each user is a member of a specific Mastodon instance, and can also communicate with users on different instances through federation. Users post short messages called "toots" for others to see, subject to various privacy settings. The service seeks to distinguish itself from Twitter through its orientation towards small communities and community-based, rather than top-down, moderation."""

block_size = 500
counter = 1

# Calculate the total number of blocks first
total_blocks = (len(post) // block_size) + 1  # Account for possible remaining text

while len(post) > 0:
    if len(post) <= block_size:
        block = post
        post = ""
    else:
        last_space_index = post[:block_size].rfind(" ")
        block = post[:last_space_index]
        post = post[last_space_index + 1:]

    print(f"{counter}/{total_blocks} {block}\n")  # Use total_blocks
    counter += 1
