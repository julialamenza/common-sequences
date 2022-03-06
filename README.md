## Common three word sequences.
**Python program executable from the command line that when given text(s) will return a list of the 100 most common three word sequences.**

### USAGE
For run this code you can run the commands below:

    python3 solution.py <moby-dick.txt>
 
If you wanna run multiples txt files  just run as it:

    python3 solution.py <moby-dick.txt> <other-filex.txt>

This program also accept **input** on **stdin**

    cat moby-dick.txt | python3 solution.py
 **This Works!!**
 
 ### DOCKER USAGE
 Inside this folder you will find a Dockerfile.
 If you wanna run it as a container you just need to build the image

     docker build  -t <tag-name> .
 And run the container
 
     docker run <container:tag-name>