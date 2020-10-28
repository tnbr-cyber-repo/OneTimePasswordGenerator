# Cybersecurity Foundations

## Project 1 - Python Scripting
<p>
    This was a learning challenge:
</p>
<ol>
<li>Learn Python within 2 weeks</li>
<li>Develop the 2 programs</li>
</ol>

### Program 1: Password Guessing Tool
<p>
    Write a Python script that prompts the user to enter a guessed password value and responds back by confirming if the provided password matches the one in the system or not.
</p>  
<p>
    Use <b>crypt.crypt(word, salt)</b> to perform this validation.
</p>
<hr>
<em>
    <p>
        <b>N.B.</b> I had 2 different perspectives on how to approach this script. So I created 2 programs to explore both options:    
    </p>
    <p>
        program1_pgt.py adheres to Lecturer's requirement, where the program should detect the identity (username) of the user logged in and accept a guess attempt and return a result.
    </p>
    <p>
        program1_pgt1.py allows user to enter a username that may have logged into the current machine recently and accept a guess password.
    </p>
</em>
### Program 2: One-Time Password Generator
<p>
    Implement a One-Time Password generator using the following algorithm.  
</p>
<p>
    Hash Feedback One-Time Password Algorithm described in the following chart.   
</p>
<p>
    Secret key is used as the initialization vector. The first OTP is generated by hashing this vector.  
</p>
<p>
    The second OTP is generated by hashing the hash generated by the first the 1st OTP, and so on.  
</p>
<p>
    The OTP is calculated by truncating the hash into a six digit hexadecimal value.  
</p>
<p>
    The most significant hex digits will be extracted as the OTP.
</p>
<p>
    Use the following hexadecimal value for the <b>Key: 810770FF00FF07012</b>.  
</p>
<p>
    Use <b>hashlib.sha256(input_message).hexdigest()</b> to calculate the hash digest.  
</p>
<p>
    Write a Python script that will generate a display on the screen the first 100 OTPs generated by the above algorithm.
</p>
<hr>  
<p>
    With God's guidance and determination to succeed, I completed the challenge on time.
</p>  
<p>
    My curiosity begun to grow as I learn more about coding with Python and I begun exploring other options for achieving the same request.
</p>   