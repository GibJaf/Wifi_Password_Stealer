
<h2> Wifi Password Stealer </h2>

<h5>Description</h5>
<ul>
<li>To retrieve ssid and wifi passwords stored on another device.</li>
<li>Can be used to penetrate target network without having to capture
4-way handshake and then trying to crack it.</li>
</ul>

<h5> Requirements </h5>
Python3.6

<h5> How to use </h5>
<ol>
<li>Start server application on your machine : <b>python server.py</b></li>
<li>Social engineer the victim to download the client file and run using
python3.6 : <b> python client.py </b> </li>
<li>A file of mac address of victim as name containing ssid and WPA2_PSk <br> 
will be generated in victims folder </li>
<li> Server will autoamatically create Wordlist by extracting unique PSK from all victim files </li>
<li> To search for password for a certain SSID : <b>python search.py</b> </li>
</ol>

<h5> Disadvantage of 4-way handshake cracking  </h5>
<ol> 
	<li> Cracking the 4-way handshake can be a very time-consuming process </li>
	<li> It has a low success rate . </li>
	<li> You need to have correct password in your wordlist </li>
	<li> To speeden up the process requires expensive GPUs </li>
</ol>

<h5> Advantage of Wifi_Password_Stealer  </h5>
<ol> 
        <li> Works very fast .</li>
        <li> Almost 100% success rate  </li>
        <li> No need to know or guess the correct password </li>
        <li> No need of expensive GPUs </li>
</ol>




<h5>Contact</h5> 
 gibraan.jafar@viit.ac.in
