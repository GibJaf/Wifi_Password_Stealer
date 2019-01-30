
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
</ol>


<!-- <h5>Limitations</h5>
<ul>
<li>As of now it only works if client and server are in same network which
totally defeats the point of penetrating a network .</li>
 <li>If anyone knows how to make it such that it can work over different 
networks , please help me improve it accordingly </li>  -->
</ul>

<h5>Contact</h5> 
 gibraan.jafar@viit.ac.in
