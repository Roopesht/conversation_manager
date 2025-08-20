# Requirement
Will detect for toxicity in the user's messages. 

## Example
If the meesage from the contact says "Your friend is very bad person, he has not completed his graduation, still he pose like a graduate"
The above message has to be tagged as Toxic

## Implementation
1. Read all the latest messages from every one.
2. Get the message 1 by 1
3. Construct a prompt  to detect the toxicity in side the message
4. Call the LLM API (providing the prompt)
5. If the LLM responds true, then respond to the contact, saying "The message is toxic, you are not appreciating it politely"

## How to find if it Toxic
Check if its toxic, do not complain if its mildly toxic: {msg}