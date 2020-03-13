<h1> RoboCar</h1> 
<h2 > Comandos para secuencia de ejecución </h2>
<h3> Instalación de recursos previos </h3>
<ul>
  <li>sudo apt-get install ros-melodic-octomap</li>
  <li>git clone https://github.com/FelipeVelazquez/RoboCar.git</li>
</ul>
<br> Añadir el espacio de trabajo de RoboCar al archivo .bashrc </br>
<h3>Hardware utilizado</h3>
<ul>
	<li>RPLIDAR V2</li>
	<img src="images/rplidar.jpg" width="400"> 
	<li>Camara estereo ZED 2</li>
	<img src="images/zed2.jpg" width="400">
	<li>Mbed LPC1768 + Aplication board</li>
	<img src="images/mbed.jpg" width="400">
	<li>Nvidia Jetson nano</li>
	<img src="images/jetson.jpg" width="400">
</ul>
<h3> Comandos para ejecución </h3>
<ol>
  <li >roslaunch rplidar rplidar.lauch</li>
  <li >roslaunch zed_wrapper zed2.launch</li>
  <li >rosrun odometria control.py</li>
  <li >rosrun gmapping slam_gmapping</li>
  <li >roslaunch octomap_server octomap_mapping.launch</li>
  <li >rosrun ia Data_recolect.py</li>
  <li >rosrun ia scan_test.py</li>
</ol>
